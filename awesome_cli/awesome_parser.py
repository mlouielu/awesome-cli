from typing import List

import colorful
import mistune
from lxml import etree


class Section:
    def __init__(self, title, level):
        self.title = title
        self.level = level
        self.items = []

    def show(self, show_items=True, show_url=True):
        # Title
        emoji = "✨" if self.level == 2 else "- 💥"
        print(f"{emoji} {colorful.bold(self.title)}")

        # Don't print items
        if not show_items:
            return

        # Items
        for item in self.items:
            print(f'{colorful.bold_orange(item["title"])} - {item["description"]}')
            if show_url:
                print(colorful.grey(f'🔗 {item["url"]}'))
        print()


class Parser(mistune.Renderer):
    sections = []

    def header(self, text, level, raw=None):
        self.sections.append(Section(text, level))
        return ""

    def list(self, body, ordered=True):
        root = etree.HTML(body)
        for name in root.xpath("//li/descendant::a[1]"):
            title = name.text
            url = name.get("href")
            description = "".join(
                map(
                    lambda n: n if isinstance(n, str) else n.text,
                    name.xpath("following-sibling::node()"),
                )
            ).strip(" -")

            self.sections[-1].items.append(
                {"title": title, "url": url, "description": description}
            )
        return ""


def parse(filename: str) -> List[Section]:
    renderer = Parser()
    md = mistune.Markdown(renderer=renderer)
    md(open(filename).read())

    return renderer.sections

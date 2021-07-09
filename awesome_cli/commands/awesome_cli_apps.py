import os
import pathlib

from cleo import Command
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle, prompt, clear

from awesome_cli import awesome_parser


PACKAGE_DIRECTORY = pathlib.Path(
    os.path.dirname(os.path.abspath(awesome_parser.__file__))
)
MARKDOWN_PATH = PACKAGE_DIRECTORY / "data" / "agarrharr-awesome-cli-apps.md"


class AwesomeCliAppsCommand(Command):
    """
    Awesome CLI Apps

    awesome-cli-apps
        {--k|--header-only : If set, only print out header }
        {--u|--exclude-url : If set, don't print url }
        {--i|--interactive : Interactive mode }"""

    def handle(self):
        import os

        sections = awesome_parser.parse(MARKDOWN_PATH)

        if self.option("interactive"):

            def pre_run():
                from prompt_toolkit.application import get_app

                app = get_app()
                b = app.current_buffer
                if b.complete_state:
                    b.complete_next()
                else:
                    b.start_completion(select_first=False)

            completer = WordCompleter(
                [
                    f'{index:02d}. {" -" if section.level == 3 else ""} {section.title}'
                    f" ({len(section.items)})"
                    for index, section in enumerate(sections)
                ]
            )

            while True:
                section_select = prompt(
                    "Please select one section to show: ",
                    completer=completer,
                    complete_style=CompleteStyle.MULTI_COLUMN,
                    pre_run=pre_run,
                )

                clear()  # Clear screen after new selection

                try:
                    index = int(section_select[:2])
                except ValueError:
                    continue
                if 0 <= index < len(sections):
                    sections[index].show(
                        show_items=not self.option("header-only"),
                        show_url=not self.option("exclude-url"),
                    )

            return

        # Not interactive
        for section in sections:
            section.show(
                show_items=not self.option("header-only"),
                show_url=not self.option("exclude-url"),
            )

import os
import pathlib

from cleo import Command

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
        {--u|--exclude-url : If set, don't print url }"""

    def handle(self):
        import os

        sections = awesome_parser.parse(MARKDOWN_PATH)
        for section in sections:
            section.show(
                show_items=not self.option("header-only"),
                show_url=not self.option("exclude-url"),
            )

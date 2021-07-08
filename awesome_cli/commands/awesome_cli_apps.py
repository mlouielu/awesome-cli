from cleo import Command

from awesome_cli import awesome_parser


class AwesomeCliAppsCommand(Command):
    """
    Awesome CLI Apps

    awesome-cli-apps
        {--k|--header-only : If set, only print out header }
        {--u|--exclude-url : If set, don't print url }"""

    def handle(self):
        import os

        sections = awesome_parser.parse(
            "awesome_cli/data/agarrharr-awesome-cli-apps.md"
        )
        for section in sections:
            section.show(
                show_items=not self.option("header-only"),
                show_url=not self.option("exclude-url"),
            )

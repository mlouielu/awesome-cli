from cleo import Application as BaseApplication

from .__version__ import __version__

from .commands.awesome_cli_apps import AwesomeCliAppsCommand
from .config import ApplicationConfig


class Application(BaseApplication):
    def __init__(self):
        super(Application, self).__init__(
            config=ApplicationConfig("awesome-cli", __version__)
        )

        self.add(AwesomeCliAppsCommand().default())

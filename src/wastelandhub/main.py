"""Main entry point for WastelandHub application."""

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from wastelandhub.screens.logs_menu import LogsMenuScreen
from wastelandhub.screens.main_menu import MainMenuScreen


class WastelandHubApp(App[None]):
    """A Textual app to simulate a RobCo Industries terminal."""

    CSS_PATH = "styles.tcss"
    TITLE = "WastelandHub - RobCo Terminal"

    # Register screens at class level for proper reuse
    SCREENS = {
        "main_menu": MainMenuScreen,
        "logs_menu": LogsMenuScreen,
    }

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("ctrl+c", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    async def on_mount(self) -> None:
        """Push initial screen."""
        await self.push_screen("main_menu")


def main() -> None:
    """Main entry point for WastelandHub."""
    app = WastelandHubApp()
    app.run()


if __name__ == "__main__":
    main()

"""Main entry point for WastelandHub application."""

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from wastelandhub.screens.main_menu import MainMenuScreen
from wastelandhub.screens.logs_menu import LogsMenuScreen


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

    def __init__(self):
        super().__init__()
        
        # Log data
        self.log_data = {
            "COMM_01": "Communication Log Entry 001\n\nAll communications with the outside world have been severed...",
            "DIARY_05": "Personal Diary Entry 005\n\nDay 127 since the incident. Food supplies running low...",
            "DOOR_CTRL": "Door Control System Log\n\nSECURITY BREACH DETECTED - All blast doors sealed...",
            "SECURITY": "Security Report\n\nMultiple unauthorized access attempts detected...", 
            "MAINTENANCE": "Maintenance Log\n\nCritical systems failure detected in Reactor Bay 3..."
        }

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

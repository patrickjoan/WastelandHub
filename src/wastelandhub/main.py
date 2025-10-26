from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Footer, Header

from wastelandhub.screens.main_menu import MainMenuScreen

# from wastelandhub.screens.hacking import HackingScreen
# from wastelandhub.screens.logs_menu import LogsMenuScreen
# from wastelandhub.widgets.typewriter import Typewriter


class WastelandHubApp(App):
    """Main application class for the Wasteland Hub terminal interface.

    This class defines the UI layout and initial state for the
    RobCo Industries (TM) Terminal simulation using the Textual framework.
    Styling is handled by the external styles.tcss file.
    """

    CSS_PATH = "styles.tcss"
    BINDINGS = [
        ("q", "quit", "Quit the application"),
    ]

    current_screen = reactive("main_menu")
    logged_in_user = reactive("guest")
    terminal_difficulty = reactive(50)

    # Content to display with the typewriter effect
    display_content = reactive("")

    # full dictionary of log data
    log_data = reactive({})

    def __init__(self, *args, **kwargs):
        """Initialize the class instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        super().__init__(*args, **kwargs)

        self.log_data = {
            "COMM_01": ">> RE: FUSION CELL STOCK\nStock is red. Priority re-route from Area 3 required immediately. - J.C.",
            "DIARY_05": "Another day spent in the simulation. I swear I saw a ghoul on the third floor today. Management is lying to us.",
            "DOOR_CTRL": "SYSTEM ONLINE. Access Level 4 Required for override.",
        }

    def compose(self) -> ComposeResult:
        """Keep compose minimal to only the header and footer."""
        yield Header()
        # The main screen content will be pushed dynamically via on_mount
        yield Footer()

    async def on_mount(self) -> None:
        """Called immediately after the app is mounted."""
        self.title = "Wasteland Hub - RobCo Terminal"

        # Register all screens the app can navigate to as instance variables
        self.screens = {
            "main_menu": MainMenuScreen(),
            # 'hacking': HackingScreen(),
            # 'logs_menu': LogsMenuScreen(),
        }

        # PUSH the initial MainMenuScreen onto the stack and wait for it to mount
        await self.push_screen(self.screens["main_menu"])

    # Reactive Watchers (The Controller)

    def watch_display_content(self, new_content: str) -> None:
        """Triggers the typewriter effect on the new content.

        This is the main display controller logic.
        """
        # Placeholder logic:
        # 1. Clear the main display log widget (e.g., query_one(TerminalLog))
        # 2. Start the typewriter process with the new_content

        if new_content:
            # For now, just print to the console while the widgets are built
            print(
                f"--- Triggered Display Update ---\n{new_content}\n--- End Update ---"
            )


def main() -> None:
    app = WastelandHubApp()
    app.run()


if __name__ == "__main__":
    main()

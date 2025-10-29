from textual.app import ComposeResult
from textual.containers import Container, Center
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static


class MainMenuScreen(Screen):
    """The main navigational screen for the RobCo Terminal.
    Displays options like viewing logs, hacking, and logging out.
    """

    DEFAULT_CSS = """
    #menu-container {
        align: center middle;
        content-align: center middle;
        width: 100%;
        padding: 1 2;
        border: round #00ff00;
    }

    .menu-button {
        width: auto;
        align: center top;
        margin-top: 1;
    }
    
    .menu-title, .menu-divider {
        content-align: center middle;
        width: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the screen structure: Header, central menu, and Footer."""
        yield Header()

        with Container(id="menu-container"):
            # The title area
            with Center():
                yield Static(
                    ":: ROBCO INDUSTRIES (TM) TERMINAL ::", classes="menu-title"
                )
                yield Static(
                    "-----------------------------------", classes="menu-divider"
                )

            # Interactive Buttons
            with Center():
                yield Button(
                    "READ LOGS", id="logs", classes="menu-button", variant="primary"
                )
            with Center():
                yield Button(
                    "HACK SYSTEM", id="hack", classes="menu-button", variant="primary"
                )
            with Center():
                yield Button(
                    "LOGOUT", id="logout", classes="menu-button", variant="error"
                )

        yield Footer()

    # --- Controller Logic: Event Handlers ---

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handles navigation when a menu button is pressed."""
        # Get a reference to the App for state and navigation
        app = self.app

        if event.button.id == "logs":
            # PUSH the logs menu screen onto the stack
            await app.push_screen(app.screens["logs_menu"])

        elif event.button.id == "hack":
            # PUSH the hacking screen onto the stack
            # app.push_screen(app.SCREENS['hacking']) # Uncomment when hacking screen is defined
            self.app.log("Navigation: Pushing to hacking screen.")  # Placeholder log

        elif event.button.id == "logout":
            # Since we don't have a login screen, we'll just quit for now
            self.app.exit("Logged out successfully.")

        else:
            self.app.log(f"Unknown button pressed: {event.button.id}")

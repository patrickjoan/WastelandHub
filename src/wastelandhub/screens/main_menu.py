from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static

# Import the App class type for type hinting and access


class MainMenuScreen(Screen):
    """The main navigational screen for the RobCo Terminal.
    Displays options like viewing logs, hacking, and logging out.
    """

    # We define the ID for the main content container to target it with CSS
    DEFAULT_CSS = """
    #menu-container {
        align: center middle; /* Centers content horizontally and vertically */
        width: 100%;
        height: 100%;
        /* Ensures the container respects the space between Header and Footer */
        min-height: 0;
    }
    .menu-button {
        width: 80%; /* Buttons take 80% of the container width */
        max-width: 40; /* Limit maximum width for a centered terminal feel */
        margin-top: 1; /* Add some space between buttons */
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the screen structure: Header, central menu, and Footer."""
        yield Header()

        with Container(id="menu-container"):
            # The title area
            yield Static(":: ROBCO INDUSTRIES (TM) TERMINAL ::", classes="menu-title")
            yield Static("-----------------------------------", classes="menu-divider")

            # Interactive Buttons
            yield Button(
                "READ LOGS", id="logs", classes="menu-button", variant="primary"
            )
            yield Button(
                "HACK SYSTEM", id="hack", classes="menu-button", variant="primary"
            )
            yield Button("LOGOUT", id="logout", classes="menu-button", variant="error")

        yield Footer()

    # --- Controller Logic: Event Handlers ---

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handles navigation when a menu button is pressed."""
        # Get a reference to the App for state and navigation
        app = self.app

        if event.button.id == "logs":
            # PUSH the logs menu screen onto the stack
            # app.push_screen(app.SCREENS['logs_menu']) # Uncomment when logs_menu is defined
            self.app.log("Navigation: Pushing to logs_menu.")  # Placeholder log

        elif event.button.id == "hack":
            # PUSH the hacking screen onto the stack
            # app.push_screen(app.SCREENS['hacking']) # Uncomment when hacking screen is defined
            self.app.log("Navigation: Pushing to hacking screen.")  # Placeholder log

        elif event.button.id == "logout":
            # Update the App Model state
            app.logged_in_user = "guest"

            # Since we don't have a login screen, we'll just quit for now
            self.app.exit("Logged out successfully.")

        else:
            self.app.log(f"Unknown button pressed: {event.button.id}")

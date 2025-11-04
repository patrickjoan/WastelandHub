from textual.app import ComposeResult
from textual.containers import Container, Center
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static


class MainMenuScreen(Screen):
    """Main menu screen for navigation."""

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
        """Compose the main menu screen."""
        yield Header()
        
        with Container(id="menu-container"):
            with Center():
                yield Static(">> ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL <<", classes="menu-title")
            
            with Center():
                yield Static("=" * 50, classes="menu-divider")
            
            with Center():
                yield Button("LOGS", id="logs", variant="primary", classes="menu-button")
            
            with Center():
                yield Button("HACK", id="hack", variant="primary", classes="menu-button")
            
            with Center():
                yield Button("LOGOUT", id="logout", variant="error", classes="menu-button")
        
        yield Footer()

    def on_show(self) -> None:
        """Restore focus to the logs button when shown."""
        self.call_after_refresh(self._focus_logs_button)

    def on_screen_resume(self) -> None:
        """Restore focus when resuming the screen."""
        self.call_after_refresh(self._focus_logs_button)

    def _focus_logs_button(self) -> None:
        """Focus on the logs button."""
        try:
            logs_button = self.query_one("#logs", Button)
            logs_button.focus()
        except Exception:
            pass

    # --- Controller Logic: Event Handlers ---

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle navigation when a button is pressed."""
        if event.button.id == "logs":
            await self.app.push_screen("logs_menu")
        elif event.button.id == "logout":
            self.app.exit()

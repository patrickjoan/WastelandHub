from textual import on
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static

from wastelandhub.data.log_data import LogData
from wastelandhub.data.config import get_config
from wastelandhub.widgets.typewriter import Typewriter


class LogsMenuScreen(Screen):
    """Screen for displaying and selecting logs with a typewriter effect."""

    BINDINGS = [
        ("escape", "pop_screen", "Back to main menu"),
    ]

    def compose(self) -> ComposeResult:
        """Compose the screen with dynamic log buttons and a typewriter display."""
        yield Header()

        with Horizontal():
            with Vertical(id="logs-sidebar"):
                yield Static(">> AVAILABLE LOGS <<", classes="sidebar-title")
                with VerticalScroll(id="logs-container"):
                    # Generate buttons for each log key
                    for key in LogData.load_default().get_log_keys():
                        yield Button(f"OPEN {key}", id=f"open-{key}", classes="log-button")

            yield Typewriter(id="typewriter", classes="main-display")

        yield Footer()

    def on_show(self) -> None:
        """Restore focus to the first log button after the screen is shown."""
        self.call_after_refresh(self._focus_first_button)

    def on_screen_resume(self) -> None:
        """Restore focus when resuming the screen."""
        self.call_after_refresh(self._focus_first_button)

    def _focus_first_button(self) -> None:
        """Focus on the first log button if available."""
        try:
            first_button = self.query_one("#logs-container Button")
            first_button.focus()
        except Exception:
            pass

    @on(Button.Pressed)
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses to start the typewriter effect."""
        button_id = event.button.id
        if button_id and button_id.startswith("open-"):
            key = button_id[5:]  # Remove "open-" prefix
            log_data = LogData.load_default()
            if key in log_data.logs:
                try:
                    config = get_config()
                    typewriter = self.query_one("#typewriter", Typewriter)
                    typewriter.start(log_data.get_log(key), cps=config.typewriter_cps)
                except Exception as e:
                    # Add debugging to help identify issues
                    self.app.log(f"Typewriter error for key {key}: {e}")

    def action_pop_screen(self) -> None:
        """Pop the screen and stop any ongoing typewriter effect."""
        try:
            typewriter = self.query_one("#typewriter", Typewriter)
            typewriter.stop()
        except Exception:
            pass
        self.app.pop_screen()

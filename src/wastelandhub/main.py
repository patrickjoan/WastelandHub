from textual.app import App, ComposeResult
from textual.widgets import (
    ContentSwitcher,
    Footer,
    Header,
    Input,
    RichLog,
    Static,
    Tab,
    Tabs,
)


class TerminalView(RichLog):
    """Scrollback log styled like a RobCo terminal with >_ prompts."""

    def __init__(self, *, prompt: str = ">_", **kwargs) -> None:
        super().__init__(highlight=False, markup=False, auto_scroll=True, **kwargs)
        self.prompt = prompt
        self.history: list[str] = []

    def on_mount(self) -> None:  # pragma: no cover - trivial wiring
        self.border_title = "ROBCO INDUSTRIES (TM) TERMINAL"
        self.write_line("ROBCO INDUSTRIES (TM) TERMINAL")
        self.write_line("Accessing Wasteland Hub...")
        self.write_line("System Ready")

    def write_line(self, message: str) -> None:
        """Append a new line to the terminal output with the configured prompt."""

        line = f"{self.prompt} {message}"
        self.history.append(line)
        self.write(line)


class WastelandHub(App):
    """Main application class for the Wasteland Hub terminal interface.

    This class defines the UI layout and initial state for the
    RobCo Industries (TM) Terminal simulation using the Textual framework.
    Styling is handled by the external styles.tcss file.
    """

    CSS_PATH = "styles.tcss"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Tabs(
            Tab("Terminal", id="tab-terminal"),
            Tab("Diagnostics", id="tab-diagnostics"),
            id="main-tabs",
        )
        yield ContentSwitcher(
            TerminalView(id="tab-terminal"),
            Static(
                "Diagnostics console offline. Awaiting Overseer authorization.",
                id="tab-diagnostics",
                classes="panel",
            ),
            id="content",
        )
        yield Input(placeholder="> Enter command (HACK, ACCESS)", id="command")
        yield Footer()

    def _on_mount(self) -> None:
        self.title = "Wasteland Hub - RobCo Terminal"
        self.query_one(Tabs).active = "tab-terminal"
        self.set_focus(self.query_one("#command", Input))

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        command = event.value.strip()
        if not command:
            return

        terminal = self.query_one(TerminalView)
        terminal.write_line(command)

        response = self._process_command(command)
        if response:
            terminal.write_line(response)

        event.input.value = ""

    def _process_command(self, raw_command: str) -> str:
        command = raw_command.upper()
        if command == "HACK":
            return "Security protocols engaged. Unauthorized access attempt logged."
        if command == "ACCESS":
            return "Mainframe link offline. Please consult Overseer."
        return "Unknown directive. Valid options: HACK, ACCESS."

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        if event.tab is None:
            return
        self.query_one(ContentSwitcher).current = event.tab.id


if __name__ == "__main__":
    app = WastelandHub()
    app.run()

from textual.widgets import RichLog


class Typewriter(RichLog):
    """A RichLog widget that simulates a typewriter effect by gradually revealing text."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._full_text = ""
        self._current_index = 0
        self._interval = None
        self._cps = 10  # Default characters per second

    def start(self, text: str, cps: int = 10) -> None:
        """Start the typewriter effect with the given text and speed."""
        self.stop()  # Stop any existing effect
        self.clear()
        self._full_text = text
        self._current_index = 0
        self._cps = cps
        interval_seconds = 1.0 / cps
        self._interval = self.set_interval(interval_seconds, self._type_next_char)

    def stop(self) -> None:
        """Stop the typewriter effect."""
        if self._interval:
            self._interval.stop()
            self._interval = None

    def skip_to_end(self) -> None:
        """Skip to the end of the typewriter effect, displaying the full text immediately."""
        self.stop()
        self.clear()
        self.write(self._full_text)

    def _type_next_char(self) -> None:
        """Internal method to type the next character."""
        if self._current_index < len(self._full_text):
            self._current_index += 1
            # Clear and write the accumulated text up to current index
            self.clear()
            current_text = self._full_text[:self._current_index]
            self.write(current_text)
        else:
            self.stop()

    def on_unmount(self) -> None:
        """Ensure the interval is stopped when the widget is unmounted."""
        self.stop()


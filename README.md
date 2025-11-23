# WastelandHub

A retro terminal interface inspired by RobCo Industries terminals from the Fallout universe. Built with Python and [Textual](https://textual.textualize.io/), WastelandHub provides an immersive green-on-black terminal experience for browsing classified logs and system files.

## Features

- 🖥️ **Authentic RobCo Terminal UI** - Classic green phosphor CRT aesthetic with scanline effects
- 📝 **Terminal Log Viewer** - Browse and read classified log entries with a typewriter effect
- ⚡ **Reactive Interface** - Smooth navigation and keyboard-driven controls
- 🎨 **Textual-Powered** - Modern TUI framework with rich formatting and layouts
- 🔧 **Modular Architecture** - Clean separation of data, screens, and widgets

## Screenshots

```
>> ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL <<
==================================================

                      LOGS
                      HACK
                     LOGOUT
```

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

## Installation

### Clone the repository

```bash
git clone https://github.com/patrickjoan/WastelandHub.git
cd WastelandHub
```

### Install dependencies

```bash
uv sync
```

## Running the Application

```bash
uv run wastelandhub
```

### Alternative run methods

```bash
# Run via Python module
uv run python -m wastelandhub.main

# Run with Textual devtools (live reload)
uv run textual run --dev src/wastelandhub/main.py:WastelandHubApp
```

## Controls

- **Tab** - Navigate menu options
- **Enter** - Select menu item
- **Escape** - Return to previous screen (in log viewer)
- **Q / Ctrl+C** - Quit application

## Development

### Run tests

```bash
uv run pytest
```

### Lint and format code

```bash
# Check for issues
uv run ruff check .

# Auto-format code
uv run ruff format .
```

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Inspired by the iconic RobCo terminals from Bethesda's Fallout series
- Built with [Textual](https://textual.textualize.io/) by Textualize
- Managed with [uv](https://docs.astral.sh/uv/) by Astral

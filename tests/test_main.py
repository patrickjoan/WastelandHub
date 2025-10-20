import pytest

from wastelandhub.main import TerminalView, WastelandHub


@pytest.mark.asyncio
async def test_app_starts():
    app = WastelandHub()
    async with app.run_test() as pilot:
        await pilot.pause()
        assert app.title == "Wasteland Hub - RobCo Terminal"
        terminal = app.query_one("#tab-terminal", TerminalView)
    assert ">_ ROBCO INDUSTRIES (TM) TERMINAL" in terminal.history
    assert ">_ System Ready" in terminal.history

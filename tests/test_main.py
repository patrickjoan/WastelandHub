import pytest

from wastelandhub.data.log_data import LogData
from wastelandhub.main import WastelandHubApp


@pytest.mark.asyncio
async def test_app_starts_and_shows_main_menu():
    """Test that the app starts correctly and displays the main menu."""
    app = WastelandHubApp()
    async with app.run_test() as pilot:
        # Allow the app to mount and push the initial screen
        await pilot.pause()
        assert app.title == "WastelandHub - RobCo Terminal"
        # The main menu screen should be active and its container present
        menu_container = app.screen.query_one("#menu-container")
        assert menu_container is not None


@pytest.mark.asyncio
async def test_navigation_to_logs_menu():
    """Test navigation from main menu to logs menu."""
    app = WastelandHubApp()
    async with app.run_test() as pilot:
        await pilot.pause()

        # Click on the LOGS button
        await pilot.click("#logs")
        await pilot.pause()

        # Should be on logs menu screen now
        logs_container = app.screen.query_one("#logs-container")
        assert logs_container is not None


@pytest.mark.asyncio
async def test_typewriter_functionality():
    """Test that typewriter widget works in logs menu."""
    app = WastelandHubApp()
    async with app.run_test() as pilot:
        await pilot.pause()

        # Navigate to logs menu
        await pilot.click("#logs")
        await pilot.pause()

        # Check typewriter widget exists
        typewriter = app.screen.query_one("#typewriter")
        assert typewriter is not None

        # Click on a log button
        await pilot.click("#open-COMM_01")
        await pilot.pause()

        # Typewriter should have some content now
        # Note: We can't easily test the gradual typing effect in tests


@pytest.mark.asyncio
async def test_escape_key_navigation():
    """Test that Escape key returns from logs menu to main menu."""
    app = WastelandHubApp()
    async with app.run_test() as pilot:
        await pilot.pause()

        # Navigate to logs menu
        await pilot.click("#logs")
        await pilot.pause()

        # Verify we're on logs screen
        logs_container = app.screen.query_one("#logs-container")
        assert logs_container is not None

        # Press Escape to go back
        await pilot.press("escape")
        await pilot.pause()

        # Should be back on main menu
        menu_container = app.screen.query_one("#menu-container")
        assert menu_container is not None


@pytest.mark.asyncio
async def test_all_log_buttons_exist():
    """Test that all log entries have corresponding buttons."""
    app = WastelandHubApp()
    async with app.run_test() as pilot:
        await pilot.pause()

        # Navigate to logs menu
        await pilot.click("#logs")
        await pilot.pause()

        # Check that all expected log buttons exist
        log_data = LogData.load_default()
        for key in log_data.get_log_keys():
            button = app.screen.query_one(f"#open-{key}")
            assert button is not None

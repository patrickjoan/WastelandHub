import pytest

from wastelandhub.main import WastelandHubApp


@pytest.mark.asyncio
async def test_app_starts_and_shows_main_menu():
    app = WastelandHubApp()
    async with app.run_test() as pilot:
        # Allow the app to mount and push the initial screen
        await pilot.pause()
        assert app.title == "Wasteland Hub - RobCo Terminal"
        # The main menu screen should be active and its container present
        menu_container = app.screen.query_one("#menu-container")
        assert menu_container is not None

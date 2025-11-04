import pytest

from wastelandhub.app.wasteland_hub import WastelandHubApp


@pytest.mark.asyncio
async def test_app_starts_and_shows_main_menu():
    """Test that the app starts correctly and displays the main menu."""
    app = WastelandHubApp()
    async with app.run_test() as pilot:
        # Allow the app to mount and push the initial screen
        await pilot.pause()
        assert app.title == "Wasteland Hub - RobCo Terminal"
        # The main menu screen should be active and its container present
        menu_container = app.screen.query_one("#menu-container")
        assert menu_container is not None


@pytest.mark.asyncio 
async def test_navigation_to_logs_menu():
    """Test navigation from main menu to logs menu."""
    app = WastelandHubApp()
    async with app.run_test() as pilot:
        await pilot.pause()
        
        # Click on the READ LOGS button
        await pilot.click("#logs")
        await pilot.pause()
        
        # Should be on logs menu screen now
        logs_container = app.screen.query_one("#logs-container")
        assert logs_container is not None


@pytest.mark.asyncio
async def test_config_and_data_loading():
    """Test that configuration and log data are loaded properly."""
    app = WastelandHubApp()
    
    # Check that config is loaded
    assert hasattr(app, 'config')
    assert app.config.typewriter_cps == 20
    
    # Check that log data is loaded
    assert hasattr(app, 'log_data')
    assert len(app.log_data.logs) > 0
    assert "COMM_01" in app.log_data.logs

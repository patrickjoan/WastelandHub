import json
import pytest
from pathlib import Path
from tempfile import TemporaryDirectory

from wastelandhub.data.config import WastelandConfig, get_config


def test_config_defaults():
    """Test that WastelandConfig has correct default values."""
    config = WastelandConfig()
    
    assert config.typewriter_cps == 20
    assert config.terminal_difficulty == 50
    assert config.default_user == "guest"
    assert config.theme == "robco_green"
    assert config.enable_sound is False
    assert config.auto_save_logs is True


def test_config_save_and_load(tmp_path, monkeypatch):
    """Test saving and loading configuration from disk."""
    # Mock XDG config directory
    config_dir = tmp_path / "config" / "wastelandhub"
    monkeypatch.setattr("wastelandhub.data.config.xdg_config_home", lambda: tmp_path / "config")
    
    # Create and save config
    config = WastelandConfig(typewriter_cps=30, theme="amber")
    config.save()
    
    # Verify file was created
    config_file = config_dir / "config.json"
    assert config_file.exists()
    
    # Verify content
    with open(config_file) as f:
        data = json.load(f)
    assert data["typewriter_cps"] == 30
    assert data["theme"] == "amber"
    
    # Load config and verify
    loaded = WastelandConfig.load()
    assert loaded.typewriter_cps == 30
    assert loaded.theme == "amber"
    assert loaded.default_user == "guest"  # Default value preserved


def test_config_load_nonexistent():
    """Test loading config when file doesn't exist returns defaults."""
    with TemporaryDirectory() as tmpdir:
        # Point to non-existent location
        import wastelandhub.data.config as config_module
        original = config_module.xdg_config_home
        config_module.xdg_config_home = lambda: Path(tmpdir) / "nonexistent"
        
        try:
            config = WastelandConfig.load()
            assert config.typewriter_cps == 20  # Should have defaults
            assert config.theme == "robco_green"
        finally:
            config_module.xdg_config_home = original


def test_config_load_corrupted(tmp_path, monkeypatch):
    """Test loading config with corrupted JSON returns defaults."""
    config_dir = tmp_path / "config" / "wastelandhub"
    config_dir.mkdir(parents=True)
    monkeypatch.setattr("wastelandhub.data.config.xdg_config_home", lambda: tmp_path / "config")
    
    # Write corrupted JSON
    config_file = config_dir / "config.json"
    config_file.write_text("{ invalid json }")
    
    # Should return defaults without crashing
    config = WastelandConfig.load()
    assert config.typewriter_cps == 20


def test_config_cache_invalidation(tmp_path, monkeypatch):
    """Test that save() invalidates get_config() cache."""
    config_dir = tmp_path / "config" / "wastelandhub"
    monkeypatch.setattr("wastelandhub.data.config.xdg_config_home", lambda: tmp_path / "config")
    
    # Clear cache before test
    get_config.cache_clear()
    
    # First call creates default config
    config1 = get_config()
    assert config1.typewriter_cps == 20
    
    # Modify and save (should invalidate cache)
    config1.typewriter_cps = 50
    config1.save()
    
    # Next call should reload from disk with new value
    config2 = get_config()
    assert config2.typewriter_cps == 50
    assert config2 is not config1  # New instance after cache clear


def test_config_properties():
    """Test config_dir and data_dir properties."""
    config = WastelandConfig()
    
    assert isinstance(config.config_dir, Path)
    assert isinstance(config.data_dir, Path)
    assert "wastelandhub" in str(config.config_dir)
    assert "wastelandhub" in str(config.data_dir)

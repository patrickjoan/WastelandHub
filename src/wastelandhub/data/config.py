"""Configuration management for WastelandHub."""

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

try:
    from xdg import xdg_config_home, xdg_data_home
except ImportError:
    # Fallback for systems without xdg
    def xdg_config_home() -> Path:
        return Path.home() / ".config"

    def xdg_data_home() -> Path:
        return Path.home() / ".local" / "share"


@dataclass
class WastelandConfig:
    """Configuration for WastelandHub application."""
    typewriter_cps: int = 20
    terminal_difficulty: int = 50
    default_user: str = "guest"
    theme: str = "robco_green"
    enable_sound: bool = False
    auto_save_logs: bool = True

    @classmethod
    def load(cls) -> "WastelandConfig":
        """Load configuration from file."""
        config_path = xdg_config_home() / "wastelandhub" / "config.json"
        if config_path.exists():
            try:
                with open(config_path, encoding="utf-8") as f:
                    data = json.load(f)
                    return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})
            except (json.JSONDecodeError, TypeError):
                # Return default config if file is corrupted
                pass
        return cls()

    def save(self) -> None:
        """Save configuration to file."""
        config_path = xdg_config_home() / "wastelandhub" / "config.json"
        config_path.parent.mkdir(parents=True, exist_ok=True)

        with open(config_path, 'w', encoding="utf-8") as f:
            json.dump(self.__dict__, f, indent=2)

    @property
    def config_dir(self) -> Path:
        """Get the configuration directory."""
        return xdg_config_home() / "wastelandhub"

    @property
    def data_dir(self) -> Path:
        """Get the data directory."""
        return xdg_data_home() / "wastelandhub"


@lru_cache(maxsize=1)
def get_config() -> WastelandConfig:
    """Get the global configuration instance."""
    return WastelandConfig.load()

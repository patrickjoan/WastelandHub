"""Log data management for WastelandHub."""

from dataclasses import dataclass
from functools import lru_cache
from typing import Dict


@dataclass(frozen=True)
class LogData:
    """Immutable container for terminal log data.
    
    This is a singleton accessed via load_default(). The data is frozen
    to prevent accidental mutations that would break the cached singleton.
    """
    logs: Dict[str, str]

    @classmethod
    @lru_cache(maxsize=1)
    def load_default(cls) -> "LogData":
        """Load default log data with expanded content (cached singleton)."""
        return cls(logs={
            "COMM_01": (
                ">> RE: FUSION CELL STOCK\n"
                "FROM: J.C. <jcurtis@robco.net>\n"
                "TO: MaintenanceTeam <maintenance@robco.net>\n"
                "PRIORITY: URGENT\n\n"
                "Stock is red. Priority re-route from Area 3 required immediately.\n"
                "Reactor 2 showing instability. Need cells ASAP.\n"
                "- J.C."
            ),
            "DIARY_05": (
                ">> PERSONAL LOG - Day 127\n"
                "Another day spent in the simulation. I swear I saw a ghoul\n"
                "on the third floor today. Management keeps telling us it's\n"
                "all part of the 'immersive experience' but something feels\n"
                "wrong. The emergency broadcasts have been more frequent.\n"
                "Sarah thinks we're not in a simulation at all.\n"
                "I'm starting to believe her."
            ),
            "DOOR_CTRL": (
                ">> DOOR CONTROL SYSTEM v2.1.7\n"
                "SYSTEM STATUS: ONLINE\n"
                "Access Level 4 Required for override.\n"
                "Current User: GUEST (Level 1)\n\n"
                "Available Commands:\n"
                "- VIEW: Display door status\n"
                "- HELP: Show command list\n"
                "- LOGOUT: End session\n\n"
                "For emergency access, contact Security."
            ),
            "SECURITY": (
                ">> SECURITY ALERT LOG\n"
                "WARNING: Multiple failed access attempts detected.\n"
                "Unauthorized login attempts from Terminal B-7.\n"
                "User: UNKNOWN\n"
                "Time: 14:23:07\n\n"
                "Lockdown protocols may be initiated if breaches continue.\n"
                "Recommend immediate investigation."
            ),
            "MAINTENANCE": (
                ">> SYSTEM DIAGNOSTIC REPORT\n"
                "All primary systems nominal.\n"
                "Radiation levels within acceptable parameters.\n"
                "Backup power: 87% capacity\n"
                "Air filtration: Operational\n\n"
                "NOTE: Unusual power fluctuations detected in Sector C.\n"
                "Scheduled maintenance required."
            ),
            "RESEARCH": (
                ">> PROJECT PURITY - STATUS UPDATE\n"
                "CLASSIFICATION: TOP SECRET\n"
                "Progress report on water purification initiative.\n"
                "Test results show 97.3% contamination removal.\n"
                "Side effects within acceptable ranges.\n\n"
                "Recommend proceeding to Phase 3 trials.\n"
                "Subject procurement from local settlements ongoing."
            )
        })

    def get_log(self, key: str) -> str:
        """Get a specific log by key."""
        return self.logs.get(key, "Log not found.")

    def get_log_keys(self) -> list[str]:
        """Get all available log keys."""
        return list(self.logs.keys())

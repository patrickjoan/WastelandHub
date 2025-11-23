import pytest

from wastelandhub.data.log_data import LogData


def test_log_data_singleton():
    """Test that LogData.load_default() returns the same instance."""
    log_data1 = LogData.load_default()
    log_data2 = LogData.load_default()
    
    assert log_data1 is log_data2


def test_log_data_immutability():
    """Test that LogData is frozen and cannot be modified."""
    log_data = LogData.load_default()
    
    # Should not be able to reassign logs field
    with pytest.raises(Exception):  # dataclass FrozenInstanceError
        log_data.logs = {}


def test_log_data_has_required_logs():
    """Test that default log data contains expected entries."""
    log_data = LogData.load_default()
    
    required_keys = ["COMM_01", "DIARY_05", "DOOR_CTRL", "SECURITY", "MAINTENANCE", "RESEARCH"]
    for key in required_keys:
        assert key in log_data.logs
        assert len(log_data.logs[key]) > 0


def test_get_log_existing():
    """Test getting an existing log entry."""
    log_data = LogData.load_default()
    
    comm_log = log_data.get_log("COMM_01")
    assert "FUSION CELL STOCK" in comm_log
    assert len(comm_log) > 0


def test_get_log_nonexistent():
    """Test getting a non-existent log returns default message."""
    log_data = LogData.load_default()
    
    result = log_data.get_log("NONEXISTENT_KEY")
    assert result == "Log not found."


def test_get_log_keys():
    """Test get_log_keys returns all log keys."""
    log_data = LogData.load_default()
    
    keys = log_data.get_log_keys()
    assert isinstance(keys, list)
    assert len(keys) == 6
    assert "COMM_01" in keys
    assert "RESEARCH" in keys


def test_log_data_content_quality():
    """Test that log entries have proper formatting."""
    log_data = LogData.load_default()
    
    # Check COMM_01 has proper email-like structure
    comm = log_data.get_log("COMM_01")
    assert "FROM:" in comm
    assert "TO:" in comm
    assert "PRIORITY:" in comm
    
    # Check DOOR_CTRL has system info
    door = log_data.get_log("DOOR_CTRL")
    assert "SYSTEM STATUS:" in door
    assert "Access Level" in door

from src.core.safety_controller import SafetyController
from src.models.character import Character
from datetime import datetime

def test_safety_controller():
    print("\nTesting Safety Controller...")
    
    # Test initialization
    controller = SafetyController()
    assert controller.system_active == True
    print("✓ Safety controller initialization test passed")
    
    # Test emergency stop
    result = controller.emergency_stop()
    assert controller.system_active == False
    assert result["status"] == "emergency_stop_activated"
    print("✓ Emergency stop test passed")
    
    # Test character integration
    test_char = Character("test001", "basic")
    assert test_char.safety_controller.system_active == True
    
    # Test emergency shutdown
    shutdown_result = test_char.emergency_shutdown()
    assert test_char.state == "inactive"
    assert shutdown_result["status"] == "emergency_stop_activated"
    print("✓ Character emergency shutdown test passed")

if __name__ == '__main__':
    test_safety_controller()

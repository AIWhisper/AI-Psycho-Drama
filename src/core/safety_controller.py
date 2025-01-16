from enum import Enum
from typing import Dict, Optional
from datetime import datetime

class SafetyController:
    def __init__(self):
        self.active_protocols = {
            "input_validation": True,
            "response_monitoring": True,
            "interaction_limits": True,
            "emergency_stop": True
        }
        self.system_active = True
        self.violation_count = 0
        self.last_check = datetime.now()
        
    def validate_interaction(self, interaction: Dict) -> bool:
        """Validates any character interaction against safety protocols"""
        if not self.active_protocols["input_validation"]:
            return True
            
        if not self.system_active:
            return False
            
        # Basic validation checks
        if interaction.get("type") not in ["dialogue", "action", "response"]:
            self.violation_count += 1
            return False
            
        return True
        
    def emergency_stop(self) -> Dict:
        """Implements emergency stop functionality"""
        self.system_active = False
        self.active_protocols["emergency_stop"] = True
        return {
            "status": "emergency_stop_activated",
            "timestamp": datetime.now(),
            "system_state": "inactive"
        }
        
    def reset_system(self) -> bool:
        """Reset system after emergency stop"""
        if self.violation_count > 0:
            return False
        self.system_active = True
        return True
        
    def check_safety_status(self) -> Dict:
        """Returns current safety status"""
        return {
            "protocols_active": self.active_protocols,
            "violations": self.violation_count,
            "last_check": self.last_check,
            "system_active": self.system_active
        }

from typing import Dict
from enum import Enum
from datetime import datetime
from src.core.safety_controller import SafetyController
from src.core.context_tracker import ContextTracker
from src.models.mood import Mood

class SafetyLevel(Enum):
    STANDARD = "standard"
    RESTRICTED = "restricted"
    UNRESTRICTED = "unrestricted"

class Character:
    def __init__(self, char_id: str, char_type: str):
        # Basic character attributes
        self.id = char_id
        self.type = char_type
        self.state = "inactive"
        self.current_mood = Mood.NEUTRAL
        self.safety_level = SafetyLevel.STANDARD
        self.interaction_history = []
        
        # System components
        self.safety_controller = SafetyController()
        self.context_tracker = ContextTracker()
        
        # Endurance tracking
        self.interaction_count = 0
        self.session_duration = 0
        self.endurance_threshold = 100
        self.session_start_time = None

    def activate(self):
        """Activate the character and start session"""
        self.state = "active"
        self.session_start_time = datetime.now()
        return {"status": "success", "id": self.id}

    def update_mood(self, new_mood: Mood) -> Dict:
        """Update character mood with validation"""
        old_mood = self.current_mood
        self.current_mood = new_mood
        result = self.context_tracker.track_mood_change(old_mood, new_mood)
        return result

    def get_state(self) -> Dict:
        return {
            "id": self.id,
            "type": self.type,
            "state": self.state,
            "mood": self.current_mood.value,
            "safety_level": self.safety_level.value
        }

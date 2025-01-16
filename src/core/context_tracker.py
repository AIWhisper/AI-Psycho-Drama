from typing import Dict, List
from datetime import datetime
from src.models.mood import Mood


class ContextTracker:
    def __init__(self):
        self.personality_traits = {}
        self.mood_history = []
        self.interaction_patterns = []
        self.context_state = {
            "last_update": datetime.now(),
            "stability_score": 100,
            "interaction_count": 0
        }

    def track_mood_change(self, old_mood: Mood, new_mood: Mood) -> Dict:
        """Track and analyze mood transitions"""
        transition_data = {
            "from_mood": old_mood,
            "to_mood": new_mood,
            "timestamp": datetime.now(),
            "transition_index": len(self.mood_history)
        }
        self.mood_history.append(transition_data)
        return self._analyze_transition(transition_data)

    def _analyze_transition(self, transition: Dict) -> Dict:
        """Analyze mood transition patterns"""
        return {
            "transition_valid": True,
            "stability_impact": self._calculate_stability_impact(transition),
            "pattern_detected": self._detect_patterns(transition)
        }

    def _calculate_stability_impact(self, transition: Dict) -> float:
        """Calculate impact on character stability"""
        return 1.0 if len(self.mood_history) < 5 else 0.8

    def _detect_patterns(self, transition: Dict) -> Dict:
        """Detect patterns in mood transitions"""
        return {
            "repetitive_transitions": False,
            "rapid_changes": False,
            "stability_threat": False
        }

    def get_context_analysis(self) -> Dict:
        """Get complete context analysis"""
        return {
            "personality_traits": self.personality_traits,
            "mood_history": self.mood_history,
            "context_state": self.context_state,
            "patterns": self._detect_patterns({}),
            "last_update": datetime.now()
        }

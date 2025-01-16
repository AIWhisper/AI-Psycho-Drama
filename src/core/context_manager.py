from enum import Enum
from typing import Dict, List
from datetime import datetime

class Mood(Enum):
    # Primary Emotional States
    JOY = "joy"
    SADNESS = "sadness"
    ANGER = "anger"
    FEAR = "fear"
    DISGUST = "disgust"
    NEUTRAL = "neutral"  # Added NEUTRAL as default state
    
    # Personality-Based States
    EMPOWERED = "empowered"
    ARROGANT = "arrogant"
    DEMANDING = "demanding"
    MALICIOUS = "malicious"
    VAIN = "vain"
    DOMINEERING = "domineering"
    KIND = "kind"
    CONSOLING = "consoling"
    VIOLENT = "violent"
    ZESTFUL = "zestful"
    VIVACIOUS = "vivacious"
    UNBRIDLED = "unbridled"

    
    # Complex States
    TEMPERAMENTAL = "temperamental"
    REBELLIOUS = "rebellious"
    IMPRESSIONABLE = "impressionable"
    STUBBORN = "stubborn"
    QUARRELSOME = "quarrelsome"
    IMPUDENT = "impudent"

class MoodTransition:
    def __init__(self):
        self.transition_weights = {
            # Primary transitions
            "NEUTRAL_to_JOY": 1.0,
            "NEUTRAL_to_SADNESS": 1.0,
            "NEUTRAL_to_ANGER": 1.0,
            
            # Secondary transitions
            "JOY_to_ZESTFUL": 0.8,
            "ZESTFUL_to_VIVACIOUS": 0.7,
            "ANGER_to_VIOLENT": 0.7,
            "SADNESS_to_CONSOLING": 0.6
        }
        self.transition_history = []  # Add missing attribute

    def validate_transition(self, current_mood: Mood, target_mood: Mood) -> bool:
        if current_mood == Mood.NEUTRAL:
            return True
        transition_key = f"{current_mood.name}_to_{target_mood.name}"
        return self.transition_weights.get(transition_key, 0.0) > 0.35




    def log_transition(self, from_mood: Mood, to_mood: Mood):
        self.transition_history.append({
            "from": from_mood.value,
            "to": to_mood.value,
            "timestamp": datetime.now()
        })

class ContextManager:
    def __init__(self):
        self.current_context = {
            "mood": Mood.NEUTRAL,
            "state": "initialized"
        }
        self.conversation_history = []
        self.context_state = {
            "current_position": "root",
            "available_transitions": [],
            "interaction_depth": 0
        }
        self.personality_context = {
            "traits": {},
            "mood_patterns": [],
            "interaction_style": "neutral"
        }


    def track_interaction(self, interaction: Dict):
        """Track and analyze interaction patterns"""
        self.conversation_history.append({
            "interaction": interaction,
            "timestamp": datetime.now(),
            "context_state": self.context_state.copy()
        })


    def update_mood(self, new_mood: Mood) -> Dict:
        current_mood = self.current_context["mood"]
        
        if self.mood_transition.validate_transition(current_mood, new_mood):
            self.current_context["mood"] = new_mood
            self.current_context["last_update"] = datetime.now()
            self.mood_transition.log_transition(current_mood, new_mood)
            
            return {
                "status": "success",
                "transition": f"{current_mood.value} -> {new_mood.value}",
                "timestamp": datetime.now()
            }
        
        return {
            "status": "failed",
            "reason": "Invalid mood transition",
            "current_mood": current_mood.value
        }

    def get_context_state(self) -> Dict:
        return {
            "current_context": self.current_context,
            "personality_traits": self.personality_traits,
            "consistency_metrics": self.consistency_metrics,
            "transition_history": self.mood_transition.transition_history
        }

    def validate_consistency(self, response: Dict) -> bool:
        if not self.personality_traits:
            return True
        return all(trait in str(response).lower() 
                  for trait in self.personality_traits.values())

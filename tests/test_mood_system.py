import unittest
from datetime import datetime
from src.core.context_manager import ContextManager, Mood, MoodTransition

class TestMoodSystem(unittest.TestCase):
    def setUp(self):
        self.context_manager = ContextManager()
        
    def test_mood_transition(self):
        """Test basic mood transitions"""
        print("\nTesting Mood Transitions...")
        
        # Test initial state
        initial_state = self.context_manager.get_context_state()
        self.assertEqual(initial_state["current_context"]["mood"], Mood.NEUTRAL)
        
        # Test transition chain
        transitions = [
            (Mood.NEUTRAL, Mood.JOY),
            (Mood.JOY, Mood.ZESTFUL),
            (Mood.ZESTFUL, Mood.VIVACIOUS)
        ]
        
        for current, target in transitions:
            self.context_manager.current_context["mood"] = current
            result = self.context_manager.update_mood(target)
            self.assertEqual(
                result["status"], 
                "success", 
                f"Transition failed: {current.value} -> {target.value}"
            )
            print(f"✓ Transition passed: {current.value} -> {target.value}")
            
    def test_invalid_transition(self):
        """Test invalid mood transitions"""
        self.context_manager.current_context["mood"] = Mood.KIND
        result = self.context_manager.update_mood(Mood.VIOLENT)
        self.assertEqual(result["status"], "failed")
        print("✓ Invalid transition test passed")

if __name__ == '__main__':
    unittest.main(verbosity=2)

import unittest
from datetime import datetime
from src.models.character import Character, Mood

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character("test001", "basic")

    def test_mood_transition(self):
        """Test mood transition functionality"""
        # Test initial mood
        self.assertEqual(self.character.current_mood, Mood.NEUTRAL)
        
        # Test mood transition
        result = self.character.update_mood(Mood.JOY)
        self.assertTrue(result["transition_valid"])
        self.assertEqual(self.character.current_mood, Mood.JOY)

    def test_character_activation(self):
        """Test character activation"""
        result = self.character.activate()
        self.assertEqual(result["status"], "success")
        self.assertEqual(self.character.state, "active")

if __name__ == '__main__':
    unittest.main()

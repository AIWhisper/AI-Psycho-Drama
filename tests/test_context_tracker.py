import unittest
from datetime import datetime
from src.core.context_tracker import ContextTracker
from src.models.mood import Mood


class TestContextTracker(unittest.TestCase):
    def setUp(self):
        self.context_tracker = ContextTracker()

    def test_mood_tracking(self):
        """Test mood transition tracking"""
        print("\nTesting Mood Tracking...")
        result = self.context_tracker.track_mood_change(Mood.NEUTRAL, Mood.JOY)
        self.assertTrue(result["transition_valid"])
        self.assertEqual(len(self.context_tracker.mood_history), 1)
        print("✓ Mood tracking test passed")

    def test_context_analysis(self):
        """Test context analysis functionality"""
        print("\nTesting Context Analysis...")
        self.context_tracker.track_mood_change(Mood.NEUTRAL, Mood.JOY)
        analysis = self.context_tracker.get_context_analysis()
        self.assertIn("personality_traits", analysis)
        self.assertIn("mood_history", analysis)
        print("✓ Context analysis test passed")

if __name__ == '__main__':
    unittest.main(verbosity=2)

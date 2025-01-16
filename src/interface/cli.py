import cmd
import logging
from datetime import datetime
from src.models.character import Character, SafetyLevel
from src.models.mood import Mood
from src.core.context_tracker import ContextTracker

class AIPsychoDramaCLI(cmd.Cmd):
    intro = 'AI Psycho Drama Testing Environment\nType help or ? for commands\n'
    prompt = '>> '

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.character = None

    def do_help(self, arg):
        """Show available commands"""
        print("\nAvailable Commands:")
        print("  create <id> <type>  - Create a new character")
        print("  activate           - Activate current character")
        print("  status            - Show character status")
        print("  mood              - Display current mood")
        print("  transition <mood>  - Change character mood")
        print("  trait <name> <val> - Add personality trait")
        print("  history           - Show mood history")
        print("  analyze           - Display analysis")
        print("  quit              - Exit program\n")

    def do_create(self, arg):
        """Create a new character"""
        try:
            args = arg.split()
            if len(args) == 2:
                char_id, char_type = args
                self.character = Character(char_id, char_type)
                print(f"Created character: {char_id}")
            else:
                print("Usage: create <id> <type>")
        except Exception as e:
            print(f"Error: {e}")

    def do_activate(self, arg):
        """Activate current character"""
        if self.character:
            result = self.character.activate()
            print(f"Character {result['id']} activated")
        else:
            print("No character created")

    def do_mood(self, arg):
        """Display current mood state"""
        if self.character:
            mood_state = self.character.context_tracker.get_context_analysis()
            print("\nCurrent Mood State:")
            print(f"├── Stability Score: {mood_state['context_state']['stability_score']}")
            print(f"├── Interaction Count: {mood_state['context_state']['interaction_count']}")
            print(f"└── Last Update: {mood_state['last_update'].strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("No character created")

    def do_transition(self, arg):
        """Request mood transition: transition <mood>"""
        if not self.character:
            print("No character created")
            return
        try:
            new_mood = Mood[arg.upper()]
            result = self.character.context_tracker.track_mood_change(
                self.character.current_mood, new_mood
            )
            print(f"Transition Result: {result}")
        except KeyError:
            print(f"Available moods: {[m.name for m in Mood]}")

    def do_trait(self, arg):
        """Add personality trait: trait <name> <value>"""
        if not self.character:
            print("No character created")
            return
        try:
            trait_name, value = arg.split()
            self.character.context_tracker.update_personality_trait(
                trait_name, float(value)
            )
            print(f"Added trait: {trait_name} = {value}")
        except ValueError:
            print("Usage: trait <name> <value>")

    def do_history(self, arg):
        """Show mood transition history"""
        if self.character:
            history = self.character.context_tracker.mood_history
            print("\nMood Transition History:")
            for idx, entry in enumerate(history, 1):
                print(f"{idx}. {entry['from_mood'].value} → {entry['to_mood'].value}")
        else:
            print("No character created")

    def do_analyze(self, arg):
        """Display context analysis"""
        if self.character:
            analysis = self.character.context_tracker.get_context_analysis()
            print("\nContext Analysis:")
            print("├── Personality Traits:")
            for trait, value in analysis['personality_traits'].items():
                print(f"│   └── {trait}: {value}")
            print(f"├── Stability Score: {analysis['context_state']['stability_score']}")
            print(f"└── Interaction Count: {analysis['context_state']['interaction_count']}")
        else:
            print("No character created")

    def do_quit(self, arg):
        """Exit the program"""
        print("\nGoodbye!")
        return True

if __name__ == '__main__':
    try:
        AIPsychoDramaCLI().cmdloop()
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

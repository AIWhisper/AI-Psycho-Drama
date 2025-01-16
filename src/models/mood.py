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
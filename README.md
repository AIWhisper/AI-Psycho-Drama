# AI Psycho Drama Testing Environment

A controlled testing environment for AI character interactions with comprehensive safety protocols and mood management.

## Overview

- Character-based AI interaction testing
- Mood transition management
- Context-aware responses
- Safety protocol integration
- Real-time monitoring

## Core Features

- Character state management
- Mood transition validation
- Context tracking
- Safety controls
- Interactive CLI

## Project Structure

```
ai-psycho-drama/
├── src/
│   ├── models/          # Core data models
│   ├── core/            # System functionality
│   └── interface/       # User interface
├── tests/               # Test implementations
├── docs/               
└── data/               
```

## Installation

1. Clone repository
2. Set PYTHONPATH:
```bash
export PYTHONPATH=$PYTHONPATH:$PWD
```
3. Run CLI:
```bash
python3 src/interface/cli.py
```

## Usage

Available commands:
- create <id> <type> - Create character
- activate - Activate character
- mood - Display mood state
- transition <mood> - Change mood
- analyze - Show analysis
- quit - Exit program

## Safety Protocols

- Standard safety level enabled by default
- Controlled testing environment
- Monitored interactions
- Emergency shutdown capability

## Development Status

- Basic functionality implemented
- Core features operational
- Testing framework established
- Active development ongoing

## License

MIT License

## Contributing

See CONTRIBUTING.md for guidelines
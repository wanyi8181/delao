from dataclasses import dataclass


@dataclass
class GameContext:
    debug_mode: bool = False

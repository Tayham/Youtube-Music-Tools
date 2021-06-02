from dataclasses import dataclass


@dataclass
class FeedbackTokens:
    add: str = None
    remove: str = None

import re

WORDS = []


def isValid(text):
    return bool(re.search(r'\bCommand\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    
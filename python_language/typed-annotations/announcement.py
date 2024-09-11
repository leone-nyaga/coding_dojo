#!/usr/bin/python3

"""Returns language and version"""
def announcement(language: str, version: float) -> str:
    return f"{language} {version} has been released"
print(announcement("Python", 3.10))

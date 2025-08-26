#!/usr/bin/env python
import os
import sys
import random

def main():
    """Run administrative tasks or just print something random."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    # Add some random fun
    random_messages = [
        "Launching Django rocket 🚀",
        "Summoning management commands... 🔮",
        "Python says hello 🐍",
        "Random number of the day: " + str(random.randint(1, 9999)),
        "Beep boop. Running manage.py 🤖"
    ]
    print(random.choice(random_messages))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Is it installed and available on your PYTHONPATH?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
# test
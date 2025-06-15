#!/usr/bin/env python3
"""
Physics Experiment Helper - Main Application Entrypoint
CBSE Class XII Computer Science (Subject Code 083) Project

Authors: Shreshth Dhimole, Prudhvi Kasinedi, Hrishikesh Khanna
School: Narayana E-Techno School, Mumbai
Academic Year: 2024-25
"""

import sys
import argparse
from src.ui.cli import PhysicsCLI


def main():
    parser = argparse.ArgumentParser(
        description="Physics Experiment Helper - CBSE Class XII Practical Companion"
    )
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Launch the desktop Graphical User Interface (Tkinter)"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run the automated test suite"
    )

    args = parser.parse_args()

    if args.gui:
        try:
            from src.gui.app import launch_gui
            launch_gui()
        except ImportError as e:
            print(f"Error launching GUI: {e}")
            sys.exit(1)
    elif args.test:
        import unittest
        loader = unittest.TestLoader()
        suite = loader.discover("tests")
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        sys.exit(0 if result.wasSuccessful() else 1)
    else:
        # Default interactive CLI mode
        cli = PhysicsCLI()
        cli.run()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Desktop Graphical User Interface Entrypoint
Physics Experiment Helper - CBSE Class XII (083)
"""

import sys
from src.gui.app import launch_gui

if __name__ == "__main__":
    try:
        launch_gui()
    except Exception as e:
        print(f"Error launching GUI application: {e}")
        sys.exit(1)

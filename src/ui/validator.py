"""
Input Validation and Safe Prompting Utilities
CBSE Class XII Computer Science (Subject Code 083) Project
"""

from typing import Optional


class InputValidator:
    """Provides validated user input prompts with physical boundary checks."""

    @staticmethod
    def get_float(prompt: str, min_val: Optional[float] = None,
                  max_val: Optional[float] = None, default: Optional[float] = None) -> float:
        """Prompt user for a valid floating-point number within [min_val, max_val]."""
        while True:
            try:
                suffix = f" (default: {default})" if default is not None else ""
                user_str = input(f"{prompt}{suffix}: ").strip()

                if not user_str and default is not None:
                    return default

                val = float(user_str)
                if min_val is not None and val < min_val:
                    print(f"  [!] Value must be >= {min_val}. Please re-enter.")
                    continue
                if max_val is not None and val > max_val:
                    print(f"  [!] Value must be <= {max_val}. Please re-enter.")
                    continue
                return val
            except ValueError:
                print("  [!] Invalid input. Please enter a valid numerical value.")
            except (KeyboardInterrupt, EOFError):
                print("\nOperation cancelled by user.")
                raise

    @staticmethod
    def get_int(prompt: str, min_val: Optional[int] = None,
                max_val: Optional[int] = None, default: Optional[int] = None) -> int:
        """Prompt user for a valid integer within [min_val, max_val]."""
        while True:
            try:
                suffix = f" (default: {default})" if default is not None else ""
                user_str = input(f"{prompt}{suffix}: ").strip()

                if not user_str and default is not None:
                    return default

                val = int(user_str)
                if min_val is not None and val < min_val:
                    print(f"  [!] Value must be >= {min_val}. Please re-enter.")
                    continue
                if max_val is not None and val > max_val:
                    print(f"  [!] Value must be <= {max_val}. Please re-enter.")
                    continue
                return val
            except ValueError:
                print("  [!] Invalid input. Please enter a valid integer.")
            except (KeyboardInterrupt, EOFError):
                print("\nOperation cancelled by user.")
                raise

    @staticmethod
    def get_yes_no(prompt: str, default: str = "yes") -> bool:
        """Prompt user for a yes/no confirmation."""
        while True:
            try:
                user_str = input(f"{prompt} (yes/no): ").strip().lower()
                if not user_str:
                    return default.lower() in ("yes", "y")
                if user_str in ("yes", "y"):
                    return True
                if user_str in ("no", "n"):
                    return False
                print("  [!] Please answer 'yes' or 'no'.")
            except (KeyboardInterrupt, EOFError):
                print("\nOperation cancelled by user.")
                raise

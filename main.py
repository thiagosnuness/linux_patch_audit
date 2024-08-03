"""
Main Module

This module serves as the entry point for the Patch Audit application. It
initializes necessary components and executes the main functionality of the
program.
"""

from computer import Computer
from patch import Patch
from art import logo


def main() -> None:
    """Main function to execute the patch audit."""
    print(logo)
    computer = Computer()
    print(computer.get_computer_info())

    patch = Patch()
    print(patch.get_patch_info())


if __name__ == "__main__":
    main()

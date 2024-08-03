"""
Utils Module

This module provides utility functions and classes for the application,
including command execution capabilities.
"""

import subprocess
from typing import Tuple


class CommandExecutor:
    """Utility class for executing shell commands."""

    @staticmethod
    def run_command(command: str) -> Tuple[str, str]:
        """
        Run a shell command and return its output and error messages.

        Args:
            command (str): The shell command to execute.

        Returns:
            Tuple[str, str]: The standard output and standard error of
            the command.

        Raises:
            subprocess.CalledProcessError: If the command returns a
            non-zero exit status.
        """
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, universal_newlines=True
        )
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(
                process.returncode, command, stderr
            )
        return stdout.strip(), stderr.strip()

"""
Computer Module

This module defines the Computer class, which is responsible for retrieving
and managing computer information such as hostname and operating system
version.
"""

from utils import CommandExecutor


class Computer:
    """Class to retrieve and manage computer information."""

    def __init__(self) -> None:
        """
        Initialize the Computer object by fetching hostname and OS version.
        """
        self.__hostname = self.get_hostname()
        self.__version_os = self.get_version_os().strip()

    def get_hostname(self) -> str:
        """
        Retrieve the hostname of the computer.

        Returns:
            str: The hostname of the computer.
        """
        command = "hostname"
        hostname, _ = CommandExecutor.run_command(command)
        return hostname

    def get_version_os(self) -> str:
        """
        Retrieve the OS version from /etc/issue.

        Returns:
            str: The OS version or "Unknown OS Version" if it cannot be
            determined.
        """
        command = (
            'cat /etc/issue | sed "s/Welcome to S/S/g" | '
            'tr "(" "\\n" | egrep -i "(SUSE|Oracle)"'
        )
        version_os, _ = CommandExecutor.run_command(command)
        return version_os or "Unknown OS Version"

    def get_computer_info(self) -> str:
        """
        Return formatted computer information.

        Returns:
            str: A formatted string containing the hostname and OS version.
        """
        hostname_length = len(self.__hostname)
        version_os_length = len(self.__version_os)
        max_hostname_length = max(hostname_length, len("HOSTNAME"))
        max_version_os_length = max(version_os_length, len("VERSION OS"))

        header = (
            f"{'HOSTNAME'.ljust(max_hostname_length)} | "
            f"{'VERSION OS'.ljust(max_version_os_length)}"
        )
        computer_info = (
            f"{self.__hostname.ljust(max_hostname_length)} | "
            f"{self.__version_os.ljust(max_version_os_length)}"
        )

        return f"\n\n{header}\n{computer_info}\n\n"

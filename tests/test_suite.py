"""
test_suite.py

This module contains unit tests for the key components of the project.
It uses the unittest framework to test the following modules:

- Computer: Tests the functionality for retrieving system information
  such as hostname and operating system version.
- Patch: Tests the functionality related to patch management, including
  attribute assignments and deadline calculations.
- CommandExecutor: Tests the ability to run shell commands and capture
  their output.

To run these tests, use the unittest discovery mode from the project
root directory:

    python -m unittest discover -s tests

This will automatically find and execute all test cases within this
module.
"""

import unittest
from unittest.mock import patch
from computer import Computer
from patch import Patch
from utils import CommandExecutor


class TestComputer(unittest.TestCase):
    """Unit tests for the Computer class."""

    def setUp(self):
        """Set up a Computer instance for testing."""
        self.patcher = patch('utils.CommandExecutor.run_command')
        self.mock_run_command = self.patcher.start()
        self.addCleanup(self.patcher.stop)
        
        self.mock_run_command.return_value = ("MockOutput", "")
        
        self.computer = Computer()
    
    def test_hostname_not_empty(self):
        """
        Test that the hostname is not empty.

        Ensures that the get_hostname method of the Computer class
        returns a non-empty string.
        """
        self.mock_run_command.return_value = ("MockHostname", "")
        hostname = self.computer.get_hostname()
        self.assertIsNotNone(hostname)
        self.assertNotEqual(hostname, '')

    def test_os_version_not_empty(self):
        """
        Test that the OS version is not empty.

        Ensures that the get_os_version method of the Computer class
        returns a non-empty string.
        """
        self.mock_run_command.return_value = ("MockOSVersion", "")
        os_version = self.computer.get_os_version()
        self.assertIsNotNone(os_version)
        self.assertNotEqual(os_version, '')


class TestPatch(unittest.TestCase):
    """Unit tests for the Patch class."""

    def setUp(self):
        """Set up a Patch instance for testing."""
        with patch.object(Patch, 'get_patch_id', return_value='CVE-1234'), \
             patch.object(Patch, 'get_cve', return_value='CVE-1234'), \
             patch.object(Patch, 'get_date', return_value='07/01/2024'), \
             patch.object(Patch, 'get_summary',
                          return_value='Critical Security Fix'), \
             patch.object(Patch, 'calculate_deadline',
                          return_value='05/07/2024'):
            self.patch = Patch()

    def test_patch_attributes(self):
        """
        Test that the Patch attributes are correctly assigned.

        Ensures that the Patch instance has correct initial values
        for its attributes.
        """
        self.assertEqual(self.patch._Patch__patch_id, 'CVE-1234')
        self.assertEqual(self.patch._Patch__cve, 'CVE-1234')
        self.assertEqual(self.patch._Patch__date, '07/01/2024')
        self.assertEqual(self.patch._Patch__summary,
                         'Critical Security Fix')
        self.assertEqual(self.patch._Patch__deadline, '05/07/2024')

    def test_calculate_deadline(self):
        """
        Test the calculate_deadline method of the Patch class.

        Verifies that the calculate_deadline method correctly adds
        6 months to the given creation_date.
        """
        deadline = self.patch.calculate_deadline()
        self.assertEqual(deadline, "05/07/2024")


class TestCommandExecutor(unittest.TestCase):
    """Unit tests for the CommandExecutor class."""

    @patch('subprocess.Popen')
    def test_run_command(self, mock_popen):
        """
        Test running a shell command.

        Ensures that the run_command method executes a command
        and returns the expected output.
        """
        mock_process = mock_popen.return_value
        mock_process.communicate.return_value = ("Hello World", "")
        mock_process.returncode = 0

        executor = CommandExecutor()
        stdout, _ = executor.run_command("echo 'Hello World'")
        self.assertIn("Hello World", stdout)


if __name__ == '__main__':
    unittest.main()

"""
Patch Module

This module defines the Patch class, which is responsible for retrieving and
managing patch information such as patch ID, CVE, creation date, summary,
and deadline.
"""

from datetime import datetime, timedelta
from utils import CommandExecutor


class Patch:
    """Class to retrieve and manage patch information."""

    def __init__(self) -> None:
        """
        Initialize the Patch object by fetching patch details if a patch ID is
        available.
        """
        self.__patch_id = self.get_patch_id()
        self.__cve = None
        self.__date = None
        self.__summary = None
        self.__deadline = None

        if self.__patch_id:
            self.__cve = self.get_cve()
            self.__date = self.get_date()
            self.__summary = self.get_summary()
            self.__deadline = self.calculate_deadline()

    def get_patch_id(self) -> str:
        """
        Retrieve the patch ID from the system.

        Returns:
            str: The patch ID or an empty string if not found.
        """
        command = (
            "zypper list-patches --cve | grep -i security | grep -i critical "
            "| grep -i SUSE-SLE-Product | awk -F '|' '!seen[$NF]++' | "
            "sort -t '|' -k 2 -r | head -n 1 | awk -F '|' '{print $3}' | xargs"
        )
        patch_id, _ = CommandExecutor.run_command(command)
        return patch_id

    def get_cve(self) -> str:
        """
        Retrieve the CVE associated with the current patch ID.

        Returns:
            str: The CVE ID or an empty string if not found.
        """
        command = (
            "zypper list-patches --cve | grep -i security | grep -i critical "
            "| grep -i SUSE-SLE-Product | awk -F '|' '!seen[$NF]++' | "
            "sort -t '|' -k 2 -r | head -n 1 | awk -F '|' '{print $2}' | xargs"
        )
        cve, _ = CommandExecutor.run_command(command)
        return cve

    def get_date(self) -> str:
        """
        Retrieve the creation date of the patch.

        Returns:
            str: The creation date of the patch in the format 'dd/mm/yyyy'.
        """
        command = (
            f"zypper patch-info {self.__patch_id} | grep '^Created On' | "
            "cut -d: -f2 | xargs -I {{}} date -d '{{}}' +'%d/%m/%Y'"
        )
        date_cve, _ = CommandExecutor.run_command(command)
        return date_cve

    def get_summary(self) -> str:
        """
        Retrieve the summary of the patch.

        Returns:
            str: The summary of the patch.
        """
        command = (
            f"zypper patch-info {self.__patch_id} | grep '^Summary' | "
            "cut -d: -f2- | xargs"
        )
        summary, _ = CommandExecutor.run_command(command)
        return summary

    def calculate_deadline(self) -> str:
        """
        Calculate the deadline for the patch, which is 6 months from the
        creation date.

        Returns:
            str: The deadline in the format 'dd/mm/yyyy'.
        """
        date_format = "%d/%m/%Y"
        date_obj = datetime.strptime(self.__date, date_format)
        deadline_obj = date_obj + timedelta(days=6*30)
        return deadline_obj.strftime(date_format)

    def get_patch_info(self) -> str:
        """
        Return formatted patch information, including a header if a patch ID
        is available.

        Returns:
            str: A formatted string containing the patch details or a message
            if no patch is found.
        """
        if self.__patch_id:
            summary_length = len(self.__summary)
            cve_length = len(self.__cve)
            date_length = len(self.__date)
            deadline_length = len(self.__deadline)

            max_summary_length = max(summary_length, len("SUMMARY"))
            max_cve_length = max(cve_length, len("CVE"))
            max_date_length = max(date_length, len("DATE"))
            max_deadline_length = max(deadline_length, len("DEADLINE"))

            header = (
                f"{'SUMMARY'.ljust(max_summary_length)} | "
                f"{'CVE'.ljust(max_cve_length)} | "
                f"{'DATE'.ljust(max_date_length)} | "
                f"{'DEADLINE'.ljust(max_deadline_length)}"
            )

            patch_info = (
                f"{self.__summary.ljust(max_summary_length)} | "
                f"{self.__cve.ljust(max_cve_length)} | "
                f"{self.__date.ljust(max_date_length)} | "
                f"{self.__deadline.ljust(max_deadline_length)}"
            )

            return f"{header}\n{patch_info}\n\n"
        else:
            return "No patches found."

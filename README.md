````markdown
# Audit Patch

## Table of Contents

- [Introduction](#introduction)
- [Project Purpose](#project-purpose)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Examples](#examples)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Introduction

Welcome to **Audit Patch**, a tool designed to audit and verify critical security patches on Linux-based systems. This application retrieves detailed information about available security patches, helping system administrators maintain up-to-date and secure environments.

## Project Purpose

With the increasing frequency of security threats, it is essential for organizations to keep their systems updated with the latest security patches. Audit Patch aims to automate the process of identifying and monitoring critical patches, thereby enhancing the efficiency and security of system management.

## Installation

### Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Shell Access**: Required to execute system commands.
- **Administrative Permissions**: Necessary for retrieving full patch details.

### Steps

1. **Clone the Repository**

   Open your terminal and run the following command:

   ```bash
   git clone https://github.com/thiagosnuness/linux_patch_audit.git
   cd audit-patch
   ```

2. **Install Dependencies**

   This project does not require any additional dependencies beyond Python standard libraries.

## How It Works

Audit Patch retrieves information about system patches using system commands. It specifically looks for critical security patches and displays relevant details such as patch ID, CVE, creation date, summary, and application deadline. This information is useful for system administrators to quickly assess the security status of their systems.

## Usage

Run the `main.py` file to execute the application and obtain information about system patches:

```bash
python main.py
```

This command will display system information and details of available critical security patches.

## Examples

Below is a sample output of the application when executed:

```
  ____       _       _          _             _ _ _   
 |  _ \ __ _| |_ ___| |__      / \  _   _  __| (_) |_ 
 | |_) / _` | __/ __| '_ \    / _ \| | | |/ _` | | __|
 |  __/ (_| | || (__| | | |  / ___ \ |_| | (_| | | |_ 
 |_|   \__,_|\__\___|_| |_| /_/   \_\__,_|\__,_|_|\__|

HOSTNAME  | VERSION OS
myserver  | openSUSE Leap 15.3

SUMMARY                | CVE        | DATE       | DEADLINE
Critical Security Fix  | CVE-1234   | 01/07/2024 | 01/01/2025
```

## Project Structure

- **`art.py`**: Contains ASCII art used for branding and visual display in the application.

- **`computer.py`**: Defines the `Computer` class, responsible for retrieving system information such as hostname and operating system version.

- **`main.py`**: Main module that serves as the entry point for the application, coordinating the execution of the audit process.

- **`patch.py`**: Defines the `Patch` class, which retrieves and manages patch details, including ID, CVE, creation date, summary, and deadline.

- **`utils.py`**: Provides utility functions such as command execution capabilities through the `CommandExecutor` class.

## Contributing

Contributions are welcome! To contribute to the project, please follow these steps:

1. **Fork the Repository**

   Create a copy of the repository in your GitHub account.

2. **Create a Branch**

   Create a branch for your feature:

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   Commit your changes to the code:

   ```bash
   git commit -m 'Add new feature'
   ```

4. **Push to the Branch**

   Push your changes to GitHub:

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

   Open a Pull Request to merge your changes into the main branch of the project.

## Credits

- **Developer**: [Thiago Nunes](https://github.com/thiagosnuness)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
````
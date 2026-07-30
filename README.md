# Os-READER
Os Reader
# System Information Detector

A cross-platform Python script that detects the operating system and displays basic system information, including the OS version, distribution, hardware architecture, hostname, and more.

## Features

- Detects Windows, Linux, and macOS
- Displays operating system details
- Identifies Linux distributions
- Detects Windows editions
- Displays macOS version
- Shows system architecture and hostname
- Requires only Python’s standard library

## Requirements

- Python 3.7 or later
- Windows, Linux, or macOS

Check whether Python is installed:

```bash
python --version
```

On some Linux and macOS systems, use:

```bash
python3 --version
```

## Installation

Clone or download this project:

```bash
git clone https://github.com/your-username/os-detector.git
cd os-detector
```

Alternatively, download `os_detector.py` directly.

## Usage

### Windows

```cmd
python os_detector.py
```

### Linux or macOS

```bash
python3 os_detector.py
```

You can also make the script executable:

```bash
chmod +x os_detector.py
./os_detector.py
```

## Example Output

```text
==================================================
       SYSTEM INFORMATION DETECTOR
==================================================
Operating System: Linux (Linux)
Linux Distribution: Ubuntu 22.04.3 LTS
System Release:    5.15.0-86-generic
Kernel Version:    #96-Ubuntu SMP
Machine Hardware:  x86_64
Hostname:          my-computer
==================================================
```

## Creating a Windows Executable

To create a standalone Windows executable, install PyInstaller:

```cmd
pip install pyinstaller
```

Build the executable:

```cmd
pyinstaller --onefile os_detector.py
```

The executable will be created in:

```text
dist/os_detector.exe
```

Run it by double-clicking the executable or from Command Prompt:

```cmd
dist\os_detector.exe
```

## Project Structure

```text
os-detector/
├── os_detector.py
└── README.md
```

## Privacy

This script only reads local system information and displays it in the terminal. It does not send data over the network or modify system files.

## License

This project is provided for educational and personal use. You may modify and distribute it as needed.

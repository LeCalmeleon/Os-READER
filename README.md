# 🖥️ System Information Detector by LeCalmeleon, Sonny and Imniwaifiok-arch

<p align="center">
	<strong>A fast, dependency-free snapshot of the machine you are running on.</strong><br>
	<sub>One Python file. Zero installs. Useful details in seconds.</sub>
</p>

<p align="center">
	<img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white" alt="Python 3.8+">
	<img src="https://img.shields.io/badge/Dependencies-none-2ea44f" alt="No dependencies">
	<img src="https://img.shields.io/badge/Platforms-Windows%20%7C%20Linux%20%7C%20macOS-6f42c1" alt="Cross-platform">
</p>

---

## ✨ What it finds

| Category | Details |
| --- | --- |
| **Operating system** | OS name, edition/distribution, release, kernel, and architecture |
| **Hardware** | Processor model, logical CPU cores, total memory, and available memory |
| **Storage** | System-drive capacity and free space |
| **Network & identity** | Hostname, current user, and local IP address |
| **Runtime** | System uptime, Python version, and interpreter path |
| **Windows extras** | Display version, build number, and Windows installation date |

## ⚡ Quick start

No packages to install—just run the script from this folder:

```powershell
python os_detector.py
```

If Python is not on your `PATH`, use its full location:

```powershell
& "C:/Users/admin/Python311/python.exe" .\os_detector.py
```

## 🧪 Example output

```text
==================================================
			 SYSTEM INFORMATION DETECTOR
==================================================
Operating System: Windows (Windows)
Windows Edition:   Windows 10 Pro
Architecture:      64bit
Processor:         Intel64 Family 6 Model 186 Stepping 2
CPU Cores:         20 logical
Total Memory:      63.7 GiB
Available Memory:  32.2 GiB
Disk Space:        182.6 GiB free of 1.8 TiB
System Uptime:     3d 18h 24m
Python Version:    3.11.9
Windows Version:   25H2 (Build 26200)
==================================================
```

## 🔒 Privacy first

The script only **reads local system information** to display it in the terminal.

- No data is uploaded.
- No network requests are made.
- No system settings are changed.

> **Note:** The local IP is resolved from the computer hostname. If a VPN or multiple network adapters are active, it may not be the IP used for internet access. Some fields can show `Unavailable` when an operating system does not expose that information.

---

<p align="center"><sub>Built with Python's standard library.</sub></p>

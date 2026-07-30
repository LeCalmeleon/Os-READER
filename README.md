# System Information Detector

A dependency-free Python script that reports useful details about the computer it runs on. It supports Windows, Linux, and macOS, with additional Windows-specific information when available.

## Reported details

- Operating system, edition/distribution, release, and kernel version
- Hardware architecture, processor model, and logical CPU core count
- Total and available memory
- System-drive capacity and free space
- Hostname, current user, and local IP address
- System uptime
- Python version and interpreter path
- On Windows: display version, build number, and installation date

## Requirements

- Python 3
- No third-party packages

## Run

From this folder, run:

```powershell
python os_detector.py
```

If `python` is not available on your PATH, run it with the full interpreter path instead:

```powershell
& "C:/Users/admin/Python311/python.exe" .\os_detector.py
```

## Notes

- The local IP address is the address associated with the computer hostname. On systems with VPNs or multiple network adapters, it may not be the address used for internet access.
- Some operating-system details may show as `Unavailable` or `Unknown` if the OS does not provide them.
- The script reads system information only; it does not modify system settings or send information anywhere.

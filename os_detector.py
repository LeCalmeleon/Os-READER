#!/usr/bin/env python3
import platform
import sys
import subprocess
import os
import getpass
import shutil
import socket
import time


def get_memory_info():
    """Return total and available memory in bytes when the OS exposes it."""
    if platform.system() == "Windows":
        try:
            import ctypes

            class MemoryStatus(ctypes.Structure):
                _fields_ = [
                    ("length", ctypes.c_ulong),
                    ("memory_load", ctypes.c_ulong),
                    ("total_physical", ctypes.c_ulonglong),
                    ("available_physical", ctypes.c_ulonglong),
                    ("total_page_file", ctypes.c_ulonglong),
                    ("available_page_file", ctypes.c_ulonglong),
                    ("total_virtual", ctypes.c_ulonglong),
                    ("available_virtual", ctypes.c_ulonglong),
                    ("available_extended_virtual", ctypes.c_ulonglong),
                ]

            status = MemoryStatus()
            status.length = ctypes.sizeof(status)
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
                return status.total_physical, status.available_physical
        except (AttributeError, OSError):
            pass
    elif os.path.exists("/proc/meminfo"):
        try:
            values = {}
            with open("/proc/meminfo", encoding="utf-8") as memory_file:
                for line in memory_file:
                    name, value = line.split(":", 1)
                    values[name] = int(value.split()[0]) * 1024
            return values.get("MemTotal"), values.get("MemAvailable")
        except (OSError, ValueError, IndexError):
            pass
    return None, None


def format_bytes(value):
    """Format a byte count in a human-friendly binary unit."""
    if value is None:
        return "Unavailable"
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if value < 1024 or unit == "TiB":
            return f"{value:.1f} {unit}"
        value /= 1024


def get_uptime():
    """Return system uptime in seconds where available."""
    if platform.system() == "Windows":
        try:
            import ctypes
            return ctypes.windll.kernel32.GetTickCount64() / 1000
        except (AttributeError, OSError):
            return None
    if os.path.exists("/proc/uptime"):
        try:
            with open("/proc/uptime", encoding="utf-8") as uptime_file:
                return float(uptime_file.read().split()[0])
        except (OSError, ValueError, IndexError):
            pass
    return None


def format_uptime(seconds):
    if seconds is None:
        return "Unavailable"
    days, remainder = divmod(int(seconds), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{days}d {hours}h {minutes}m"

def get_os_info():
    """Detect OS and gather detailed information."""
    os_name = platform.system()
    info = {
        'system': os_name,
        'node': platform.node(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'architecture': platform.architecture()[0],
        'processor': platform.processor() or "Unknown processor",
        'cpu_cores': os.cpu_count() or "Unknown",
        'hostname': socket.gethostname(),
        'user': getpass.getuser(),
        'python_version': platform.python_version(),
        'python_executable': sys.executable,
        'uptime': get_uptime(),
    }

    total_memory, available_memory = get_memory_info()
    info['total_memory'] = total_memory
    info['available_memory'] = available_memory

    try:
        info['disk'] = shutil.disk_usage(os.path.abspath(os.sep))
    except OSError:
        info['disk'] = None

    try:
        info['ip_address'] = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        info['ip_address'] = "Unavailable"

    # Windows-specific details
    if os_name == "Windows":
        info['type'] = "Windows"
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
            info['edition'] = winreg.QueryValueEx(key, "ProductName")[0]
            info['display_version'] = winreg.QueryValueEx(key, "DisplayVersion")[0]
            info['build_number'] = winreg.QueryValueEx(key, "CurrentBuildNumber")[0]
            info['install_date'] = time.strftime(
                "%Y-%m-%d", time.localtime(winreg.QueryValueEx(key, "InstallDate")[0])
            )
            winreg.CloseKey(key)
        except (FileNotFoundError, OSError):
            info['edition'] = "Unknown Windows Edition"

    # Linux-specific details
    elif os_name == "Linux":
        info['type'] = "Linux"
        try:
            with open('/etc/os-release') as f:
                for line in f:
                    if line.startswith('PRETTY_NAME='):
                        info['distro'] = line.split('=')[1].strip().strip('"')
                        break
        except OSError:
            info['distro'] = "Unknown Linux Distribution"

    # macOS-specific details
    elif os_name == "Darwin":
        info['type'] = "macOS"
        try:
            result = subprocess.run(['sw_vers', '-productVersion'], capture_output=True, text=True)
            if result.returncode == 0:
                info['mac_version'] = result.stdout.strip()
        except OSError:
            info['mac_version'] = "Unknown macOS Version"

    return info

def main():
    os_info = get_os_info()
    print("\n" + "="*50)
    print("       SYSTEM INFORMATION DETECTOR")
    print("="*50)
    print(f"Operating System: {os_info['system']} ({os_info.get('type', 'Unknown')})")
    if 'edition' in os_info:
        print(f"Windows Edition:   {os_info['edition']}")
    if 'distro' in os_info:
        print(f"Linux Distribution: {os_info['distro']}")
    if 'mac_version' in os_info:
        print(f"macOS Version:     {os_info['mac_version']}")
    print(f"System Release:    {os_info['release']}")
    print(f"Kernel Version:    {os_info['version']}")
    print(f"Machine Hardware:  {os_info['machine']}")
    print(f"Architecture:      {os_info['architecture']}")
    print(f"Processor:         {os_info['processor']}")
    print(f"CPU Cores:         {os_info['cpu_cores']} logical")
    print(f"Total Memory:      {format_bytes(os_info['total_memory'])}")
    print(f"Available Memory:  {format_bytes(os_info['available_memory'])}")
    if os_info['disk']:
        disk = os_info['disk']
        print(f"System Drive:      {os.path.abspath(os.sep)}")
        print(f"Disk Space:        {format_bytes(disk.free)} free of {format_bytes(disk.total)}")
    print(f"Hostname:          {os_info['hostname']}")
    print(f"Current User:      {os_info['user']}")
    print(f"Local IP Address:  {os_info['ip_address']}")
    print(f"System Uptime:     {format_uptime(os_info['uptime'])}")
    print(f"Python Version:    {os_info['python_version']}")
    print(f"Python Executable: {os_info['python_executable']}")
    if 'display_version' in os_info:
        print(f"Windows Version:   {os_info['display_version']} (Build {os_info['build_number']})")
    if 'install_date' in os_info:
        print(f"Windows Installed: {os_info['install_date']}")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
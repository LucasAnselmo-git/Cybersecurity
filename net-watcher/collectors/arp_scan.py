"""
Arp-scan for net-watcher project

Scan for current active devices on my LAN
"""

import subprocess


ARP_SCAN_BIN = "/usr/sbin/arp-scan"
OUI_FILE = "/usr/share/arp-scan/ieee-oui.txt"
MAC_VENDOR_FILE = "/etc/arp-scan/mac-vendor.txt"


def get_current_devices() -> list[dict]:
    """
    Get the current active devices

    Args:
        none

    Returns:
        A list of dicts, with the device IP, MAC and Vendor
    """

    pass


if __name__ == "__main__":
    curr_devices = get_current_devices()
    print("Number of current devices", curr_devices)
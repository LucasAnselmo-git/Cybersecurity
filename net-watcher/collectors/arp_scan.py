"""
Arp-scan for net-watcher project

Scan for current active devices on my LAN
"""

import subprocess


ARP_SCAN_BIN = "/usr/sbin/arp-scan"
OUI_FILE = "/usr/share/arp-scan/ieee-oui.txt"
MAC_VENDOR_FILE = "/etc/arp-scan/mac-vendor.txt"


def get_raw_scan() -> str:
    """
    Fetches the raw arp-scan data

    Args:
        None

    Returns:
        Scan result in str format
    """

    cmd = ["arp-scan", f"--ouifile={OUI_FILE}", f"--macfile={MAC_VENDOR_FILE}", "--localnet"]
    
    scan = subprocess.run(cmd, capture_output=True, text=True)

    return scan.stdout

def get_current_devices(raw_output: str=None) -> list[dict]:
    """
    Get the current active devices

    Args:
        Raw output of a arp-scan, default it's the function scanning itself

    Returns:
        A list of dicts, with the device IP, MAC and Vendor
    """
    result = []
    if raw_output is None:
        raw_output=get_raw_scan()

    arp_scan = raw_output.splitlines()

    for line in arp_scan:
        parts = line.split("\t")

        if len(parts) == 3:
            ip, mac, vendor = parts
            dict_result = {"ip":ip, "mac":mac, "vendor":vendor}
            result.append(dict_result)


    return result



# Check if is in main
if __name__ == "__main__":
    raw_scan = get_raw_scan()
    curr_devices = get_current_devices()
    print("Number of current devices", curr_devices)
    print("Raw scan: ", raw_scan)
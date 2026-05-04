from config import devices_name_map
from collectors.arp_scan import get_current_devices
from rich.table import Table
from rich import box
from rich.console import Console


def build_arp_panel(devices):
    """
    Function to build the ARP panel view of the dashboard

    Args:
        devices (list[dict]): Raw data from ARP scan

    Returns:
        rich.table.Table: Table with columns: Device, IP
    """
    table = Table(title="Active Devices", box=box.SIMPLE_HEAVY)

    table.add_column("Device")
    table.add_column("IP")

    for row in devices:
        device_name = devices_name_map.get(row["ip"], row["ip"][8:]) # Registered name or IP

        
        table.add_row(f"[#2a6496]{device_name}[/#2a6496]", row["ip"][8:])
    
    return table

if __name__=="__main__":
    devices = get_current_devices()
    table = build_arp_panel(devices)
    Console().print(table)
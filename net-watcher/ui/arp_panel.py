from config import devices_name_map
from collectors.arp_scan import get_current_devices
from rich.table import Table
from rich import box
from rich.console import Console


def build_arp_panel(queries):
    """
    Function to build the ARP panel view of the dashboard

    Args:
        Dict of queries

    Returns:
        A table with the columns: Device, IP.
        Built from rich library
    """
    table = Table(title="Active Devices", box=box.SIMPLE_HEAVY)

    table.add_column("Device")
    table.add_column("IP")

    for row in queries:
        device_name = devices_name_map.get(row["ip"], row["ip"])
        
        table.add_row(f"[#2a6496]{device_name}[/#2a6496]", row["ip"])
    
    return table

if __name__=="__main__":
    queries = get_current_devices()
    table = build_arp_panel(queries)
    Console().print(table)
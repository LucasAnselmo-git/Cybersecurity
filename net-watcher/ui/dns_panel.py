from config import devices_name_map
from collectors.dns_queries import get_recent_queries
from rich.table import Table
from rich import box
from rich.console import Console
from datetime import datetime


ALLOWED_STATUS = {2, 3, 12, 13, 14, 17}


def build_dns_panel(queries):
    """
    Function to build the DNS panel view of the dashboard

    Args:
        Dict of queries

    Returns:
        A table with the columns: Device, Domain, Time.
        Built from rich library
    """
    table = Table(title="Recent Queries", box=box.SIMPLE_HEAVY)

    table.add_column("Device")
    table.add_column("Domain")
    table.add_column("Time")

    for row in queries:
        client = devices_name_map.get(row["client"], row["client"])
        timestamp = datetime.fromtimestamp(row["timestamp"]).strftime('%H:%M:%S')
        colour = "#2d8a4e" if row["status"] in ALLOWED_STATUS else "#c0392b"
        
        table.add_row(client, f"[{colour}]{row["domain"]}[/{colour}]", timestamp)
    
    return table


if __name__=="__main__":
    queries = get_recent_queries(20)
    table = build_dns_panel(queries)
    Console().print(table)
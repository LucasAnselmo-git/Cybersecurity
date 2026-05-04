from collectors.arp_scan import get_current_devices
from collectors.dns_queries import get_recent_queries
from ui.dns_panel import build_dns_panel, ALLOWED_STATUS
from ui.arp_panel import build_arp_panel
from rich.console import Console
from rich.layout import Layout
from datetime import datetime
from rich.panel import Panel
from rich import box



def build_dashboard(arp_data, dns_data, pihole_status):
    """
    Builds the full dashboard, with status bar, DNS and ARP panels

    Args:
        arp_data (list[dict]): ARP scan results with keys: ip, mac, vendor
        dns_data (list[dict]): DNS query results with keys: client, domain, status, timestamp
        pihole_status (bool): True if Pi-hole FTL is reachable
    Returns:
        rich.layout.Layout: Complete dashboard renderable
    """
    arp_panel = build_arp_panel(arp_data)
    dns_panel = build_dns_panel(dns_data)

    # getting statuses for status bar
    refresh_time = datetime.now().strftime('%H:%M')
    active_devices = len(arp_data)
    percentage_blocked = 100 * len([row for row in dns_data \
    if row["status"] not in ALLOWED_STATUS]) \
    / len(dns_data) if dns_data else 0

    if pihole_status:
        status_display = "[#2d8a4e]Active[/#2d8a4e]"
    else:
        status_display = "[#c0392b]Down[/#c0392b]"

    pihole_text = f"[bold]Pi-Hole:[/bold] {status_display} @ 1.147"
    stats_text = (
    f"[bold]Active:[/bold] {active_devices}    "    
    f"[bold]Blocked:[/bold] {percentage_blocked:.2f}%    "    
    f"[bold]Updated:[/bold] {refresh_time}")

    # building the layout by splitting it into four panels
    layout = Layout()
    layout.split_column(
        Layout(name="upper", size=3),
        Layout(name="lower")
    )
    layout["upper"].split_row(
        Layout(Panel(pihole_text, box=box.SIMPLE_HEAD)),
        Layout(Panel(stats_text, box=box.SIMPLE_HEAD))
    )

    layout["lower"].split_row(
        Layout(arp_panel),
        Layout(dns_panel)
    )

    return layout



if __name__=="__main__":
    dns_scan = get_recent_queries(20)
    arp_scan = get_current_devices()
    pihole_status = True

    Console().print(build_dashboard(arp_scan, dns_scan, pihole_status))
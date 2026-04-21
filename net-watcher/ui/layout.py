from collectors.arp_scan import get_current_devices
from collectors.dns_queries import get_recent_queries
from ui.dns_panel import build_dns_panel, ALLOWED_STATUS
from ui.arp_panel import build_arp_panel
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich import box



def build_dashboard(arp_data, dns_data):
    arp_panel = build_arp_panel(arp_data)
    dns_panel = build_dns_panel(dns_data)

    active_devices = len(arp_data)
    percentage_blocked = 100 * len([row for row in dns_data if row["status"] not in ALLOWED_STATUS]) / len(dns_data)
    
    pihole_text = f"[bold]Pi-Hole:[/bold] [#2d8a4e]Active[/#2d8a4e] @ 1.147"
    stats_text = f"[bold]Active:[/bold] {active_devices}    [bold]Blocked:[/bold] {percentage_blocked:.2f}%"

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

    Console().print(build_dashboard(arp_scan, dns_scan))
"""
Net-watcher: Live TUI dashboard for LAN monitoring.
Polls Pi-hole DNS queries and ARP scan data,
displays results via a rich terminal dashboard.

Usage: python3 -m netwatcher
Exit:  Ctrl+C
"""

from collectors.dns_queries import get_recent_queries
from collectors.arp_scan import get_current_devices
from collectors.errors import CollectorError
from ui.layout import build_dashboard
from rich.live import Live
import time

arp_scan = []
dns_scan = []
pihole_status = False
counter = 0

try:
    with Live(build_dashboard(arp_scan, dns_scan, pihole_status), refresh_per_second=0.5) as live:
        while True:
            if counter % 10 == 0:
                try:
                    arp_scan = get_current_devices()
                except CollectorError:
                    arp_scan = []

            try:
                dns_scan = get_recent_queries(20)
                pihole_status = True
            except CollectorError:
                dns_scan = []
                pihole_status = False
            
            live.update(build_dashboard(arp_scan, dns_scan, pihole_status))
            
            counter += 1
            time.sleep(3)
except KeyboardInterrupt:
    print("Closing dashboard...")
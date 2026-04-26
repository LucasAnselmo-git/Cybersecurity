from collectors.arp_scan import get_current_devices
from collectors.dns_queries import get_recent_queries
from ui.layout import build_dashboard
from rich.live import Live
import time

arp_scan = get_current_devices()
dns_scan = get_recent_queries(20)

counter = 0

try:
    with Live(build_dashboard(arp_scan, dns_scan), refresh_per_second=0.5) as live:
        while True:
            dns_scan = get_recent_queries(20)

            if counter % 10 == 0:
                arp_scan = get_current_devices()
            
            live.update(build_dashboard(arp_scan, dns_scan))
            
            counter += 1
            time.sleep(3)
except KeyboardInterrupt:
    print("Closing dashboard...")
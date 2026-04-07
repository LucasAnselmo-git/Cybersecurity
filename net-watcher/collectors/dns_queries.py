"""
DNS collector for net-watcher project

Reads most recent logs from queries in the Pi-Hole FTL database and returns a list of dicts.
"""

import sqlite3

FTL_DB_PACTH = "/etc/pihole/pihole-FTL.db"

def get_recent_queries(limit: int = 20) -> list[dict]:
    """
    Fetch the most recent queries.

    Args:
        limit: how many queries it returns (default is 20)
    
    Returns: 
        One list of dicts per query, with keys:
        timestamp, domain, client, status
    """

    pass

# Only run if is in main
if __name__ == "__main__":
    queries = get_recent_queries(5)
    print(queries)
"""
DNS collector for net-watcher project

Reads most recent logs from queries in the Pi-Hole FTL database and returns a list of dicts.
"""


import sqlite3
from .errors import CollectorError


FTL_DB_PATH = "/etc/pihole/pihole-FTL.db"


def get_recent_queries(limit: int = 20) -> list[dict]:
    """
    Fetch the most recent queries.

    Args:
        limit: how many queries it returns (default is 20)
    
    Returns: 
        One list of dicts per query, with keys:
        timestamp, client, domain, status
    """

    sql = """
        SELECT timestamp, client, domain, status
        FROM queries
        ORDER BY id DESC
        LIMIT ?
    """
    try:
        with sqlite3.connect(f"file:{FTL_DB_PATH}?mode=ro", uri=True) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(sql, (limit,))
            rows = cursor.fetchall()
    except sqlite3.OperationalError as e:
        raise CollectorError(f"Something went wrong with the DB: {e}") from e

    return [dict(row) for row in rows]

# Only run if is in main
if __name__ == "__main__":
    queries = get_recent_queries(5)
    print(f"Got {len(queries)} queries:\n")
    for query in queries:
        print(query)
import csv
import json
from datetime import datetime, timezone

def load_logs_from_csv(filepath):
    logs = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            # Convert timestamp
            try:
                timestamp = datetime.fromtimestamp(int(row['time']), tz=timezone.utc).isoformat()
                logs.append(json.dumps({
                    "timestamp": timestamp,
                    "pid": 1000 + (i % 5),  # Rotate between 5 clients
                    "source": row['host'],
                    "method": row['method'],
                    "url": row['url'],
                    "status": int(row['response']),
                    "size": int(row['bytes']),
                    "message": f"{row['method']} {row['url']} [{row['response']}]"
                }))
            except:
                continue
    return logs

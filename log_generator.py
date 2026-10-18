
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

# Mini-SOC: Simulated authentication events
users = ["admin", "suad", "analyst", "guest"]
ip_addresses = [
    "192.0.2.10",
    "192.0.2.20",
    "198.51.100.25",
    "203.0.113.50"
]

events = []
start_time = datetime.now() - timedelta(minutes=30)

for i in range(100):
    timestamp = start_time + timedelta(seconds=i * 10)
    user = random.choice(users)
    ip = random.choice(ip_addresses)
    status = random.choices(
        ["SUCCESS", "FAILED"],
        weights=[70, 30]
    )[0]

    events.append([timestamp.isoformat(), user, ip, status])

# Simulated brute-force activity
attack_ip = "203.0.113.99"

for i in range(15):
    timestamp = datetime.now() + timedelta(seconds=i)

    events.append([
        timestamp.isoformat(),
        "admin",
        attack_ip,
        "FAILED"
    ])

events.sort(key=lambda event: event[0])

output_file = Path(__file__).parent / "authentication_logs.csv"

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "username", "src_ip", "status"])
    writer.writerows(events)

print(f"Generated {len(events)} security events")
print(f"Saved to: {output_file}")

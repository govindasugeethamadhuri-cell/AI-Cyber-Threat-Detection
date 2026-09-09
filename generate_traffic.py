import pandas as pd
import random

data = []

protocols = ["TCP", "UDP", "ICMP"]

# NORMAL TRAFFIC
for i in range(500):
    packets = random.randint(5, 100)
    duration = random.uniform(1, 20)
    bytes_sent = random.randint(500, 10000)
    packet_rate = packets / duration

    data.append([
        f"192.168.1.{random.randint(2, 50)}",
        f"10.0.0.{random.randint(2, 20)}",
        random.choice(protocols),
        random.randint(1024, 60000),
        random.choice([80, 443, 53, 22]),
        duration,
        packets,
        bytes_sent,
        packet_rate,
        random.randint(1, 5),
        "NORMAL"
    ])


# PORT SCAN
for i in range(200):
    packets = random.randint(100, 500)
    duration = random.uniform(0.1, 3)
    bytes_sent = random.randint(1000, 5000)
    packet_rate = packets / duration

    data.append([
        f"192.168.1.{random.randint(2, 50)}",
        f"10.0.0.{random.randint(2, 20)}",
        "TCP",
        random.randint(1024, 60000),
        random.randint(1, 65535),
        duration,
        packets,
        bytes_sent,
        packet_rate,
        random.randint(20, 100),
        "PORT_SCAN"
    ])


# DOS TRAFFIC
for i in range(200):
    packets = random.randint(1000, 5000)
    duration = random.uniform(0.1, 2)
    bytes_sent = random.randint(10000, 100000)
    packet_rate = packets / duration

    data.append([
        f"192.168.1.{random.randint(2, 50)}",
        f"10.0.0.{random.randint(2, 20)}",
        "TCP",
        random.randint(1024, 60000),
        random.choice([80, 443]),
        duration,
        packets,
        bytes_sent,
        packet_rate,
        random.randint(100, 500),
        "DOS"
    ])


# BRUTE FORCE
for i in range(200):
    packets = random.randint(50, 300)
    duration = random.uniform(1, 10)
    bytes_sent = random.randint(2000, 15000)
    packet_rate = packets / duration

    data.append([
        f"192.168.1.{random.randint(2, 50)}",
        f"10.0.0.{random.randint(2, 20)}",
        "TCP",
        random.randint(1024, 60000),
        22,
        duration,
        packets,
        bytes_sent,
        packet_rate,
        random.randint(10, 50),
        "BRUTE_FORCE"
    ])


# DATA EXFILTRATION
for i in range(200):
    packets = random.randint(200, 1000)
    duration = random.uniform(10, 60)
    bytes_sent = random.randint(100000, 1000000)
    packet_rate = packets / duration

    data.append([
        f"192.168.1.{random.randint(2, 50)}",
        f"10.0.0.{random.randint(2, 20)}",
        "TCP",
        random.randint(1024, 60000),
        random.choice([80, 443]),
        duration,
        packets,
        bytes_sent,
        packet_rate,
        random.randint(5, 20),
        "DATA_EXFILTRATION"
    ])


# CREATE DATASET
columns = [
    "source_ip",
    "destination_ip",
    "protocol",
    "source_port",
    "destination_port",
    "duration",
    "packets",
    "bytes",
    "packet_rate",
    "connection_count",
    "label"
]

df = pd.DataFrame(data, columns=columns)

# SAVE DATASET
df.to_csv("data/traffic.csv", index=False)

print("Traffic dataset generated successfully!")
print(df.head())

print("\nTotal records:", len(df))
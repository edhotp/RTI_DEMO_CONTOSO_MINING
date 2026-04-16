"""
Contoso Mining — Real-Time Data Simulator
==========================================
Mengirim data simulasi hauling, stockpile, dan barge loading
ke Microsoft Fabric Eventstream via Custom App endpoint.

Cara pakai:
  1. pip install -r requirements.txt
  2. Isi CONNECTION STRING di bagian CONFIGURATION di bawah
  3. python data_generator.py
  4. Ctrl+C untuk stop
"""

import json
import random
import time
import threading
from datetime import datetime, timezone, timedelta
from azure.eventhub import EventHubProducerClient, EventData

# =============================================================================
# CONFIGURATION — Isi dengan Connection String dari Eventstream > Custom App
# =============================================================================
# Cara mendapatkan:
#   1. Buka Eventstream di Fabric Portal
#   2. Klik source "Custom App"
#   3. Klik tab "Keys"
#   4. Copy "Connection string" dan "Event hub name"

HAULING_CONN_STR = "<PASTE_HAULING_STREAM_CONNECTION_STRING>"
HAULING_EVENTHUB = "<PASTE_HAULING_STREAM_EVENTHUB_NAME>"

STOCKPILE_CONN_STR = "<PASTE_STOCKPILE_STREAM_CONNECTION_STRING>"
STOCKPILE_EVENTHUB = "<PASTE_STOCKPILE_STREAM_EVENTHUB_NAME>"

BARGE_CONN_STR = "<PASTE_BARGE_STREAM_CONNECTION_STRING>"
BARGE_EVENTHUB = "<PASTE_BARGE_STREAM_EVENTHUB_NAME>"

# =============================================================================
# MASTER DATA
# =============================================================================
TRUCKS = [
    {"truck_id": f"TRK-{str(i).zfill(3)}", "base_lat": -1.6821, "base_lon": 116.0735}
    for i in range(1, 21)  # 20 dump trucks
]

ROUTES = [
    "Pit-A1 to ROM-Stockyard",
    "Pit-A2 to ROM-Stockyard",
    "Pit-B1 to Port-A",
    "ROM-Stockyard to Port-A",
    "ROM-Stockyard to Port-B",
]

STOCKPILES = [
    {"stockpile_id": "ROM", "max_capacity_ton": 80000, "base_level": 65.0},
    {"stockpile_id": "PORT-A", "max_capacity_ton": 50000, "base_level": 45.0},
    {"stockpile_id": "PORT-B", "max_capacity_ton": 50000, "base_level": 70.0},
]

BARGES = [
    {"barge_id": "BRG-201", "target_tonnage": 8000, "jetty_id": "JETTY-1"},
    {"barge_id": "BRG-202", "target_tonnage": 7500, "jetty_id": "JETTY-2"},
    {"barge_id": "BRG-203", "target_tonnage": 10000, "jetty_id": "JETTY-1"},
]

COAL_QUALITIES = ["GAR-4200", "GAR-4700", "GAR-5000", "GAR-5500"]

# =============================================================================
# DATA GENERATORS
# =============================================================================
def generate_hauling_event(truck):
    cycle_phases = ["loading", "hauling", "queuing", "unloading", "returning", "idle"]
    statuses = ["empty", "loaded", "unloading", "idle"]
    phase = random.choice(cycle_phases)
    status = "loaded" if phase == "hauling" else random.choice(statuses)
    payload = round(random.uniform(30, 42), 1) if status == "loaded" else 0.0
    speed = round(random.uniform(15, 40), 1) if phase in ("hauling", "returning") else round(random.uniform(0, 5), 1)

    return {
        "truck_id": truck["truck_id"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "latitude": round(truck["base_lat"] + random.uniform(-0.05, 0.05), 6),
        "longitude": round(truck["base_lon"] + random.uniform(-0.05, 0.05), 6),
        "speed_kmh": speed,
        "payload_ton": payload,
        "status": status,
        "route": random.choice(ROUTES),
        "cycle_phase": phase,
    }


def generate_stockpile_event(stockpile):
    # Level bergeser perlahan (drift) agar terlihat realistis
    drift = random.uniform(-3, 3)
    stockpile["base_level"] = max(15, min(92, stockpile["base_level"] + drift))
    level = round(stockpile["base_level"], 1)
    tonnage = round(level / 100 * stockpile["max_capacity_ton"])

    # Temperature naik jika level tinggi (simulasi risiko spontaneous combustion)
    base_temp = 35 + (level / 100) * 20
    temp = round(base_temp + random.uniform(-5, 8), 1)

    return {
        "stockpile_id": stockpile["stockpile_id"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level_percentage": level,
        "estimated_tonnage": tonnage,
        "max_capacity_ton": stockpile["max_capacity_ton"],
        "coal_quality": random.choice(COAL_QUALITIES),
        "temperature_celsius": temp,
    }


def generate_barge_event(barge):
    statuses = ["waiting", "loading", "loading", "loading", "loaded", "departed"]
    status = random.choice(statuses)

    if status == "loading":
        loaded = round(random.uniform(1000, barge["target_tonnage"] * 0.9))
        rate = round(random.uniform(700, 1200))
    elif status in ("loaded", "departed"):
        loaded = barge["target_tonnage"]
        rate = 0
    else:
        loaded = 0
        rate = 0

    remaining = max(0, barge["target_tonnage"] - loaded)
    eta_hours = remaining / 900 if rate == 0 and remaining > 0 else (remaining / rate if rate > 0 else 0)
    eta = datetime.now(timezone.utc) + timedelta(hours=eta_hours)

    return {
        "barge_id": barge["barge_id"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "jetty_id": barge["jetty_id"],
        "loading_rate_tph": rate,
        "loaded_tonnage": loaded,
        "target_tonnage": barge["target_tonnage"],
        "status": status,
        "eta_completion": eta.isoformat(),
    }


# =============================================================================
# SENDER
# =============================================================================
def send_events(conn_str, eventhub_name, events):
    """Kirim batch events ke Eventstream."""
    try:
        producer = EventHubProducerClient.from_connection_string(
            conn_str, eventhub_name=eventhub_name
        )
        with producer:
            batch = producer.create_batch()
            for event in events:
                batch.add(EventData(json.dumps(event)))
            producer.send_batch(batch)
        print(f"  [OK] {len(events)} events -> {eventhub_name}")
    except Exception as e:
        print(f"  [ERR] {eventhub_name}: {e}")


# =============================================================================
# STREAM LOOPS
# =============================================================================
def stream_hauling(interval=30):
    print(f"  Hauling  : setiap {interval}s, {len(TRUCKS)} trucks")
    while True:
        events = [generate_hauling_event(t) for t in TRUCKS]
        send_events(HAULING_CONN_STR, HAULING_EVENTHUB, events)
        time.sleep(interval)


def stream_stockpile(interval=60):
    print(f"  Stockpile: setiap {interval}s, {len(STOCKPILES)} sites")
    while True:
        events = [generate_stockpile_event(s) for s in STOCKPILES]
        send_events(STOCKPILE_CONN_STR, STOCKPILE_EVENTHUB, events)
        time.sleep(interval)


def stream_barge(interval=45):
    print(f"  Barge    : setiap {interval}s, {len(BARGES)} barges")
    while True:
        events = [generate_barge_event(b) for b in BARGES]
        send_events(BARGE_CONN_STR, BARGE_EVENTHUB, events)
        time.sleep(interval)


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    print()
    print("=" * 55)
    print("  Contoso Mining - Real-Time Data Simulator")
    print("=" * 55)
    print()
    print("Streams:")

    threads = [
        threading.Thread(target=stream_hauling, daemon=True),
        threading.Thread(target=stream_stockpile, daemon=True),
        threading.Thread(target=stream_barge, daemon=True),
    ]
    for t in threads:
        t.start()

    print()
    print("Running... Tekan Ctrl+C untuk stop.")
    print("-" * 55)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped.")

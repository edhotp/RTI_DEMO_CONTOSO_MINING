# AI Prompt — Recreate Contoso Mining Fabric RTI Demo

> Satu prompt lengkap untuk meregenerasi seluruh project ini dari nol menggunakan AI coding assistant.
> Copy-paste prompt di bawah ini ke GitHub Copilot, Claude, atau ChatGPT.

---

## The Prompt

```
Kamu adalah expert Microsoft Fabric developer. Buatkan project demo lengkap bernama
"Contoso Mining — Real-Time Intelligence Demo" untuk industri coal mining di Kalimantan
Selatan, Indonesia (area tambang Adaro, Tabalong-Balangan). Project ini mendemonstrasikan
kemampuan Microsoft Fabric Real-Time Intelligence (RTI) stack secara end-to-end.

=== KONTEKS BISNIS ===

Perusahaan tambang batubara dengan operasi:
- 20 dump truck (Komatsu HD785-7 kapasitas 42 ton, CAT 777F kapasitas 40 ton)
- 5 rute hauling: Pit-A1→ROM-Stockyard, Pit-A2→ROM-Stockyard, Pit-B1→Port-A,
  ROM-Stockyard→Port-A, ROM-Stockyard→Port-B
- 3 stockpile: ROM Stockyard (80,000 ton), Port-A (50,000 ton, GAR-4200),
  Port-B (50,000 ton, GAR-5000)
- 3 tongkang: BRG-201 (8,000t), BRG-202 (7,500t), BRG-203 (10,000t)
- 2 jetty: JETTY-1 (Port-A, 2 conveyor, 1200 TPH), JETTY-2 (Port-B, 1 conveyor, 800 TPH)
- Koordinat GPS: pit area ~(-2.08, 115.43), port area ~(-2.20, 115.34)
- Target harian: 15,000 ton batubara
- Kualitas batubara: GAR-4200, GAR-4700, GAR-5000, GAR-5500

=== ARSITEKTUR FABRIC ===

```
Python Data Generator → 3 Eventstream (Custom App) → Eventhouse (KQL Database)
  → Real-Time Dashboard (10 tiles, 30s auto-refresh)
  → Fabric Activator (email/Teams alerts)
  → OneLake Shortcut → Lakehouse → Notebook (Star Schema) → Semantic Model → Power BI Report
  → Data Agent (NL2KQL/NL2SQL)
  → Operations Agent + Ontology (Fabric IQ, preview)
```

=== DELIVERABLES YANG HARUS DIBUAT ===

1. **README.md** — Project overview, architecture diagram (Mermaid), demo scenarios,
   quick start, tech stack

2. **Contoso_Mining_Fabric_RTI_Demo_Plan.md** (~1200 baris) — Dokumen perencanaan lengkap:
   - Executive summary & 6 objectives
   - Architecture diagram (Mermaid)
   - Data generator design (master data, volume estimates ~67,680 events/day)
   - 5 Demo Scenarios dengan detail:
     * Scenario 1: Real-Time Coal Hauling Monitor (20 trucks, GPS, tonnage)
     * Scenario 2: Stockpile Level Monitoring (3 stockpiles, temperature alerts)
     * Scenario 3: Barge Loading & Shipping Tracker (3 barges, progress tracking)
     * Scenario 4: Data Agent Q&A (conversation examples, NL2KQL)
     * Scenario 5: Operations Agent (Ontology-based, Fabric IQ)
   - Dashboard tile specifications (10 tiles dengan KQL queries)
   - Power BI Report design (3 pages: Hauling, Stockpile, Shipping)
   - Step-by-step setup guide

3. **Tutorial_Implementation_Guide.md** (~680 baris, Bahasa Indonesia) — Tutorial langkah
   demi langkah 13 steps, ~60-90 menit:
   - Step 1: Create Workspace "Contoso-Mining-RTI"
   - Step 2: Create Eventhouse "ContosoMiningEH" + 3 KQL tables
   - Step 3: Create 3 Eventstreams dengan Custom App source
   - Step 4: Run Python data generator
   - Step 5: Verify data di KQL Database
   - Step 6: Create Real-Time Dashboard "Mining Operations Live" (8 tiles)
     * Termasuk tips konfigurasi Map visual (lat/lon binding bisa tertukar!)
   - Step 7: Create Fabric Activator alerts (2 metode: dari Dashboard & Eventstream)
   - Step 8: Create Lakehouse + OneLake Shortcuts (6 sub-steps 8a-8f):
     * 8a: Enable OneLake Availability di Eventhouse
     * 8b: WAJIB percepat mirroring latency (TargetLatencyInMinutes=5)
     * 8c: Verifikasi mirroring via .show database <DB> operations mirroring-statistics
     * 8d: Create Lakehouse "ContosoMiningLH"
     * 8e: Create shortcut via "New table shortcut" (BUKAN "New shortcut")
     * 8f: Verifikasi shortcut (SQL + Spark)
     * Troubleshooting tabel greyed out saat membuat shortcut
   - Step 9: Run Notebook Star Schema
   - Step 10: Create Semantic Model (8 relationships + 15 DAX measures)
   - Step 11: Create Power BI Report (3 halaman)
   - Step 12: Setup Data Agent
   - Step 13: Setup Fabric IQ / Operations Agent (preview, F2+)
   - Troubleshooting table + Final checklist

4. **scripts/create_eventhouse_tables.kql** — KQL script:
   - .create table HaulingEvents (truck_id:string, timestamp:datetime, latitude:real,
     longitude:real, speed_kmh:real, payload_ton:real, status:string, route:string,
     cycle_phase:string)
   - .create table StockpileEvents (stockpile_id:string, timestamp:datetime,
     level_percentage:real, estimated_tonnage:real, max_capacity_ton:real,
     coal_quality:string, temperature_celsius:real)
   - .create table BargeLoadingEvents (barge_id:string, timestamp:datetime, jetty_id:string,
     loading_rate_tph:real, loaded_tonnage:real, target_tonnage:real, status:string,
     eta_completion:datetime)
   - Enable streaming ingestion + 90-day retention policy

5. **scripts/data_generator.py** (~192 baris) — Python real-time simulator:
   - Dependency: azure-eventhub>=5.11.0
   - 3 Eventstream connections (Connection string + EventHub name placeholders)
   - Master data: 20 trucks dengan GPS coords Adaro area, 5 routes, 3 stockpiles,
     3 barges, 4 coal qualities
   - generate_hauling_event(): phase-status map (loading/hauling/queuing/unloading/
     unloaded/returning/idle), GPS jitter per route, speed by phase
   - generate_stockpile_event(): level drift ±3%, temp correlated with level,
     spontaneous combustion simulation (base_temp = 35 + level/100 * 20)
   - generate_barge_event(): status-dependent tonnage/rate, ETA calculation
   - send_events(): EventHubProducerClient batch sender
   - 3 threaded daemon loops: hauling/10s, stockpile/20s, barge/15s
   - Connection string placeholders (BUKAN hardcoded credentials)

6. **scripts/dashboard_queries.kql** — 10 KQL queries untuk Real-Time Dashboard:
   - Tile 1: Total Tonnage Today (scorecard, status="unloaded", ago(1d))
   - Tile 2: Active Trucks count (scorecard, status != "idle")
   - Tile 3: Avg Speed loaded trucks (scorecard)
   - Tile 4: Truck Map (Map visual, alias "lat"/"lon", ago(1h))
     * PENTING: tambahkan komentar bahwa lat/lon harus di-bind dengan benar di visual
   - Tile 5: Hauling Trend (time chart, bin 1 menit, ago(1h), payload_ton > 0)
   - Tile 6: Stockpile Levels (bar chart)
   - Tile 7: Barge Loading Status (table with progress %)
   - Tile 8: Top 10 Trucks by Tonnage (bar chart)
   - Tile 9: Stockpile Temperature with status emoji (table)
   - Tile 10: Recent Events Feed (union 3 streams, top 20)

7. **scripts/create_star_schema.py** (~167 baris) — PySpark untuk Fabric Notebook:
   - 6 Dimension tables:
     * DimTruck (20 rows, truck_id/name/type/max_payload/operator/commissioning_date)
     * DimRoute (5 rows, route_id/name/origin/destination/distance_km/category)
     * DimStockpile (3 rows, stockpile_id/name/location/max_capacity/quality_spec)
     * DimBarge (3 rows, barge_id/name/owner/max_capacity/vessel_type)
     * DimJetty (2 rows, jetty_id/name/location/conveyor_count/max_loading_rate_tph)
     * DimDate (730 rows, 2025-2026, date_key yyyyMMdd, year/month/day/month_name/
       week_of_year/day_name/shift_number)
   - 3 Fact tables (transform dari Eventhouse shortcut):
     * FactHauling: + date_key + cycle_time_minutes (simulated 35-55 min for unloaded)
     * FactStockpile: + date_key
     * FactBargeLoading: + date_key
   - Semua saveAsTable("...") format delta, mode overwrite

8. **scripts/dax_measures.dax** — 15 DAX measures:
   - Hauling (8): Total Tonnage, Total Trips, Avg Payload Per Trip, Avg Cycle Time,
     Tonnage vs Target % (target 15000), Active Trucks, Idle Trucks, Truck Utilization %
   - Stockpile (3): Stockpile Utilization %, Avg Temperature, Critical Stockpiles (<30%)
   - Barge (5): Loading Efficiency %, Avg Loading Rate TPH, Barges Completed,
     Total Shipped Tonnage, Avg Barge Wait Time (hrs)

9. **scripts/sample_queries.kql** — KQL queries untuk verifikasi dan eksplorasi:
   - Verification: count per table, top 5 recent per table
   - Hauling: tonnage per truck, idle >30min, avg speed per route, cycle phase distribution
   - Stockpile: current levels, critical <30%, hourly trend, high temp >50°C
   - Barge: current status + progress %, total shipped today, avg rate per jetty

10. **scripts/data_catalog.md** — Data catalog untuk Power BI Copilot:
    - Setiap tabel: description + synonyms (bilingual Indonesia + English)
    - Setiap kolom: type, description, synonyms
    - Status value reference (valid values + deskripsi) untuk FactHauling dan FactBargeLoading
    - DAX measures: description + synonyms
    - Star schema relationships diagram

11. **scripts/requirements.txt** — Satu baris: azure-eventhub>=5.11.0

12. **.gitignore** — Python (__pycache__, *.py[cod], .env, venv), IDE (.vscode, .idea),
    OS (Thumbs.db, .DS_Store), sensitive (event_stream_credential.txt, ITM_Coal_Business*)

=== ATURAN PENTING ===

- Semua ID harus konsisten antar file (truck_id, route names, stockpile_id, barge_id,
  jetty_id harus PERSIS SAMA di data_generator.py, create_star_schema.py, dan dax_measures.dax)
- Koordinat GPS harus di area Tabalong-Balangan, Kalimantan Selatan
  (latitude: -2.06 s/d -2.22, longitude: 115.32 s/d 115.46)
- Tutorial ditulis dalam Bahasa Indonesia
- Demo Plan ditulis dalam Bahasa Indonesia dengan istilah teknis dalam Bahasa Inggris
- Data catalog harus bilingual (Indonesia + English synonyms)
- Connection string di data_generator.py harus berupa PLACEHOLDER, bukan credentials asli
- Semua KQL queries harus bisa berjalan tanpa error di Fabric Eventhouse
- DAX measures harus mereferensikan kolom yang benar-benar ada di Fact/Dim tables
- Star schema: semua relationship Many-to-One, Single direction
- Map visual query harus pakai alias "lat" dan "lon" (bukan "latitude"/"longitude")
  untuk menghindari salah binding di dashboard
- Hauling trend query harus pakai bin 1 menit (bukan 1 jam) agar terlihat bergerak saat demo
- Mirroring latency command yang benar: .alter-merge table <T> policy mirroring
  dataformat=parquet with (IsEnabled=true, TargetLatencyInMinutes=5)
- Cek mirroring status yang benar: .show database <DB> operations mirroring-statistics
  (BUKAN .show table <T> mirroring operations — syntax ini tidak ada)
- Lakehouse shortcut harus pakai "New table shortcut" (bukan "New shortcut")

=== FORMAT OUTPUT ===

Buat setiap file sebagai code block terpisah dengan path lengkap sebagai header.
Pastikan semua file lengkap, tidak ada bagian yang di-skip atau disingkat.
```

---

> **Catatan:** Prompt ini menghasilkan ~12 file. Untuk hasil optimal, gunakan model dengan context window besar (Claude Opus/Sonnet, GPT-4o, atau Gemini 2.5 Pro). Jika output terpotong, minta lanjutkan file yang belum selesai.

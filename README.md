# ⛏️ Contoso Mining — Fabric Real-Time Intelligence Demo

Demo end-to-end **Microsoft Fabric Real-Time Intelligence** untuk operasi tambang batubara. Repo ini berisi rencana demo lengkap, tutorial implementasi, dan semua script yang siap dijalankan — dari data simulator hingga AI-powered Operations Agent.

## Overview

Contoso Mining mengoperasikan armada dump truck, stockpile batubara, dan tongkang pengiriman. Repo ini menunjukkan bagaimana **Microsoft Fabric** mengubah operasi tambang dari monitoring manual (radio & WhatsApp) menjadi platform data real-time terintegrasi:

```
Data Generator (Python) → Eventstream → Eventhouse (KQL) → Real-Time Dashboard
                                              │
                                              ├── Data Activator (Alert otomatis)
                                              ├── Lakehouse → Notebook → Semantic Model → Power BI
                                              ├── Data Agent (Tanya jawab bahasa natural)
                                              └── Operations Agent (Rekomendasi AI proaktif)
```

**5 skenario demo:**
1. 🚛 **Real-Time Coal Hauling Monitor** — tracking 20 truck, tonase, cycle time
2. 📦 **Stockpile Level Monitoring** — alert otomatis saat level kritis atau suhu tinggi
3. 🚢 **Barge Loading & Shipping Tracker** — progress loading dan ETA
4. 🤖 **Data Agent Q&A** — tanya data pakai bahasa natural (NL2KQL/NL2SQL)
5. 🧠 **Operations Agent** — AI otonom yang monitor dan rekomendasikan aksi via Teams

## Dokumentasi

| File | Deskripsi |
|------|-----------|
| [**Contoso_Mining_Fabric_RTI_Demo_Plan.md**](Contoso_Mining_Fabric_RTI_Demo_Plan.md) | Rencana demo lengkap: arsitektur, 5 skenario, data schema, dashboard design, demo script 20 menit, business impact |
| [**Tutorial_Implementation_Guide.md**](Tutorial_Implementation_Guide.md) | Tutorial step-by-step (13 langkah) dalam Bahasa Indonesia — dari buat workspace sampai deploy Operations Agent |

## Scripts

Semua script siap dijalankan — tinggal ikuti urutan di [Tutorial](Tutorial_Implementation_Guide.md).

| File | Bahasa | Fungsi |
|------|--------|--------|
| [**data_generator.py**](scripts/data_generator.py) | Python | Simulator 3 data stream (hauling, stockpile, barge) → Eventstream via `azure-eventhub` SDK |
| [**requirements.txt**](scripts/requirements.txt) | pip | Dependency: `azure-eventhub>=5.11.0` |
| [**create_eventhouse_tables.kql**](scripts/create_eventhouse_tables.kql) | KQL | Buat 3 tabel di Eventhouse + streaming ingestion policy + 90-day retention |
| [**create_star_schema.py**](scripts/create_star_schema.py) | PySpark | Buat star schema (6 Dim + 3 Fact tables) — jalankan di Fabric Notebook |
| [**dashboard_queries.kql**](scripts/dashboard_queries.kql) | KQL | 10 query untuk tile Real-Time Dashboard |
| [**sample_queries.kql**](scripts/sample_queries.kql) | KQL | Query verifikasi data dan eksplorasi |
| [**dax_measures.dax**](scripts/dax_measures.dax) | DAX | 15 measures untuk Semantic Model (Hauling, Stockpile, Barge) |

## Quick Start

```bash
# 1. Clone repo
git clone https://github.com/edhotp/RTI_DEMO_CONTOSO_MINING.git
cd RTI_DEMO_CONTOSO_MINING

# 2. Install Python dependency
pip install -r scripts/requirements.txt

# 3. Ikuti tutorial step-by-step
# → Buka Tutorial_Implementation_Guide.md
```

> **Prerequisites:** Microsoft Fabric account dengan kapasitas aktif (Trial F64 atau Paid), Python 3.8+

## Tech Stack

| Teknologi | Komponen | Peran |
|-----------|----------|-------|
| **Fabric RTI** | Eventstream, Eventhouse, Real-Time Dashboard, Data Activator | Ingesti, simpan, visualisasi, alert real-time |
| **Fabric Analytics** | Lakehouse, Notebook, Semantic Model, Power BI | Historical analytics & star schema |
| **Fabric AI** | Data Agent, Fabric IQ Ontology, Operations Agent | NL Q&A & autonomous operations |
| **Python** | `azure-eventhub` SDK (AMQP protocol) | Data simulator |
| **KQL** | Kusto Query Language | Real-time queries |
| **DAX** | Data Analysis Expressions | Business metrics |
| **PySpark** | Apache Spark | Data transformation |

## Fabric Features Digunakan

- **Eventstream** — streaming data ingestion (Custom App endpoint, Event Hub compatible)
- **Eventhouse** — KQL Database untuk time-series data
- **Real-Time Dashboard** — live visualisasi dengan auto-refresh 30s
- **Data Activator / Reflex** — alert rule-based (email + Teams)
- **Lakehouse** — Delta tables via Shortcut dari Eventhouse
- **Notebook** — PySpark transformation ke star schema
- **Semantic Model** — DirectLake mode + 15 DAX measures
- **Power BI Report** — 3 halaman analisis historis
- **Data Agent** *(GA)* — conversational Q&A, NL2KQL/NL2SQL/NL2DAX
- **Fabric IQ + Operations Agent** *(Preview)* — ontology-driven, autonomous recommendations via Teams

## License

Internal use — Demo purposes only.

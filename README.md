# Contoso Mining — Fabric Real-Time Intelligence Demo

End-to-end demo Microsoft Fabric Real-Time Intelligence untuk operasi tambang batubara (Contoso Mining).

## Struktur Repo

```
├── Contoso_Mining_Fabric_RTI_Demo_Plan.md   # Full demo plan (5 scenarios + AI)
├── Tutorial_Implementation_Guide.md          # Step-by-step tutorial (Bahasa Indonesia)
├── ITM_Coal_Business_Overview.md             # ITM Coal business overview (ID)
├── ITM_Coal_Business_Overview_en.md          # ITM Coal business overview (EN)
├── ITM_Coal_Business.png                     # Original architecture image
└── scripts/
    ├── data_generator.py                     # Python simulator → Eventstream
    ├── create_eventhouse_tables.kql          # KQL table creation scripts
    ├── create_star_schema.py                 # PySpark star schema (Notebook)
    ├── dashboard_queries.kql                 # Real-Time Dashboard KQL queries
    ├── sample_queries.kql                    # Verification & exploration queries
    ├── dax_measures.dax                      # DAX measures for Semantic Model
    └── requirements.txt                      # Python dependencies
```

## Quick Start

1. Baca `Tutorial_Implementation_Guide.md` untuk panduan step-by-step
2. Siapkan Fabric workspace dengan kapasitas aktif
3. Jalankan scripts sesuai urutan di tutorial

## Tech Stack

- **Microsoft Fabric**: Eventstream, Eventhouse, Real-Time Dashboard, Data Activator, Lakehouse, Notebook, Semantic Model, Power BI, Data Agent, Fabric IQ
- **Python**: `azure-eventhub` SDK (AMQP protocol)
- **KQL**: Kusto Query Language untuk real-time analytics
- **DAX**: Data Analysis Expressions untuk semantic model
- **PySpark**: Star schema transformation

## License

Internal use — Demo purposes only.

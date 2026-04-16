# ITM Coal Business – Core Value Applications and Data Landscape

## Overview

Dokumen ini menjelaskan arsitektur aplikasi dan lanskap data bisnis batubara **ITM (Indo Tambangraya Megah)**, yang mencakup seluruh **Mining Value Chain** — alur batubara dari sumber daya (resource) hingga ke pelanggan (customer), termasuk rantai pasok (supply chain) dan optimalisasi.

Arsitektur ini terbagi menjadi **4 lapisan utama**:

1. **Digital Mine (E2E Value Chain)** — Rantai nilai end-to-end pertambangan
2. **ITM Core Business Application Landscape** — Aplikasi inti bisnis
3. **Enabler Application** — Aplikasi pendukung operasional
4. **Data Management Platform** — Platform pengelolaan data terpadu

---

## 1. Digital Mine (E2E Value Chain)

Lapisan ini menggambarkan alur operasional tambang secara digital dari hulu ke hilir:

### Diagram: Mining Value Chain (E2E Flow)

```mermaid
flowchart LR
    subgraph Exploration["🔍 Exploration & Geo Model"]
        A1[Survei Geologi]
        A2[Pemodelan Cadangan]
    end

    subgraph Planning["📋 Mine Planning"]
        B1[Perencanaan Pit]
        B2[Perencanaan Produksi]
    end

    subgraph Operations["⛏️ Mine Operations"]
        C1[Drill & Blast]
        C2[OB Load & Haul]
        C3[Coal Load & Winning]
        C4[ROM Stockyard]
        C5[Disposal]
    end

    subgraph Hauling["🚛 Hauling"]
        D1[Coal Hauling]
    end

    subgraph Stockyards["🏗️ Stockyards"]
        E1[Crushing]
        E2[FC/Port Stockpile]
    end

    subgraph Barging["🚢 Barging & Shipping"]
        F1[Barge Loading]
        F2[Reclaimer & Ship Loader]
    end

    subgraph Customer["👤 Customer"]
        G1[Marketing]
        G2[Trading]
    end

    Exploration --> Planning --> Operations --> Hauling --> Stockyards --> Barging --> Customer
```

| Tahap | Deskripsi | Aktivitas Utama |
|-------|-----------|-----------------|
| **Exploration and Geo Model** | Eksplorasi dan pemodelan geologi | Survei, pemodelan cadangan |
| **Mine Planning** | Perencanaan tambang | Perencanaan produksi dan pit |
| **Mine Operations (OB & Coal)** | Operasi penambangan overburden & batubara | Drill & Blast, OB Load & Haul, Coal Load & Winning, ROM Stockyard, Disposal |
| **Hauling** | Pengangkutan batubara | Coal Hauling dari pit ke stockyard/port |
| **Stockyards** | Pengelolaan stockpile | Crushing, FC/Port Stockpile |
| **Barging & Shipping** | Pengapalan dan tongkang | Barge Loading (incl. 3rd party), Reclaimer & Ship Loader |
| **Customer** | Pemasaran dan perdagangan | Marketing, Trading |

### Diagram: Alur Operasi Penambangan Detail

```mermaid
flowchart TD
    subgraph MineOps["Mine Operations (OB & Coal)"]
        direction TB
        DB[Drill & Blast] --> OB[OB Load & Haul]
        DB --> CL[Coal Load & Winning]
        OB --> DISP[Disposal]
        CL --> ROM[ROM Stockyard]
    end

    ROM --> HAUL[Coal Hauling]
    HAUL --> CRUSH[Crushing]
    CRUSH --> STOCK[FC/Port Stockpile]
    STOCK --> BARGE[Barge Loading\nincl. 3rd Party]
    STOCK --> RECLAIM[Reclaimer &\nShip Loader]
    BARGE --> MKT[Marketing & Trading]
    RECLAIM --> MKT
```

---

## 2. Sistem Pemerintah / Regulasi (ESDM / Government)

Integrasi dengan sistem pemerintah untuk kepatuhan regulasi:

| Sistem | Fungsi |
|--------|--------|
| **RKAB Online** | Rencana Kerja dan Anggaran Biaya — pelaporan rencana kerja tambang ke ESDM |
| **MOMS / Minerba Online** | Mining Operations Management System — pelaporan produksi dan operasi ke Ditjen Minerba |
| **E-PNBP** | Penerimaan Negara Bukan Pajak elektronik — pembayaran royalti dan iuran |
| **MVP** | Sistem verifikasi dan validasi pemerintah |

### Diagram: Integrasi Sistem Pemerintah

```mermaid
flowchart LR
    subgraph GOV["ESDM / Government Systems"]
        direction LR
        RKAB[RKAB Online] --> MOMS[MOMS / Minerba Online]
        MOMS --> EPNBP[E-PNBP]
        EPNBP --> MVP[MVP]
    end

    subgraph ITM["ITM Operations"]
        PLAN[Mine Planning] -.->|Rencana Kerja| RKAB
        OPS[Mine Operations] -.->|Laporan Produksi| MOMS
        FIN[Finance] -.->|Royalti & Iuran| EPNBP
        SHIP[Shipping] -.->|Verifikasi| MVP
    end
```

---

## 3. ITM Core Business Application Landscape

### 3.1 Aplikasi Geospasial & Perencanaan

| Aplikasi | Fungsi |
|----------|--------|
| **Arc GIS** | Sistem informasi geografis untuk pemetaan dan analisis spasial |
| **Minex** | Software perencanaan tambang dan pemodelan geologi |
| **Mine Scape** | Software pemodelan tambang dan perencanaan pit |

### 3.2 Mine 2 Port (M2P Super Apps)

Platform super-app yang mengintegrasikan operasi dari tambang hingga pelabuhan, mencakup:

#### Diagram: Ekosistem M2P Super Apps

```mermaid
flowchart TB
    subgraph M2P["Mine 2 Port - M2P Super Apps"]
        direction TB
        MM["Mine Market\n(Operation, Logistic,\nInvoice to Customer)"]

        subgraph Tracking["Monitoring & Tracking"]
            TS[Truck Scale]
            CHT[Coal Haul Tracking]
            SCADA_APP[SCADA]
        end

        subgraph Shipping["Shipping & Operations"]
            SHIPPO_APP[SHIPPO]
            COAPPS[Coapps]
            SOS_APP[SOS]
        end
    end

    MINE["⛏️ Mine Site"] --> TS
    TS --> CHT
    CHT --> SCADA_APP
    SCADA_APP --> SHIPPO_APP
    SHIPPO_APP --> PORT["🚢 Port"]
    MM --> |End-to-End| PORT
```

| Aplikasi | Fungsi |
|----------|--------|
| **Mine Market** | Operasi, logistik, hingga invoice ke customer — sistem end-to-end untuk manajemen penjualan dan distribusi batubara |
| **Truck Scale** | Sistem penimbangan truk untuk pencatatan tonase |
| **Coal Haul Tracking** | Pelacakan pengangkutan batubara secara real-time |
| **SCADA** | Supervisory Control and Data Acquisition — monitoring dan kontrol operasi |
| **SHIPPO** | Sistem manajemen pengapalan (shipping operations) |
| **Coapps** | Aplikasi koordinasi operasional |
| **SOS** | Sistem operasi pendukung |

### 3.3 Aplikasi Kepatuhan & Optimasi

| Aplikasi | Fungsi |
|----------|--------|
| **PLIS** | Sistem informasi perizinan dan lisensi |
| **Obligation & Compliance** | Manajemen kewajiban dan kepatuhan regulasi |
| **Mercy** | Aplikasi pendukung operasional |
| **MOCA** | Monitoring and Control Application |
| **STSC Optimization (SSO)** | Optimalisasi rantai pasok (Supply Chain Optimization) |
| **CoTrap** | Coal Transportation Planning — perencanaan transportasi batubara |
| **Squba** | Sistem pendukung operasi barging |

### Diagram: Core Application Integration Map

```mermaid
flowchart TB
    subgraph GEO["Geospasial & Planning"]
        ARC[Arc GIS]
        MINEX[Minex]
        MS[Mine Scape]
    end

    subgraph M2P["M2P Super Apps"]
        MM[Mine Market]
        CHT[Coal Haul Tracking]
        SCADA_D[SCADA]
        SHIPPO_D[SHIPPO]
    end

    subgraph COMPLIANCE["Compliance & Optimization"]
        PLIS_D[PLIS]
        OC[Obligation & Compliance]
        SSO[STSC Optimization]
        CT[CoTrap]
    end

    subgraph ERP["ERP & Asset"]
        ORA["Oracle\n(Procurement, Accounting, Finance)"]
        MAX["Maximo\n(Asset Management)"]
    end

    GEO -->|Planning Data| M2P
    M2P -->|Operational Data| ERP
    M2P -->|Compliance Data| COMPLIANCE
    COMPLIANCE -->|Financial Impact| ERP
    MAX -->|Maintenance Cost| ORA
    SSO -->|Optimization| M2P
```

### 3.4 Sistem ERP & Asset Management

| Aplikasi | Fungsi |
|----------|--------|
| **Oracle** | Sistem ERP untuk **Procurement, Accounting, dan Finance** — backbone keuangan dan pengadaan |
| **Maximo** | Enterprise Asset Management — manajemen aset dan pemeliharaan peralatan tambang |

### 3.5 Sistem Operasi Pendukung

| Aplikasi | Fungsi |
|----------|--------|
| **ROMA** | Sistem manajemen operasional |
| **MMS** | Maintenance Management System |
| **SLeZ** | Sistem pendukung operasional |

---

## 4. Enabler Application

Aplikasi pendukung yang menopang fungsi-fungsi korporat:

### Diagram: Enabler Application Ecosystem

```mermaid
flowchart TB
    subgraph ENABLER["Enabler Applications"]
        direction LR
        subgraph HR["👥 HR"]
            SF[Sunfish Workplace]
            EL[eLeave]
            KPI[KPI Online]
            CA[Competency Assessment]
            SA[Smart Attendance]
        end

        subgraph HSEC["🛡️ HSEC"]
            GS[GoSafe]
            SCH[Siaga Carmat Hemat]
            IR[Incident Report]
            SIM[SIMPER]
            EC[eCommissioning]
        end

        subgraph FIN["💰 Finance"]
            TR[TREES]
            IT[Intax]
            BP[BPS]
            HO[HOI]
        end

        subgraph GA["🏢 GA"]
            GAC[GA Center]
            ES[eStationary]
            ETA[e-TA]
            HD[Hot Desk]
        end

        subgraph LEGAL["⚖️ CorSec & Legal"]
            EN[eNumbering]
            TC[Transparency Center]
            IC[ICOMIS]
            ESIG[E-signatures]
        end
    end

    ENABLER -->|Support| CORE["ITM Core Business Operations"]
```

### 4.1 Human Resources (HR)

| Aplikasi | Fungsi |
|----------|--------|
| **Sunfish Workplace** | Sistem HRIS (Human Resource Information System) utama |
| **eLeave** | Manajemen cuti elektronik |
| **KPI Online** | Sistem manajemen kinerja dan KPI |
| **Competency Assessment** | Penilaian kompetensi karyawan |
| **Smart Attendance** | Sistem absensi/kehadiran digital |

### 4.2 Health, Safety, Environment & Community (HSEC)

| Aplikasi | Fungsi |
|----------|--------|
| **GoSafe** | Aplikasi keselamatan kerja |
| **Siaga Carmat Hemat (using MDP)** | Sistem siaga dan kesiapan darurat menggunakan Mobile Digital Platform |
| **Incident Report** | Pelaporan insiden keselamatan |
| **SIMPER** | Surat Izin Mengemudi Perusahaan — manajemen izin mengemudi internal |
| **eCommissioning** | Sistem commissioning peralatan elektronik |

### 4.3 Finance

| Aplikasi | Fungsi |
|----------|--------|
| **TREES** | Sistem pelaporan dan analisis keuangan |
| **Intax** | Sistem manajemen perpajakan |
| **BPS** | Budget Planning System — sistem perencanaan anggaran |
| **HOI** | Sistem keuangan pendukung |

### 4.4 General Affairs (GA)

| Aplikasi | Fungsi |
|----------|--------|
| **GA Center** | Pusat layanan General Affairs |
| **eStationary** | Manajemen alat tulis kantor elektronik |
| **e-TA** | Electronic Travel Authorization — manajemen perjalanan dinas |
| **Hot Desk** | Sistem reservasi meja kerja (hot desking) |

### 4.5 Corporate Secretary and Legal (CorSec and Legal)

| Aplikasi | Fungsi |
|----------|--------|
| **eNumbering** | Sistem penomoran dokumen korporat |
| **Transparency Center** | Pusat transparansi dan kepatuhan |
| **ICOMIS** | Integrated Corporate Management Information System |
| **E-signatures** | Tanda tangan digital/elektronik |

---

## 5. Data Management Platform

Fondasi dari seluruh arsitektur adalah **Data Management Platform** yang mencakup:

| Komponen | Deskripsi |
|----------|-----------|
| **ITM One Data** | Inisiatif satu sumber data terpadu (single source of truth) untuk seluruh organisasi |
| **Data Governance** | Tata kelola data — kebijakan, standar, dan prosedur pengelolaan data |
| **Data Quality** | Manajemen kualitas data — memastikan akurasi, kelengkapan, dan konsistensi data |
| **Data Analytics** | Analitik data menggunakan **Power BI** sebagai platform visualisasi dan business intelligence |

---

## Ringkasan Arsitektur

### Diagram: Arsitektur Keseluruhan (Layered View)

```mermaid
flowchart TB
    subgraph D["Digital Mine — E2E Value Chain"]
        direction LR
        EXP["Exploration"] --- PLAN["Planning"] --- OPS["Operations"] --- HAUL["Hauling"] --- STOCK["Stockyards"] --- BARGE["Barging"] --- CUST["Customer"]
    end
    subgraph GOV["Government / Regulatory"]
        direction LR
        RKAB["RKAB Online"] --- MOMS["MOMS/Minerba"] --- EPNBP["E-PNBP"] --- MVP2["MVP"]
    end
    subgraph CORE["ITM Core Business Applications"]
        direction LR
        GIS["GIS & Planning"] --- M2PA["M2P Super Apps"] --- ORACLE["Oracle ERP"] --- MAXIMO["Maximo"]
    end
    subgraph ENABLE["Enabler Applications"]
        direction LR
        HRB["HR"] --- HSECB["HSEC"] --- FINB["Finance"] --- GAB["GA"] --- LEGALB["CorSec & Legal"]
    end
    subgraph DATA["Data Management Platform"]
        direction LR
        ONE["ITM One Data"] --- GOVN["Data Governance"] --- QUAL["Data Quality"] --- ANA["Data Analytics (Power BI)"]
    end

    D --> GOV
    D --> CORE
    CORE --> ENABLE
    CORE --> DATA

    style D fill:#1565C0,color:#fff
    style GOV fill:#0277BD,color:#fff
    style CORE fill:#00838F,color:#fff
    style ENABLE fill:#00695C,color:#fff
    style DATA fill:#E65100,color:#fff
```

### Diagram: Alur Data End-to-End

```mermaid
flowchart TD
    subgraph Sources["Data Sources"]
        direction LR
        S1["Mine Operations\n(SCADA, Truck Scale)"]
        S2["M2P Super Apps\n(Mine Market, SHIPPO)"]
        S3["ERP\n(Oracle, Maximo)"]
        S4["Enabler Apps\n(HR, HSEC, Finance)"]
        S5["Government Systems\n(MOMS, RKAB)"]
    end

    subgraph Platform["Data Management Platform"]
        direction LR
        DG[Data Governance] --> DQ[Data Quality]
        DQ --> OD[ITM One Data]
        OD --> DA[Data Analytics]
    end

    subgraph Output["Business Intelligence"]
        PBI["Power BI\nDashboards & Reports"]
        DEC["Data-Driven\nDecision Making"]
    end

    S1 --> Platform
    S2 --> Platform
    S3 --> Platform
    S4 --> Platform
    S5 --> Platform
    DA --> PBI --> DEC
```

---

## Catatan Penting

- Arsitektur ini menunjukkan **integrasi vertikal** dari operasi tambang hingga pelanggan
- **Mine 2 Port (M2P)** berperan sebagai super-app yang menyatukan berbagai sistem operasional
- **Oracle ERP** menjadi backbone untuk proses procurement, accounting, dan finance
- **Data Management Platform** di lapisan paling bawah menunjukkan komitmen terhadap **data-driven decision making**
- Integrasi dengan sistem pemerintah (ESDM) memastikan kepatuhan regulasi pertambangan Indonesia

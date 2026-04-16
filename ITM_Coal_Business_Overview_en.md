# ITM Coal Business – Core Value Applications and Data Landscape

## Overview

This document describes the application architecture and data landscape of **ITM (Indo Tambangraya Megah)** coal business, covering the entire **Mining Value Chain** — the flow of coal from resource to customer, including supply chain and optimization.

The architecture is divided into **4 main layers**:

1. **Digital Mine (E2E Value Chain)** — End-to-end mining value chain
2. **ITM Core Business Application Landscape** — Core business applications
3. **Enabler Application** — Operational support applications
4. **Data Management Platform** — Unified data management platform

---

## 1. Digital Mine (E2E Value Chain)

This layer illustrates the digital mining operational flow from upstream to downstream:

### Diagram: Mining Value Chain (E2E Flow)

```mermaid
flowchart LR
    subgraph Exploration["🔍 Exploration & Geo Model"]
        A1[Geological Survey]
        A2[Reserve Modeling]
    end

    subgraph Planning["📋 Mine Planning"]
        B1[Pit Planning]
        B2[Production Planning]
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

| Stage | Description | Key Activities |
|-------|-------------|----------------|
| **Exploration and Geo Model** | Geological exploration and modeling | Survey, reserve modeling |
| **Mine Planning** | Mine planning | Production and pit planning |
| **Mine Operations (OB & Coal)** | Overburden & coal mining operations | Drill & Blast, OB Load & Haul, Coal Load & Winning, ROM Stockyard, Disposal |
| **Hauling** | Coal transportation | Coal hauling from pit to stockyard/port |
| **Stockyards** | Stockpile management | Crushing, FC/Port Stockpile |
| **Barging & Shipping** | Barging and shipping operations | Barge Loading (incl. 3rd party), Reclaimer & Ship Loader |
| **Customer** | Marketing and trading | Marketing, Trading |

### Diagram: Detailed Mining Operations Flow

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

## 2. Government / Regulatory Systems (ESDM / Government)

Integration with government systems for regulatory compliance:

| System | Function |
|--------|----------|
| **RKAB Online** | Work Plan and Budget — mine work plan reporting to ESDM (Ministry of Energy and Mineral Resources) |
| **MOMS / Minerba Online** | Mining Operations Management System — production and operations reporting to Directorate General of Minerals and Coal |
| **E-PNBP** | Electronic Non-Tax State Revenue — royalty and levy payments |
| **MVP** | Government verification and validation system |

### Diagram: Government System Integration

```mermaid
flowchart LR
    subgraph GOV["ESDM / Government Systems"]
        direction LR
        RKAB[RKAB Online] --> MOMS[MOMS / Minerba Online]
        MOMS --> EPNBP[E-PNBP]
        EPNBP --> MVP[MVP]
    end

    subgraph ITM["ITM Operations"]
        PLAN[Mine Planning] -.->|Work Plan| RKAB
        OPS[Mine Operations] -.->|Production Report| MOMS
        FIN[Finance] -.->|Royalties & Levies| EPNBP
        SHIP[Shipping] -.->|Verification| MVP
    end
```

---

## 3. ITM Core Business Application Landscape

### 3.1 Geospatial & Planning Applications

| Application | Function |
|-------------|----------|
| **Arc GIS** | Geographic Information System for mapping and spatial analysis |
| **Minex** | Mine planning and geological modeling software |
| **Mine Scape** | Mine modeling and pit planning software |

### 3.2 Mine 2 Port (M2P Super Apps)

A super-app platform integrating operations from mine to port, including:

#### Diagram: M2P Super Apps Ecosystem

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

| Application | Function |
|-------------|----------|
| **Mine Market** | Operations, logistics, through to customer invoicing — end-to-end system for coal sales and distribution management |
| **Truck Scale** | Truck weighing system for tonnage recording |
| **Coal Haul Tracking** | Real-time coal hauling tracking |
| **SCADA** | Supervisory Control and Data Acquisition — operational monitoring and control |
| **SHIPPO** | Shipping operations management system |
| **Coapps** | Operational coordination application |
| **SOS** | Support operations system |

### 3.3 Compliance & Optimization Applications

| Application | Function |
|-------------|----------|
| **PLIS** | Permit and licensing information system |
| **Obligation & Compliance** | Obligation and regulatory compliance management |
| **Mercy** | Operational support application |
| **MOCA** | Monitoring and Control Application |
| **STSC Optimization (SSO)** | Supply Chain Optimization |
| **CoTrap** | Coal Transportation Planning |
| **Squba** | Barging operations support system |

### Diagram: Core Application Integration Map

```mermaid
flowchart TB
    subgraph GEO["Geospatial & Planning"]
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

### 3.4 ERP & Asset Management Systems

| Application | Function |
|-------------|----------|
| **Oracle** | ERP system for **Procurement, Accounting, and Finance** — financial and procurement backbone |
| **Maximo** | Enterprise Asset Management — mining equipment asset and maintenance management |

### 3.5 Operational Support Systems

| Application | Function |
|-------------|----------|
| **ROMA** | Operational management system |
| **MMS** | Maintenance Management System |
| **SLeZ** | Operational support system |

---

## 4. Enabler Applications

Supporting applications that underpin corporate functions:

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
            SCH[Emergency Preparedness]
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

| Application | Function |
|-------------|----------|
| **Sunfish Workplace** | Primary HRIS (Human Resource Information System) |
| **eLeave** | Electronic leave management |
| **KPI Online** | Performance and KPI management system |
| **Competency Assessment** | Employee competency assessment |
| **Smart Attendance** | Digital attendance system |

### 4.2 Health, Safety, Environment & Community (HSEC)

| Application | Function |
|-------------|----------|
| **GoSafe** | Workplace safety application |
| **Siaga Carmat Hemat (using MDP)** | Emergency preparedness system using Mobile Digital Platform |
| **Incident Report** | Safety incident reporting |
| **SIMPER** | Company Driving Permit — internal driving permit management |
| **eCommissioning** | Electronic equipment commissioning system |

### 4.3 Finance

| Application | Function |
|-------------|----------|
| **TREES** | Financial reporting and analysis system |
| **Intax** | Tax management system |
| **BPS** | Budget Planning System |
| **HOI** | Supporting financial system |

### 4.4 General Affairs (GA)

| Application | Function |
|-------------|----------|
| **GA Center** | General Affairs service center |
| **eStationary** | Electronic office supplies management |
| **e-TA** | Electronic Travel Authorization — business travel management |
| **Hot Desk** | Hot desk reservation system |

### 4.5 Corporate Secretary and Legal (CorSec and Legal)

| Application | Function |
|-------------|----------|
| **eNumbering** | Corporate document numbering system |
| **Transparency Center** | Transparency and compliance center |
| **ICOMIS** | Integrated Corporate Management Information System |
| **E-signatures** | Digital/electronic signatures |

---

## 5. Data Management Platform

The foundation of the entire architecture is the **Data Management Platform**, which includes:

| Component | Description |
|-----------|-------------|
| **ITM One Data** | A unified single source of truth initiative for the entire organization |
| **Data Governance** | Data governance — policies, standards, and data management procedures |
| **Data Quality** | Data quality management — ensuring accuracy, completeness, and consistency of data |
| **Data Analytics** | Data analytics using **Power BI** as the visualization and business intelligence platform |

---

## Architecture Summary

### Diagram: Overall Architecture (Layered View)

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

### Diagram: End-to-End Data Flow

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

## Key Takeaways

- This architecture demonstrates **vertical integration** from mining operations through to the customer
- **Mine 2 Port (M2P)** serves as a super-app unifying various operational systems
- **Oracle ERP** is the backbone for procurement, accounting, and finance processes
- The **Data Management Platform** at the bottom layer reflects a commitment to **data-driven decision making**
- Integration with government systems (ESDM) ensures compliance with Indonesian mining regulations

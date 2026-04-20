# Contoso Mining — Data Catalog & Linguistic Metadata

> Dokumen ini mendeskripsikan seluruh tabel, kolom, dan DAX measures di Semantic Model **ContosoMining_SemanticModel**.
> Gunakan informasi **Synonyms** untuk mengoptimalkan Power BI Copilot agar mengenali pertanyaan natural language dalam Bahasa Indonesia maupun Inggris.
>
> **Cara pakai di Power BI:**
> 1. Buka Semantic Model → pilih tabel → pilih kolom
> 2. Di Properties pane, isi **Description** dan **Synonyms** sesuai dokumen ini
> 3. Untuk DAX measures, klik measure → isi Description & Synonyms di Properties

---

## Dimension Tables

### DimTruck

**Description:** Master data armada dump truck tambang. Berisi 20 unit haul truck yang beroperasi di area Adaro, Kalimantan Selatan.

**Synonyms:** Trucks, Armada, Fleet, Dump Truck, Haul Truck, Unit Alat Angkut, Kendaraan Tambang

| Column | Type | Description | Synonyms |
|--------|------|-------------|----------|
| truck_id | string | Identifier unik truck (TRK-001 s/d TRK-020) | ID Truk, Kode Truk, Nomor Unit, Unit ID, Truck Code |
| truck_name | string | Nama tampilan truck | Nama Truk, Nama Unit, Truck Label |
| truck_type | string | Merk dan model truck (Komatsu HD785-7 atau CAT 777F) | Tipe Truk, Jenis Truk, Model, Merk, Brand, Equipment Type |
| max_payload_ton | double | Kapasitas muat maksimum dalam ton (40–42 ton) | Kapasitas Muat, Maximum Payload, Tonnage Capacity, Max Load, Muatan Maksimal |
| operator_name | string | Nama operator/driver yang ditugaskan | Nama Driver, Nama Pengemudi, Operator, Supir |
| commissioning_date | string | Tanggal mulai operasional unit | Tanggal Komisioning, Tanggal Mulai, Start Date, Date Commissioned |

---

### DimRoute

**Description:** Master data rute angkut batubara dari pit ke stockyard atau port.

**Synonyms:** Rute, Routes, Jalur Angkut, Hauling Route, Lintasan, Trayek

| Column | Type | Description | Synonyms |
|--------|------|-------------|----------|
| route_id | int | Identifier numerik rute | ID Rute, Kode Rute, Route Code |
| route_name | string | Nama lengkap rute (contoh: "Pit-A1 to ROM-Stockyard") | Nama Rute, Route Label, Jalur |
| origin | string | Titik asal rute | Asal, Titik Muat, Origin, Source, Loading Point, Pit Asal |
| destination | string | Titik tujuan rute | Tujuan, Titik Bongkar, Destination, Target, Dumping Point |
| distance_km | double | Jarak tempuh rute dalam kilometer | Jarak, Distance, Kilometer, KM, Panjang Rute |
| route_category | string | Kategori rute: Pit-to-ROM, Pit-to-Port, ROM-to-Port | Kategori Rute, Tipe Rute, Route Type, Category |

---

### DimStockpile

**Description:** Master data area penumpukan/penyimpanan batubara (ROM Stockyard dan Port Stockpile).

**Synonyms:** Stockpile, Penumpukan, Timbunan, Stok Batubara, Coal Stockpile, Storage Area, Tempat Penumpukan

| Column | Type | Description | Synonyms |
|--------|------|-------------|----------|
| stockpile_id | string | Identifier unik stockpile (ROM, PORT-A, PORT-B) | ID Stockpile, Kode Stockpile, Stockpile Code |
| stockpile_name | string | Nama lengkap stockpile | Nama Stockpile, Nama Penumpukan, Stockpile Label |
| location | string | Lokasi fisik: "Mine Site" atau "Port Area" | Lokasi, Area, Site, Tempat |
| max_capacity_ton | double | Kapasitas maksimum penyimpanan dalam ton | Kapasitas Maksimal, Maximum Capacity, Max Storage, Kapasitas Tampung |
| coal_quality_spec | string | Spesifikasi kualitas batubara (GAR) | Kualitas Batubara, Coal Quality, Spek, GAR, Kalori |

---

### DimBarge

**Description:** Master data tongkang (barge) untuk pengangkutan batubara via sungai/laut.

**Synonyms:** Tongkang, Barge, Kapal, Vessel, Angkutan Sungai, Angkutan Laut

| Column | Type | Description | Synonyms |
|--------|------|-------------|----------|
| barge_id | string | Identifier unik tongkang (BRG-201 s/d BRG-203) | ID Tongkang, Kode Tongkang, Barge Code, Vessel ID |
| barge_name | string | Nama tampilan tongkang | Nama Tongkang, Barge Label, Nama Kapal |
| owner | string | Perusahaan pemilik/operator tongkang | Pemilik, Operator, Owner Company, Perusahaan Pelayaran |
| max_capacity_ton | double | Kapasitas muat maksimum tongkang dalam ton | Kapasitas Muat, Maximum Capacity, DWT, Daya Angkut |
| vessel_type | string | Tipe tongkang: Flat-top atau Self-propelled | Tipe Kapal, Jenis Tongkang, Vessel Type |

---

### DimJetty

**Description:** Master data dermaga/jetty untuk pemuatan batubara ke tongkang.

**Synonyms:** Dermaga, Jetty, Pelabuhan, Wharf, Loading Dock, Tempat Muat, Jetty Muat

| Column | Type | Description | Synonyms |
|--------|------|-------------|----------|
| jetty_id | string | Identifier unik jetty (JETTY-1, JETTY-2) | ID Dermaga, Kode Jetty, Jetty Code |
| jetty_name | string | Nama dermaga | Nama Dermaga, Nama Jetty, Jetty Label |
| location | string | Lokasi port dermaga (Port-A atau Port-B) | Lokasi, Port, Pelabuhan |
| conveyor_count | int | Jumlah conveyor yang tersedia | Jumlah Conveyor, Conveyor Count, Belt Conveyor |
| max_loading_rate_tph | double | Kecepatan muat maksimum dalam ton per jam (TPH) | Rate Muat, Loading Rate, TPH, Ton Per Hour, Kecepatan Muat |

---

### DimDate

**Description:** Tabel dimensi waktu (kalender) untuk periode 2025–2026. Digunakan sebagai slicer tanggal di report.

**Synonyms:** Tanggal, Kalender, Date, Calendar, Waktu, Periode, Time

| Column | Type | Description | Synonyms |
|--------|------|-------------|----------|
| date_key | int | Surrogate key tanggal dalam format yyyyMMdd (contoh: 20260420) | Kunci Tanggal, Date Key, Date ID |
| full_date | date | Tanggal lengkap | Tanggal Lengkap, Full Date, Calendar Date |
| year | int | Tahun (2025 atau 2026) | Tahun, Year |
| month | int | Bulan (1–12) | Bulan, Month, Month Number |
| day | int | Hari dalam bulan (1–31) | Hari, Day, Day of Month |
| month_name | string | Nama bulan dalam bahasa Inggris (January, February, dll.) | Nama Bulan, Month Name |
| week_of_year | int | Minggu ke-berapa dalam setahun (1–52) | Minggu, Week, Week Number, Minggu Ke |
| day_name | string | Nama hari dalam bahasa Inggris (Monday, Tuesday, dll.) | Nama Hari, Day Name, Hari Dalam Minggu |
| shift_number | int | Nomor shift kerja (1 = Shift Pagi, 2 = Shift Malam) | Shift, Shift Kerja, Work Shift, Shift Number |

---

## Fact Tables

### FactHauling

**Description:** Fact table berisi setiap event pengangkutan batubara oleh dump truck. Mencakup posisi GPS, tonase muatan, kecepatan, dan waktu siklus. Sumber data: HaulingEvents dari Eventhouse (real-time).

**Synonyms:** Hauling, Pengangkutan, Data Angkut, Hauling Events, Trip Data, Data Trip, Ritase, OB Hauling

| Column | Type | Description | Synonyms |
|--------|------|-------------|----------|
| truck_id | string | FK → DimTruck. ID truck yang melakukan trip | ID Truk, Kode Truk, Truck Code |
| timestamp | datetime | Waktu event dicatat (UTC) | Waktu, Tanggal Waktu, Event Time, Timestamp, Jam |
| latitude | double | Koordinat lintang GPS truck | Lintang, Lat, GPS Latitude, Posisi Y |
| longitude | double | Koordinat bujur GPS truck | Bujur, Lon, Long, GPS Longitude, Posisi X |
| speed_kmh | double | Kecepatan truck dalam km/jam | Kecepatan, Speed, KM/H, Velocity, Laju |
| payload_ton | double | Muatan batubara dalam ton (0 jika kosong, 30–42 jika terisi) | Muatan, Tonnase, Payload, Ton, Tonase Angkut, Load |
| status | string | Status operasional truck: loading, loaded, unloading, unloaded, empty, idle | Status, Status Truk, Truck Status, Kondisi |
| route | string | FK → DimRoute.route_name. Nama rute yang dilalui | Rute, Jalur, Route, Jalur Angkut |
| cycle_phase | string | Fase dalam siklus hauling: loading, hauling, queuing, unloading, unloaded, returning, idle | Fase Siklus, Cycle Phase, Phase, Tahap |
| date_key | int | FK → DimDate. Surrogate key tanggal (yyyyMMdd) | Kunci Tanggal, Date Key |
| cycle_time_minutes | double | Waktu siklus hauling lengkap dalam menit (35–55 menit, hanya terisi untuk phase "unloaded") | Waktu Siklus, Cycle Time, CT, Durasi Siklus, Menit Siklus |

**Nilai status yang valid:**
| Status | Deskripsi |
|--------|-----------|
| loading | Truck sedang dimuat di pit |
| loaded | Truck terisi penuh, sedang hauling atau antri |
| unloading | Truck sedang membongkar muatan |
| unloaded | Muatan selesai dibongkar (digunakan untuk menghitung tonnage) |
| empty | Truck kosong, kembali ke pit |
| idle | Truck tidak beroperasi |

---

### FactStockpile

**Description:** Fact table berisi pembacaan sensor level dan suhu stockpile batubara secara berkala. Digunakan untuk monitoring kapasitas dan deteksi risiko spontaneous combustion.

**Synonyms:** Stockpile Data, Data Stockpile, Monitoring Stockpile, Stockpile Events, Level Stockpile, Data Penumpukan

| Column | Type | Description | Synonyms |
|--------|------|-------------|----------|
| stockpile_id | string | FK → DimStockpile. ID area penumpukan | ID Stockpile, Kode Stockpile |
| timestamp | datetime | Waktu pembacaan sensor (UTC) | Waktu, Event Time, Timestamp |
| level_percentage | double | Persentase level isi stockpile (15–92%) | Level, Persentase, Level Persen, Fill Level, Tingkat Isi, Kapasitas Terpakai |
| estimated_tonnage | double | Estimasi tonase batubara saat ini (dihitung dari level × kapasitas) | Tonase Saat Ini, Current Tonnage, Estimated Tons, Stok Saat Ini |
| max_capacity_ton | double | Kapasitas maksimum stockpile dalam ton | Kapasitas Maksimal, Max Capacity |
| coal_quality | string | Kualitas batubara saat ini (GAR-4200, GAR-4700, GAR-5000, GAR-5500) | Kualitas, Coal Quality, GAR, Kalori, Spek Batubara |
| temperature_celsius | double | Suhu stockpile dalam derajat Celsius (risiko > 60°C) | Suhu, Temperature, Temp, Derajat, Temperatur |
| date_key | int | FK → DimDate. Surrogate key tanggal (yyyyMMdd) | Kunci Tanggal, Date Key |

---

### FactBargeLoading

**Description:** Fact table berisi status pemuatan batubara ke tongkang di dermaga. Mencakup progress loading, rate pemuatan, dan estimasi waktu selesai.

**Synonyms:** Barge Loading, Pemuatan Tongkang, Data Tongkang, Barge Events, Loading Data, Data Muat Tongkang, Barging

| Column | Type | Description | Synonyms |
|--------|------|-------------|----------|
| barge_id | string | FK → DimBarge. ID tongkang yang sedang dimuat | ID Tongkang, Kode Tongkang, Barge Code |
| timestamp | datetime | Waktu event pemuatan dicatat (UTC) | Waktu, Event Time, Timestamp |
| jetty_id | string | FK → DimJetty. ID dermaga tempat pemuatan | ID Dermaga, Kode Jetty, Jetty Code |
| loading_rate_tph | double | Kecepatan pemuatan saat ini dalam ton per jam (700–1200 saat loading, 0 saat lainnya) | Rate Muat, Loading Rate, TPH, Ton Per Jam, Kecepatan Muat |
| loaded_tonnage | double | Total tonase yang sudah dimuat ke tongkang | Tonase Termuat, Loaded Tons, Muatan Saat Ini, Progress Muat |
| target_tonnage | double | Target tonase penuh tongkang | Target Muat, Target Tonnage, Kapasitas Target |
| status | string | Status pemuatan: waiting, loading, loaded, departed | Status, Status Muat, Loading Status, Kondisi Tongkang |
| eta_completion | datetime | Estimasi waktu selesai pemuatan | ETA, Estimasi Selesai, Estimated Completion, Waktu Perkiraan Selesai |
| date_key | int | FK → DimDate. Surrogate key tanggal (yyyyMMdd) | Kunci Tanggal, Date Key |

**Nilai status yang valid:**
| Status | Deskripsi |
|--------|-----------|
| waiting | Tongkang menunggu di luar dermaga |
| loading | Tongkang sedang dimuat di jetty |
| loaded | Pemuatan selesai, tongkang penuh |
| departed | Tongkang sudah berangkat |

---

## DAX Measures

### Hauling Measures

| Measure | Description | Synonyms |
|---------|-------------|----------|
| Total Tonnage | Total tonase batubara yang berhasil diangkut (status = unloaded) | Total Tonase, Tonnage, Total Muatan, Jumlah Tonase, Total Angkut |
| Total Trips | Jumlah trip selesai (status = unloaded) | Jumlah Trip, Total Perjalanan, Total Ritase, Trip Count |
| Avg Payload Per Trip | Rata-rata muatan per trip dalam ton | Rata-rata Muatan, Average Payload, Muatan Rata-Rata |
| Avg Cycle Time (min) | Rata-rata waktu siklus hauling lengkap dalam menit | Rata-rata Waktu Siklus, Average Cycle Time, CT Rata-Rata |
| Tonnage vs Target % | Persentase pencapaian target tonase harian (target: 15,000 ton) | Pencapaian Target, Achievement, Target Percentage, Persentase Target |
| Active Trucks | Jumlah truck yang sedang beroperasi (status ≠ idle) | Truk Aktif, Active Fleet, Jumlah Truk Aktif, Unit Beroperasi |
| Idle Trucks | Jumlah truck yang tidak beroperasi (status = idle) | Truk Idle, Truk Menganggur, Idle Fleet, Unit Tidak Beroperasi |
| Truck Utilization % | Persentase utilisasi armada (Active / Total trucks) | Utilisasi Truk, Fleet Utilization, Persen Utilisasi, Pemakaian Alat |

### Stockpile Measures

| Measure | Description | Synonyms |
|---------|-------------|----------|
| Stockpile Utilization % | Persentase utilisasi stockpile (tonase saat ini / kapasitas maks) | Utilisasi Stockpile, Pemakaian Stockpile, Tingkat Isi, Fill Rate |
| Avg Temperature | Rata-rata suhu stockpile dalam °C | Rata-rata Suhu, Average Temperature, Suhu Rata-Rata, Temperatur |
| Critical Stockpiles | Jumlah stockpile dengan level < 30% (perlu refill) | Stockpile Kritis, Low Stock, Stockpile Rendah, Stok Kritis |

### Barge Loading Measures

| Measure | Description | Synonyms |
|---------|-------------|----------|
| Loading Efficiency % | Efisiensi pemuatan (tonase termuat / target tonase) | Efisiensi Muat, Loading Efficiency, Persen Muat |
| Avg Loading Rate (TPH) | Rata-rata kecepatan pemuatan dalam ton per jam | Rata-rata Rate Muat, Average Loading Rate, TPH Rata-Rata |
| Barges Completed | Jumlah tongkang yang selesai dimuat (status loaded atau departed) | Tongkang Selesai, Barge Done, Jumlah Tongkang Selesai |
| Total Shipped Tonnage | Total tonase batubara yang sudah dikirim via tongkang | Total Tonase Kirim, Shipped Tonnage, Total Pengiriman |
| Avg Barge Wait Time (hrs) | Rata-rata waktu tunggu tongkang sebelum dimuat dalam jam | Waktu Tunggu Tongkang, Barge Wait Time, Antrian Tongkang |

---

## Relationships (Star Schema)

```
DimTruck ──── truck_id ────── FactHauling
DimRoute ──── route_name ──── FactHauling (via route)
DimDate ───── date_key ────── FactHauling
DimDate ───── date_key ────── FactStockpile
DimDate ───── date_key ────── FactBargeLoading
DimStockpile ─ stockpile_id ─ FactStockpile
DimBarge ──── barge_id ────── FactBargeLoading
DimJetty ──── jetty_id ────── FactBargeLoading
```

Semua relationship: **Many-to-One** (Fact → Dim), **Single direction** filter.

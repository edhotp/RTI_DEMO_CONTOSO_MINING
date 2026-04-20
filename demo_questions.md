# Contoso Mining — Demo Questions for Fabric Data Agent & Power BI Copilot

> Daftar pertanyaan demo yang disusun berdasarkan schema dan data generator proyek ini.
> Dikelompokkan berdasarkan **kompleksitas** (Low → Medium → High) dan **domain** (Hauling, Stockpile, Barge, Cross-Domain).
>
> **Cara pakai:**
> - **Power BI Copilot:** Tanyakan langsung di Copilot pane pada report/semantic model
> - **Fabric Data Agent:** Tanyakan via Data Agent chat yang terhubung ke Eventhouse/Lakehouse
>
> **Tips demo:**
> - Mulai dari pertanyaan sederhana (Level 1) untuk menunjukkan kemudahan
> - Naikkan kompleksitas secara bertahap untuk menunjukkan kecerdasan
> - Gunakan campuran Bahasa Indonesia & English untuk menunjukkan bilingual support
> - Setelah tiap jawaban, tunjukkan visual yang dihasilkan Copilot

---

## Level 1 — Low Complexity (Single Table, Direct Lookup)

> Pertanyaan simpel yang hanya melibatkan 1 tabel, tanpa perhitungan kompleks.
> Cocok untuk membuka demo dan menunjukkan betapa mudahnya bertanya.

### Hauling

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 1.1 | Berapa jumlah truk yang ada? | How many trucks do we have? | Scorecard: 20 |
| 1.2 | Tampilkan daftar semua truk beserta tipenya | Show all trucks and their types | Table: truck_id, truck_name, truck_type |
| 1.3 | Truk apa saja yang bertipe Komatsu? | Which trucks are Komatsu models? | Table: filtered DimTruck where truck_type contains "Komatsu" |
| 1.4 | Siapa operator truk TRK-005? | Who is the operator of truck TRK-005? | Card: "Driver E" |
| 1.5 | Berapa kapasitas muat maksimal CAT 777F? | What is the max payload of CAT 777F? | Card: 40 tons |
| 1.6 | Tampilkan semua rute yang tersedia | Show all available routes | Table: DimRoute with route_name, distance_km |
| 1.7 | Berapa jarak rute Pit-A1 ke ROM-Stockyard? | What is the distance of Pit-A1 to ROM-Stockyard route? | Card: 5.2 km |

### Stockpile

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 1.8 | Ada berapa stockpile? | How many stockpiles are there? | Card: 3 |
| 1.9 | Tampilkan daftar stockpile dan kapasitasnya | List all stockpiles with their capacity | Table: stockpile_id, stockpile_name, max_capacity_ton |
| 1.10 | Berapa kapasitas maksimal ROM Stockyard? | What is the max capacity of ROM Stockyard? | Card: 80,000 tons |
| 1.11 | Stockpile mana yang ada di Port Area? | Which stockpiles are in the Port Area? | Table: PORT-A, PORT-B |

### Barge & Jetty

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 1.12 | Ada berapa tongkang yang beroperasi? | How many barges are in operation? | Card: 3 |
| 1.13 | Siapa pemilik tongkang BRG-201? | Who owns barge BRG-201? | Card: "PT Pelayaran Nusantara" |
| 1.14 | Berapa jumlah conveyor di Jetty Utama? | How many conveyors does the main jetty have? | Card: 2 |
| 1.15 | Tampilkan semua dermaga dan rate muat maksimalnya | Show all jetties and their max loading rates | Table: jetty_id, jetty_name, max_loading_rate_tph |

---

## Level 2 — Low-Medium Complexity (Single Fact Table, Simple Aggregation)

> Pertanyaan yang melibatkan 1 fact table dengan agregasi sederhana (SUM, COUNT, AVG).
> Menunjukkan kemampuan Copilot menghasilkan measure dari data real-time.

### Hauling

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 2.1 | Berapa total tonase hari ini? | What is today's total tonnage? | Scorecard: Total Tonnage (filtered today) |
| 2.2 | Berapa jumlah trip yang sudah selesai hari ini? | How many trips are completed today? | Scorecard: count where status = "unloaded" |
| 2.3 | Berapa rata-rata muatan per trip? | What is the average payload per trip? | Scorecard: Avg Payload Per Trip |
| 2.4 | Berapa rata-rata kecepatan truk saat ini? | What is the current average truck speed? | Scorecard: avg speed_kmh where speed > 0 |
| 2.5 | Berapa truk yang sedang aktif? | How many trucks are currently active? | Scorecard: Active Trucks |
| 2.6 | Truk mana saja yang sedang idle? | Which trucks are currently idle? | Table: truck_id where status = "idle" |
| 2.7 | Berapa rata-rata cycle time? | What is the average cycle time? | Scorecard: Avg Cycle Time (min) |

### Stockpile

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 2.8 | Berapa level stockpile saat ini? | What are the current stockpile levels? | Bar chart: level_percentage by stockpile_id |
| 2.9 | Berapa tonase batubara di semua stockpile sekarang? | What is the total coal tonnage across all stockpiles now? | Scorecard: sum estimated_tonnage (latest) |
| 2.10 | Berapa suhu rata-rata stockpile? | What is the average stockpile temperature? | Scorecard: Avg Temperature |
| 2.11 | Ada stockpile yang suhunya di atas 50 derajat? | Are there any stockpiles above 50 degrees? | Table: stockpile_id, temperature_celsius where > 50 |

### Barge

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 2.12 | Bagaimana progress muat tongkang saat ini? | What is the current barge loading progress? | Table: barge_id, loaded_tonnage, target_tonnage, progress % |
| 2.13 | Berapa total tonase yang sudah dikirim via tongkang? | How much tonnage has been shipped via barge? | Scorecard: Total Shipped Tonnage |
| 2.14 | Berapa rata-rata loading rate saat ini? | What is the current average loading rate? | Scorecard: Avg Loading Rate (TPH) |
| 2.15 | Tongkang mana yang sedang menunggu? | Which barges are currently waiting? | Table: barge_id where status = "waiting" |

---

## Level 3 — Medium Complexity (Joins, Grouping, Ranking)

> Pertanyaan yang melibatkan join antara fact dan dimension table, group by, dan ranking.
> Menunjukkan Copilot bisa menyusun query multi-tabel.

### Hauling

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 3.1 | Tampilkan total tonase per truk hari ini, urutkan dari tertinggi | Show today's tonnage by truck, sorted highest first | Bar chart: truck_id vs Total Tonnage, descending |
| 3.2 | Truk mana yang mengangkut paling banyak hari ini? | Which truck hauled the most today? | Card + detail: top 1 truck by tonnage |
| 3.3 | Berapa total tonase per rute? | What is the total tonnage by route? | Bar chart: route vs Total Tonnage |
| 3.4 | Rute mana yang paling banyak dilalui? | Which route has the most trips? | Bar chart: route vs trip count |
| 3.5 | Tampilkan distribusi tipe truk dan total tonasenya | Show truck type distribution and their total tonnage | Bar chart: truck_type vs Total Tonnage |
| 3.6 | Berapa rata-rata kecepatan per rute? | What is the average speed per route? | Table: route, avg speed_kmh |
| 3.7 | Top 5 truk dengan cycle time tercepat | Top 5 trucks with fastest cycle time | Table: top 5 by avg cycle_time_minutes ascending |
| 3.8 | Berapa tonase yang diangkut truk Komatsu vs CAT hari ini? | Compare Komatsu vs CAT tonnage today | Bar chart: truck_type vs Total Tonnage |

### Stockpile

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 3.9 | Stockpile mana yang paling penuh saat ini? | Which stockpile is most full right now? | Card: stockpile with highest level_percentage |
| 3.10 | Berapa utilisasi setiap stockpile? | What is each stockpile's utilization? | Bar chart: stockpile_id vs utilization % |
| 3.11 | Tampilkan stockpile beserta lokasi dan kualitas batubaranya | Show stockpiles with their location and coal quality | Table: joined DimStockpile + FactStockpile |
| 3.12 | Stockpile mana yang kritis (level < 30%)? | Which stockpiles are critical (below 30%)? | Table: stockpile_id, level_percentage where < 30 |

### Barge

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 3.13 | Tampilkan progress muat per tongkang beserta nama jettynya | Show loading progress by barge with jetty name | Table: barge_name, jetty_name, loaded_tonnage, target, progress % |
| 3.14 | Berapa rata-rata loading rate per jetty? | What is the average loading rate per jetty? | Bar chart: jetty_id vs avg loading_rate_tph |
| 3.15 | Jetty mana yang paling produktif? | Which jetty is most productive? | Card: jetty with highest total loaded_tonnage |
| 3.16 | Berapa tongkang yang sudah selesai dimuat? | How many barges have completed loading? | Scorecard: Barges Completed |

---

## Level 4 — Medium-High Complexity (Multi-Measure, Conditional, Time-Based)

> Pertanyaan yang melibatkan multiple measures, kondisi logika, atau analisis berbasis waktu.
> Menunjukkan kemampuan Copilot menangani pertanyaan bisnis yang lebih realistis.

### Hauling — Performance & Target

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 4.1 | Berapa persen pencapaian target tonase hari ini? | What is today's tonnage target achievement? | Scorecard: Tonnage vs Target % (target 15,000 tons) |
| 4.2 | Apakah kita on-track untuk mencapai target 15.000 ton hari ini? | Are we on track to reach the 15,000 ton daily target? | Card with context: current tonnage, target %, hours remaining |
| 4.3 | Berapa utilisasi fleet saat ini? | What is the current fleet utilization? | Scorecard: Truck Utilization % |
| 4.4 | Tampilkan performa fleet: truk aktif, idle, utilisasi, dan cycle time | Show fleet performance: active, idle, utilization, and cycle time | Multi-card: Active, Idle, Util %, Avg CT |
| 4.5 | Truk mana yang idle lebih dari 30 menit? | Which trucks have been idle for more than 30 minutes? | Table: truck_id, idle duration |
| 4.6 | Bandingkan produktivitas shift 1 vs shift 2 | Compare productivity of shift 1 vs shift 2 | Bar chart: shift_number vs Total Tonnage, Total Trips |

### Stockpile — Monitoring & Alerts

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 4.7 | Apakah ada stockpile yang berisiko terbakar spontan? | Are there any stockpiles at risk of spontaneous combustion? | Table: stockpile with temperature > 60°C flagged CRITICAL |
| 4.8 | Tampilkan status semua stockpile: level, suhu, dan status keamanan | Show all stockpile status: level, temperature, and safety status | Table with conditional formatting |
| 4.9 | Berapa stockpile yang perlu segera diisi ulang? | How many stockpiles need immediate refilling? | Scorecard: Critical Stockpiles (level < 30%) |
| 4.10 | Bagaimana tren level stockpile ROM dalam 24 jam terakhir? | What is the ROM stockpile level trend over the last 24 hours? | Line chart: timestamp vs level_percentage for ROM |

### Barge — Efficiency & ETA

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 4.11 | Berapa efisiensi pemuatan tongkang keseluruhan? | What is the overall barge loading efficiency? | Scorecard: Loading Efficiency % |
| 4.12 | Kapan tongkang BRG-201 diperkirakan selesai dimuat? | When will barge BRG-201 finish loading? | Card: eta_completion for BRG-201 |
| 4.13 | Tongkang mana yang paling lama menunggu? | Which barge has been waiting the longest? | Card: barge with longest wait time |
| 4.14 | Apakah ada tongkang dengan loading rate di bawah normal (< 700 TPH)? | Are there any barges with below-normal loading rates? | Table: barge_id, loading_rate_tph where < 700 |

---

## Level 5 — High Complexity (Cross-Domain, Analytical, Scenario-Based)

> Pertanyaan analitis yang menggabungkan data lintas domain (hauling + stockpile + barge).
> Menunjukkan kemampuan Copilot untuk insight operasional end-to-end.

### Supply Chain Overview

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 5.1 | Berikan ringkasan operasional lengkap hari ini: tonase diangkut, level stockpile, dan progress muat tongkang | Give a full operations summary today: tonnage hauled, stockpile levels, and barge loading progress | Multi-visual: 3 scorecards + summary table |
| 5.2 | Apakah ada bottleneck di supply chain kita hari ini? | Are there any bottlenecks in our supply chain today? | Analysis: compare hauling rate vs stockpile outflow vs barge loading rate |
| 5.3 | Berapa rasio antara tonase yang diangkut ke stockpile vs tonase yang dimuat ke tongkang? | What is the ratio of tonnage hauled to stockpile vs tonnage loaded to barge? | Card: ratio comparison |
| 5.4 | Jika semua truk aktif terus beroperasi, berapa estimasi tonase akhir hari ini? | If all active trucks keep operating, what is the estimated end-of-day tonnage? | Calculation: current rate × remaining hours |

### Fleet & Route Optimization

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 5.5 | Rute mana yang paling efisien berdasarkan tonase per kilometer? | Which route is most efficient based on tonnage per kilometer? | Table: route, tonnage, distance, tonnage/km ratio |
| 5.6 | Apakah ada korelasi antara jarak rute dan cycle time? | Is there a correlation between route distance and cycle time? | Scatter plot: distance_km vs avg cycle_time_minutes |
| 5.7 | Truk mana yang paling produktif dan di rute mana mereka beroperasi? | Which trucks are most productive and on which routes do they operate? | Table: top trucks with route, tonnage, trips |
| 5.8 | Berapa truk tambahan yang dibutuhkan agar target 15.000 ton tercapai? | How many additional trucks are needed to reach the 15,000 ton target? | Calculation: gap / avg payload per truck |

### Stockpile Balance & Risk

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 5.9 | Apakah input ke stockpile (dari hauling) seimbang dengan output (ke barge)? | Is the stockpile input (from hauling) balanced with output (to barge)? | Comparison: hauling tonnage to stockpile vs barge loaded tonnage |
| 5.10 | Dengan rate muat saat ini, berapa jam lagi stockpile PORT-A akan kosong? | At the current loading rate, how many hours until PORT-A stockpile is empty? | Calculation: estimated_tonnage / loading_rate_tph |
| 5.11 | Stockpile mana yang paling berisiko: level kritis DAN suhu tinggi? | Which stockpile has the highest risk: critical level AND high temperature? | Table: stockpile with combined risk score |
| 5.12 | Berapa total kapasitas yang tersisa di semua stockpile? | What is the total remaining capacity across all stockpiles? | Card: sum(max_capacity - estimated_tonnage) |

### Barge Logistics

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 5.13 | Berapa total tonase yang bisa dikirim jika semua tongkang penuh? | What is the total shippable tonnage if all barges are fully loaded? | Card: sum(target_tonnage) = 25,500 tons |
| 5.14 | Apakah kapasitas jetty cukup untuk melayani semua tongkang secara bersamaan? | Is the jetty capacity sufficient to serve all barges simultaneously? | Analysis: conveyor count vs barge count at each jetty |
| 5.15 | Berapa waktu yang diperlukan untuk memuat semua tongkang dari nol? | How long to load all barges from zero? | Calculation: sum(target_tonnage) / sum(max_loading_rate_tph) |

---

## Level 6 — Expert (What-If, Predictive, Executive-Level)

> Pertanyaan level eksekutif dan skenario what-if.
> Menunjukkan batas kemampuan Copilot dan kapan perlu custom DAX/notebook.

### Executive Questions

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 6.1 | Buatkan executive summary untuk laporan shift ini | Create an executive summary for this shift report | Text summary: tonnage, target %, fleet util, stockpile status, barge status |
| 6.2 | Apa 3 hal yang perlu segera diperhatikan manajemen? | What are the top 3 things management should pay attention to right now? | Prioritized list: based on alerts (temp, low stock, idle trucks) |
| 6.3 | Bandingkan performa hari ini vs kemarin | Compare today's performance vs yesterday | Table: tonnage, trips, utilization — today vs yesterday |
| 6.4 | Tampilkan tren tonase harian selama seminggu terakhir | Show daily tonnage trend for the last week | Line chart: date vs Total Tonnage (7 days) |
| 6.5 | Hari apa dalam seminggu terakhir yang produksinya paling rendah? | Which day in the last week had the lowest production? | Card: date with min tonnage |

### What-If Scenarios

| # | Bahasa Indonesia | English | Expected Output |
|---|---|---|---|
| 6.6 | Jika 5 truk rusak mendadak, berapa estimasi tonase yang hilang per shift? | If 5 trucks break down, how much tonnage would we lose per shift? | Calculation: 5 × avg payload × avg trips per truck per shift |
| 6.7 | Jika target naik menjadi 20.000 ton/hari, berapa utilisasi fleet yang dibutuhkan? | If target increases to 20,000 tons/day, what fleet utilization is needed? | Calculation: 20000 / (20 trucks × avg payload × avg trips) |
| 6.8 | Berapa lama stockpile ROM bisa bertahan tanpa input dari hauling? | How long can ROM stockpile sustain without hauling input? | Calculation: current ROM tonnage / barge loading rate |
| 6.9 | Jika loading rate tongkang naik 20%, berapa jam lebih cepat pengiriman selesai? | If barge loading rate increases 20%, how many hours faster would shipping complete? | Before/after comparison |
| 6.10 | Bagaimana jika kita menambah 1 jetty baru dengan kapasitas 1000 TPH? | What if we add a new jetty with 1000 TPH capacity? | Scenario analysis: impact on total throughput |

---

## Pertanyaan Khusus untuk Demo Fabric Data Agent (KQL)

> Fabric Data Agent yang terhubung ke Eventhouse (KQL Database) bisa menjawab pertanyaan
> secara real-time langsung dari streaming data.

| # | Pertanyaan | Expected KQL Pattern |
|---|---|---|
| A.1 | Tampilkan 10 event hauling terbaru | `HaulingEvents \| top 10 by timestamp desc` |
| A.2 | Berapa total tonase yang diangkut dalam 1 jam terakhir? | `HaulingEvents \| where timestamp > ago(1h) \| where status == "unloaded" \| summarize sum(payload_ton)` |
| A.3 | Dimana posisi semua truk sekarang? | `HaulingEvents \| summarize arg_max(timestamp, *) by truck_id \| project truck_id, latitude, longitude, status` |
| A.4 | Truk mana yang kecepatannya di atas 35 km/jam? | `HaulingEvents \| summarize arg_max(timestamp, *) by truck_id \| where speed_kmh > 35` |
| A.5 | Berapa distribusi phase truk saat ini? | `HaulingEvents \| summarize arg_max(timestamp, *) by truck_id \| summarize count() by cycle_phase` |
| A.6 | Tampilkan tren tonase per 10 menit dalam 1 jam terakhir | `HaulingEvents \| where timestamp > ago(1h) \| where status == "unloaded" \| summarize sum(payload_ton) by bin(timestamp, 10m)` |
| A.7 | Stockpile mana yang suhunya paling tinggi sekarang? | `StockpileEvents \| summarize arg_max(timestamp, *) by stockpile_id \| top 1 by temperature_celsius desc` |
| A.8 | Tren suhu stockpile ROM 6 jam terakhir | `StockpileEvents \| where stockpile_id == "ROM" \| where timestamp > ago(6h) \| summarize avg(temperature_celsius) by bin(timestamp, 30m)` |
| A.9 | Tongkang mana yang progress muatnya paling tinggi? | `BargeLoadingEvents \| summarize arg_max(timestamp, *) by barge_id \| extend progress = loaded_tonnage/target_tonnage*100 \| top 1 by progress desc` |
| A.10 | Tampilkan timeline event tongkang BRG-201 dalam 2 jam terakhir | `BargeLoadingEvents \| where barge_id == "BRG-201" \| where timestamp > ago(2h) \| project timestamp, status, loaded_tonnage, loading_rate_tph \| order by timestamp asc` |

---

## Skenario Demo Flow (Recommended)

> Urutan pertanyaan yang direkomendasikan untuk demo 15–20 menit.

### Opening — "Wow Factor" (2 menit)

```
1. "Berapa total tonase hari ini?" (2.1)
2. "Truk mana yang idle?" (2.6)  
3. "Bagaimana progress muat tongkang?" (2.12)
```

### Deep Dive — Hauling (5 menit)

```
4. "Top 5 truk yang paling produktif hari ini" (3.1)
5. "Berapa persen pencapaian target?" (4.1)
6. "Bandingkan tonase Komatsu vs CAT" (3.8)
7. "Tampilkan performa fleet lengkap" (4.4)
```

### Deep Dive — Stockpile & Safety (3 menit)

```
8. "Berapa level semua stockpile?" (2.8)
9. "Ada yang berisiko terbakar spontan?" (4.7)
10. "Stockpile mana yang kritis?" (3.12)
```

### Deep Dive — Barge & Shipping (3 menit)

```
11. "Berapa efisiensi pemuatan tongkang?" (4.11)
12. "Kapan BRG-201 selesai dimuat?" (4.12)
13. "Berapa total yang sudah dikirim?" (2.13)
```

### Grand Finale — Cross-Domain & Executive (5 menit)

```
14. "Berikan ringkasan operasional lengkap" (5.1)
15. "Ada bottleneck di supply chain?" (5.2)
16. "Apa 3 hal yang perlu diperhatikan manajemen?" (6.2)
17. "Bandingkan performa hari ini vs kemarin" (6.3)
```

---

## Tips untuk Demo yang Sukses

| Tip | Detail |
|---|---|
| **Jalankan data generator** | Pastikan `data_generator.py` berjalan minimal 10 menit sebelum demo agar ada cukup data historis |
| **Gunakan bilingual** | Tunjukkan bahwa Copilot mengerti Bahasa Indonesia dan English karena sudah dikonfigurasi synonyms |
| **Tunjukkan visual** | Setelah jawaban Copilot, klik "Add to page" untuk menunjukkan visual interaktif |
| **Narasi bisnis** | Bungkus setiap pertanyaan dengan konteks bisnis: "Sebagai site manager yang baru datang shift pagi..." |
| **Handle error gracefully** | Jika Copilot salah jawab, jelaskan bahwa ini nondeterministic dan tunjukkan cara refine prompt |
| **Prep for AI badge** | Tunjukkan badge "Prepped for AI" di semantic model untuk menunjukkan governance |
| **Verified answers** | Demo verified answers terakhir untuk menunjukkan guaranteed accuracy untuk pertanyaan kritikal |

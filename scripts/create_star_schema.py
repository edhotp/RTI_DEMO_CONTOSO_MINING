# ============================================================
# Contoso Mining — Create Star Schema (Lakehouse)
# ============================================================
# Jalankan di Fabric Notebook yang terhubung ke Lakehouse
# ContosoMiningLH. Paste seluruh isi file ini ke satu cell.
# ============================================================

from pyspark.sql import functions as F
from pyspark.sql.types import *
from pyspark.sql.functions import col, year, month, dayofmonth, date_format, weekofyear
import datetime

print("Creating dimension tables...")

# =========================
# DimTruck
# =========================
dim_truck_data = [
    ("TRK-001", "Truck 001", "Komatsu HD785-7", 42.0, "Driver A", "2023-01-15"),
    ("TRK-002", "Truck 002", "CAT 777F", 40.0, "Driver B", "2023-03-20"),
    ("TRK-003", "Truck 003", "Komatsu HD785-7", 42.0, "Driver C", "2022-08-10"),
    ("TRK-004", "Truck 004", "CAT 777F", 40.0, "Driver D", "2023-06-01"),
    ("TRK-005", "Truck 005", "Komatsu HD785-7", 42.0, "Driver E", "2022-11-22"),
    ("TRK-006", "Truck 006", "CAT 777F", 40.0, "Driver F", "2023-02-14"),
    ("TRK-007", "Truck 007", "Komatsu HD785-7", 42.0, "Driver G", "2022-05-30"),
    ("TRK-008", "Truck 008", "CAT 777F", 40.0, "Driver H", "2023-09-12"),
    ("TRK-009", "Truck 009", "Komatsu HD785-7", 42.0, "Driver I", "2022-12-01"),
    ("TRK-010", "Truck 010", "CAT 777F", 40.0, "Driver J", "2023-04-18"),
    ("TRK-011", "Truck 011", "Komatsu HD785-7", 42.0, "Driver K", "2023-07-05"),
    ("TRK-012", "Truck 012", "CAT 777F", 40.0, "Driver L", "2022-10-20"),
    ("TRK-013", "Truck 013", "Komatsu HD785-7", 42.0, "Driver M", "2023-01-28"),
    ("TRK-014", "Truck 014", "CAT 777F", 40.0, "Driver N", "2022-06-15"),
    ("TRK-015", "Truck 015", "Komatsu HD785-7", 42.0, "Driver O", "2023-08-08"),
    ("TRK-016", "Truck 016", "CAT 777F", 40.0, "Driver P", "2022-04-25"),
    ("TRK-017", "Truck 017", "Komatsu HD785-7", 42.0, "Driver Q", "2023-11-10"),
    ("TRK-018", "Truck 018", "CAT 777F", 40.0, "Driver R", "2022-09-03"),
    ("TRK-019", "Truck 019", "Komatsu HD785-7", 42.0, "Driver S", "2023-05-22"),
    ("TRK-020", "Truck 020", "CAT 777F", 40.0, "Driver T", "2022-07-17"),
]
dim_truck_schema = StructType([
    StructField("truck_id", StringType()), StructField("truck_name", StringType()),
    StructField("truck_type", StringType()), StructField("max_payload_ton", DoubleType()),
    StructField("operator_name", StringType()), StructField("commissioning_date", StringType()),
])
spark.createDataFrame(dim_truck_data, dim_truck_schema) \
    .write.mode("overwrite").format("delta").saveAsTable("DimTruck")
print("  ✅ DimTruck")

# =========================
# DimRoute
# =========================
dim_route_data = [
    (1, "Pit-A1 to ROM-Stockyard", "Pit-A1", "ROM-Stockyard", 5.2, "Pit-to-ROM"),
    (2, "Pit-A2 to ROM-Stockyard", "Pit-A2", "ROM-Stockyard", 6.8, "Pit-to-ROM"),
    (3, "Pit-B1 to Port-A", "Pit-B1", "Port-A", 12.5, "Pit-to-Port"),
    (4, "ROM-Stockyard to Port-A", "ROM-Stockyard", "Port-A", 8.3, "ROM-to-Port"),
    (5, "ROM-Stockyard to Port-B", "ROM-Stockyard", "Port-B", 9.1, "ROM-to-Port"),
]
dim_route_schema = StructType([
    StructField("route_id", IntegerType()), StructField("route_name", StringType()),
    StructField("origin", StringType()), StructField("destination", StringType()),
    StructField("distance_km", DoubleType()), StructField("route_category", StringType()),
])
spark.createDataFrame(dim_route_data, dim_route_schema) \
    .write.mode("overwrite").format("delta").saveAsTable("DimRoute")
print("  ✅ DimRoute")

# =========================
# DimStockpile
# =========================
dim_stockpile_data = [
    ("ROM", "ROM Stockyard", "Mine Site", 80000.0, "Mixed"),
    ("PORT-A", "Port-A Stockpile", "Port Area", 50000.0, "GAR-4200"),
    ("PORT-B", "Port-B Stockpile", "Port Area", 50000.0, "GAR-5000"),
]
dim_sp_schema = StructType([
    StructField("stockpile_id", StringType()), StructField("stockpile_name", StringType()),
    StructField("location", StringType()), StructField("max_capacity_ton", DoubleType()),
    StructField("coal_quality_spec", StringType()),
])
spark.createDataFrame(dim_stockpile_data, dim_sp_schema) \
    .write.mode("overwrite").format("delta").saveAsTable("DimStockpile")
print("  ✅ DimStockpile")

# =========================
# DimBarge
# =========================
dim_barge_data = [
    ("BRG-201", "Barge 201", "PT Pelayaran Nusantara", 8000.0, "Flat-top"),
    ("BRG-202", "Barge 202", "PT Samudera Logistics", 7500.0, "Flat-top"),
    ("BRG-203", "Barge 203", "PT Pelayaran Nusantara", 10000.0, "Self-propelled"),
]
dim_barge_schema = StructType([
    StructField("barge_id", StringType()), StructField("barge_name", StringType()),
    StructField("owner", StringType()), StructField("max_capacity_ton", DoubleType()),
    StructField("vessel_type", StringType()),
])
spark.createDataFrame(dim_barge_data, dim_barge_schema) \
    .write.mode("overwrite").format("delta").saveAsTable("DimBarge")
print("  ✅ DimBarge")

# =========================
# DimJetty
# =========================
dim_jetty_data = [
    ("JETTY-1", "Jetty Utama", "Port-A", 2, 1200.0),
    ("JETTY-2", "Jetty Cadangan", "Port-B", 1, 800.0),
]
dim_jetty_schema = StructType([
    StructField("jetty_id", StringType()), StructField("jetty_name", StringType()),
    StructField("location", StringType()), StructField("conveyor_count", IntegerType()),
    StructField("max_loading_rate_tph", DoubleType()),
])
spark.createDataFrame(dim_jetty_data, dim_jetty_schema) \
    .write.mode("overwrite").format("delta").saveAsTable("DimJetty")
print("  ✅ DimJetty")

# =========================
# DimDate (2 tahun: 2025-2026)
# =========================
dates = [(datetime.date(2025, 1, 1) + datetime.timedelta(days=i),) for i in range(730)]
df_date = spark.createDataFrame(dates, ["full_date"])
df_date = df_date \
    .withColumn("date_key", F.date_format("full_date", "yyyyMMdd").cast("int")) \
    .withColumn("year", year("full_date")) \
    .withColumn("month", month("full_date")) \
    .withColumn("day", dayofmonth("full_date")) \
    .withColumn("month_name", date_format("full_date", "MMMM")) \
    .withColumn("week_of_year", weekofyear("full_date")) \
    .withColumn("day_name", date_format("full_date", "EEEE")) \
    .withColumn("shift_number", F.when(F.hour(F.current_timestamp()) < 14, 1).otherwise(2))
df_date.write.mode("overwrite").format("delta").saveAsTable("DimDate")
print("  ✅ DimDate (730 rows)")

# =========================
# Fact Tables (transform dari Eventhouse shortcut)
# =========================
print("\nCreating fact tables from Eventhouse shortcut...")

try:
    df_hauling = spark.sql("SELECT * FROM HaulingEvents")
    df_hauling = df_hauling \
        .withColumn("date_key", F.date_format("timestamp", "yyyyMMdd").cast("int")) \
        .withColumn("cycle_time_minutes", F.lit(None).cast("double"))
    df_hauling.write.mode("overwrite").format("delta").saveAsTable("FactHauling")
    print(f"  ✅ FactHauling ({df_hauling.count()} rows)")
except Exception as e:
    print(f"  ⚠️ FactHauling skipped (run data generator first): {e}")

try:
    df_stockpile = spark.sql("SELECT * FROM StockpileEvents")
    df_stockpile = df_stockpile \
        .withColumn("date_key", F.date_format("timestamp", "yyyyMMdd").cast("int"))
    df_stockpile.write.mode("overwrite").format("delta").saveAsTable("FactStockpile")
    print(f"  ✅ FactStockpile ({df_stockpile.count()} rows)")
except Exception as e:
    print(f"  ⚠️ FactStockpile skipped: {e}")

try:
    df_barge = spark.sql("SELECT * FROM BargeLoadingEvents")
    df_barge = df_barge \
        .withColumn("date_key", F.date_format("timestamp", "yyyyMMdd").cast("int"))
    df_barge.write.mode("overwrite").format("delta").saveAsTable("FactBargeLoading")
    print(f"  ✅ FactBargeLoading ({df_barge.count()} rows)")
except Exception as e:
    print(f"  ⚠️ FactBargeLoading skipped: {e}")

print("\n✅ Star schema setup complete!")

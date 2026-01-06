from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, sum, date_format

spark = SparkSession.builder.appName("EcommerceClickTimeAnalysis").getOrCreate()

df = spark.read.json("file:///mnt/c/Users/bhara/Desktop/ecom_project/logs/user_logs.json")
df.printSchema()
df.show(5)

# 1️⃣  Click frequency per action
click_summary = df.groupBy("action").agg(count("*").alias("total_clicks"))

# 2️⃣  Activity per hour
time_summary = (
    df.withColumn("hour", date_format(col("timestamp"), "HH"))
      .groupBy("hour")
      .agg(count("*").alias("clicks_per_hour"))
      .orderBy("hour")
)

# 3️⃣  Session duration stats (for "Session Ended" actions)
screen_time = (
    df.filter(col("action") == "Session Ended")
      .groupBy()
      .agg(
          count("*").alias("total_sessions"),
          avg(col("time_spent_seconds")).alias("avg_time_spent_seconds"),
          sum(col("time_spent_seconds")).alias("total_time_spent_seconds")
      )
)

# 4️⃣  Save results locally
click_summary.coalesce(1).write.csv(
    "file:///mnt/c/Users/bhara/Desktop/ecom_project/output_click_summary",
    header=True, mode="overwrite"
)

time_summary.coalesce(1).write.csv(
    "file:///mnt/c/Users/bhara/Desktop/ecom_project/output_time_summary",
    header=True, mode="overwrite"
)

screen_time.coalesce(1).write.csv(
    "file:///mnt/c/Users/bhara/Desktop/ecom_project/output_screen_summary",
    header=True, mode="overwrite"
)

print("\n✅ Analysis completed! Check output folders:")
print("   - output_click_summary/")
print("   - output_time_summary/")
print("   - output_screen_summary/")

spark.stop()

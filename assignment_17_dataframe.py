from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SalesDataFrame").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.csv("sales.csv", header=True, inferSchema=True)

# Sort by sales descending
sorted_df = df.orderBy(col("sales").desc())
print("All products sorted by sales (descending):")
sorted_df.show()

# Top 3 products
print("Top 3 products with highest sales:")
sorted_df.limit(3).show()

# Filter products with sales > 80000 and save as CSV
filtered = df.filter(col("sales") > 80000)
print("Products with sales > 80,000:")
filtered.show()
filtered.write.csv("high_sales_output", header=True, mode="overwrite")
print("Filtered results saved to high_sales_output/")

spark.stop()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PartitionDemo").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.range(5000000)

print("Initial number of partitions:", df.rdd.getNumPartitions())

df_repart = df.repartition(12)
print("After repartition(12):", df_repart.rdd.getNumPartitions())

df_coalesced = df_repart.coalesce(3)
print("After coalesce(3):", df_coalesced.rdd.getNumPartitions())

spark.stop()

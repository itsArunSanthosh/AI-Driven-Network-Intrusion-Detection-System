"""
Reads standardized flow data from Kafka and converts it into a Spark DataFrame.
"""

from pyspark.sql import SparkSession

def create_kafka_stream():
    spark = SparkSession.builder \
        .appName("FlowIngestionJob") \
        .getOrCreate()

    df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "standardized-flows") \
        .load()

    return df
"""
Writes computed features to feature store or Kafka.
"""

def write_to_sink(df):
    return df.writeStream \
        .format("console") \
        .start()
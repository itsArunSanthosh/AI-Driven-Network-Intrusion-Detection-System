def write_to_sink(df):
    return df.writeStream \
        .format("console") \
        .start()
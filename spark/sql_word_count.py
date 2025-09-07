import sys
from pyspark.sql.functions import split, explode, col
from pyspark.sql import SparkSession

def word_count(spark, filename: str):
    text_file = spark.read.text(filename)
    words_df = text_file.withColumn("word", explode(split(col("value"), " ")))
    return words_df.groupBy("word").count().orderBy("count", ascending=False)

if __name__ == '__main__':
    filename = "../data/hamlet.txt" if len(sys.argv) < 2 else sys.argv[1]
    spark = SparkSession.builder \
             .master("local[*]") \
             .appName('word_count') \
             .getOrCreate()
    result = word_count(spark, filename)
    result.show(10)
    spark.stop()
import sys

import pyspark
from pyspark.sql import SparkSession

def word_count(sc : pyspark.SparkContext, filename: str, k:int):
    ##
    text_file = sc.textFile(filename)
    counts = text_file.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda x, y: x + y)
    return (counts.map(lambda i: (i[1], i[0]))
            .sortByKey(ascending=False)
            .map(lambda i: (i[1], i[0]))
            .take(k))

if __name__ == '__main__':
    filename = "../data/hamlet.txt" if len(sys.argv) < 2 else sys.argv[1]
    spark = SparkSession.builder \
             .master("local[*]") \
             .appName('word_count') \
             .getOrCreate()
    result = word_count(spark.sparkContext, filename, 10)
    [print(r) for r in result]
    spark.stop()
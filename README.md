# Distributed Data Parallel Computing with Spark

This lab is a introduction to the Apache Spark framework for Data Parallel processing on
distributed environments.
We will be using it in the context of the Python programming language via the _pyspark_ module.

## Requirements

A Python (virtual) environment that includes the pyspark module.

* Python distribution (> 3.7)
* Java version 17 (you may try other versions, but it is not sure that it will work)
* PySpark. You may install it through _pip_
```
pip install pyspark
```

## Word Count Example 

Word counting is a fundamental text analysis process that calculates 
the total number of words in a given text. It’s widely used for 
monitoring document length and analyzing word frequency. 
It is also a common example of data processing, especially in 
distributed computing systems.

The process typically involves reading the input text, splitting it 
into words, and counting how many times each word appears.

### Example 

Input text:
``
Big data means big opportunities with big challenges.
``

Result: 
```
big → 3
data → 1
means → 1
opportunities → 1
with → 1
challenges → 1
```

### Code

You have three implementations to test and understand:

* sequential_word_count.py: Sequential Python implementation
* spark/rdd_word_count.py: PySpark implementation with the base RDD API.
* spark/sql_word_count.py: PySpark implementation with the SQL API.
* data: Data files

## Work To Do


## Documentation

* Spark: https://spark.apache.org/docs/latest/
* Spark RDD Programming Guide: https://spark.apache.org/docs/latest/rdd-programming-guide.html
* A simple Spark Tutorial: https://www.tutorialspoint.com/apache_spark/index.htm

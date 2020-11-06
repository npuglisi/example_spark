from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

sc = SparkContext('local')
spark = SparkSession(sc)
path = ".\\dataset"

def read_json():
    df = spark.read.json(path+"\\part-00000.json", multiLine = "false")
    """
    df = df.union(spark.read.json(path+"\\part-00001.json", multiLine = "false"))
    df = df.union(spark.read.json(path+"\\part-00002.json", multiLine = "false"))
    df = df.union(spark.read.json(path+"\\part-00003.json", multiLine = "false"))
    df = df.union(spark.read.json(path+"\\part-00004.json", multiLine = "false"))
    """
    return df

from objects.sessionamento import Sessionamento
from reading.read import read_json
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
import pyspark.sql.functions as F
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

df = read_json()

schema = StructType([
    StructField('agrupamento', StringType(), True),
    StructField('nome', StringType(), True),
    StructField('sessoes', IntegerType(), True)
    ])

result = StructType([
    StructField('', StringType(), True),
    StructField('', IntegerType(), True)
    ])

def to_sessionamento():
    lista = []
    section = 0

    dataFrame = df
    dataCollect = dataFrame.collect()
    firtsRows = dataFrame.limit(1)
    lastTime = int(firtsRows.select("device_sent_timestamp").collect()[0][0])
    nextTime = lastTime
    lastAnm = firtsRows.select("anonymous_id").collect()[0][0]

    for anm in dataCollect:

        if lastAnm != anm["anonymous_id"]:
            section = 0
            lastTime = int(anm["device_sent_timestamp"])

        nextTime = int(anm["device_sent_timestamp"])

        if (nextTime - lastTime) > 1800:
            section += 1
            lista.append(["browser_family",anm["browser_family"], section])
            lista.append(["os_family",anm["os_family"], section])
            lista.append(["device_family",anm["device_family"], section])
                    
        lastTime = nextTime   
        lastAnm = anm["anonymous_id"]         
    return spark.createDataFrame(lista, schema)

def sessionamento_browser():
    df_browser = to_sessionamento()    
    return df_browser.filter(df_browser["agrupamento"]=='browser_family').groupBy("nome").sum("sessoes")

def sessionamento_device():
    df_device = to_sessionamento()
    return df_device.filter(df_device["agrupamento"]=='device_family').groupBy("nome").sum("sessoes")
    
def sessionamento_os():
    df_os = to_sessionamento()
    return df_os.filter(df_os["agrupamento"]=='os_family').groupBy("nome").sum("sessoes")

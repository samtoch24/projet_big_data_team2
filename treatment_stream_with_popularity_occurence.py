import os
from time import sleep
import PyPDF2 as p
import pyspark
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from tempfile import tempdir
from pyspark import SparkFiles
from pyspark.shell import spark

# Path file
file_dir = "C:\\wamp64\\www\\projet_big_data_team2\\file"
file = "morenam.pdf"

# Lecture du fichier PDF
a = p.PdfFileReader(file_dir + "\\" + file)
texte = " "
for i in range(0, a.getNumPages()):
    texte = texte + a.getPage(i).extractText()
# print(texte)

# Creation de la session spark
spark = SparkSession.builder.appName("WordCount").config("spark.driver.bindAddress", "127.0.0.1").getOrCreate()

# Création du contexte spark
sc = spark.sparkContext()

# Création du contexte streaming
ssc = StreamingContext(sc, 1)

# flux entrant
rddQueue = []
for i in range(len(texte)):
    rddQueue += [ssc.sparkContext.parallelize(texte[i].replace(':', ' ').split(' '))]
inputStream = ssc.queueStream(rddQueue)

inputStream.map(lambda x: "mot: " + str(x)).pprint()

inputStream.map(lambda x: 1) \
    .reduce(lambda x, y: x + y) \
    .map(lambda x: str(x) + " mots reçus") \
    .pprint()

ssc.start()
sleep(10)
ssc.stop(stopSparkContext=True, stopGraceFully=True)

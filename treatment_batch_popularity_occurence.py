import os
import PyPDF2 as p
from pyspark.sql import SparkSession

# Chemin du fichier
file_dir = "C:\\wamp64\\www\\projet_big_data_team2\\file"

# Lecture du fichier PDF
file = "morenam.pdf"
a = p.PdfFileReader(file_dir + "\\" + file)
texte = " "
for i in range(0, a.getNumPages()):
    texte = texte + a.getPage(i).extractText()

# Liste des chemins vers les fichiers
file_list = os.listdir(file_dir)
file_list_path = [os.path.join(file_dir, f) for f in file_list]

# Analyse des fichiers

# Creation de la session spark
spark = SparkSession.builder.appName("Candidate's occurences").config("spark.driver.bindAddress",
                                                                      "127.0.0.1").getOrCreate()

# Initialisation du contexte
sc = spark.sparkContext

# Parrallélisation des traitements sur l'ensemble des fichiers
file_pdf = sc.parallelize(texte)

# Traitement batch avec spark
# CandidatWordcount = files.map(read_file).flatMap(lambda line: line.split(' ')).map(lambda word: (word, 1)).reduceByKey(
# lambda count1, count2: count1 + count2).collect()

Candidats = ["Trump", "Biden", "Samson", "Morena"]


# Fonction evaluation qui renvoie 0 si le nom d'un candidat apparait dans le fichier et 1 sinon
def mapEvaluation(word):
    return (word, int(not word in Candidats))


C_wordcount = file_pdf.flatMap(lambda line: line.split(' ')).map(mapEvaluation).reduceByKey(
    lambda count1, count2: count1 + count2).collect()
# for (word, count) in C_wordcount:
#     print(word, count)
# Liste des 5 mots les plus fréquents
for i in range(5):
    print(i, C_wordcount[i][0], C_wordcount[i][1])


# # Fonction evaluation qui renvoie 0 si le nom d'un candidat apparait dans le fichier et 1 sinon
# def mapEvaluation(word):
#     return (word, int(not word in Candidats))
#
#
# # Traitement batch avec spark
# CandidatWordcount = file_pdf.map(texte).flatMap(lambda line: line.split(' ')).map(mapEvaluation).reduceByKey(
#     lambda count1, count2: count1 + count2).collect()
#
# # Trie de la liste en fonction du nombre d’occurrences
# CandidatWordcount.sort(key=lambda v: -v[1])
#
# # Liste des 5 mots les plus fréquents
# for i in range(5):
#     print(i, CandidatWordcount[i][0], CandidatWordcount[i][1])

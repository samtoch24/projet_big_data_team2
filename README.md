Projet_Big_data_Team2
======================


## Projet de big data (Mars - Avril 2021)

Sujet:
Vous faites partie d'une équipe de campagne politique du parti de votre choix dans le pays de votre choix. 
Votre candidat souhaite mettre en place une analyse de données pour deux objectifs :
  - Le premier est d'être informé en temps réel des faits et gestes des autres candidats. 
   Ils veulent avoir un maximum d'informations sur les lieux, évènements ou les rencontres.
  - Le deuxième est de connaitre les tendances quotidiennes de votes et la popularité des candidats. 
   Quels sont les candidats qui occupent les médias ? De quels candidats tel ou tel média parle-t-il le plus ? etc.



## Participants : 
- NZUMGUENG Samson
- MORENA Lizanne
- EITEL Rostand
- TOUKAM Lindsey
- NZUTSEU Vaneck
- LEUNGA Reinna

## Creation & activation de l'environnement virtuel :
- python -m venv env
- .\env\Scripts\activate


## APIs (Swagger)
 - Informations sur les mouvements des autres candidats tels que leur position, les evenements, les rencotres et leur faits et geste en temps réel (Samson & vaneck)
 - Tendance quatidienne des votes (lindsey ey eitel)
 - popularité des candidats (morena et reinna)

## Librairies supplementaires en dehors de celle de tps
  - textract (pip install textract)
  - data.world (pip install datadotworld) & dw configure
  - flask_cors (pip install flask-cors-3.0.10)
  - PyPDF2 (pip install  PyPDF2)
  - motplotlib (pip install matplotlib==3.1.3)

## Pour connaitre les librairies deja installées : 
  - pip freeze 


# A Savoir : 
- Pour installer les packages : pip install -r requirements.txt
- Adresse du serveur de l'API : http://127.0.0.1:5000/v0.0.1/home/
- Documentation de l'API (interface du swagger) : http://127.0.0.1:5000/v0.0.1/docs/


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




### tiré du fichier "requirements.txt"
argon2-cffi==20.1.0
async-generator==1.10
attrs==20.3.0
backcall==0.2.0
beautifulsoup4==4.9.3
bleach==3.3.0
bs4==0.0.1
cffi==1.14.5
click==7.1.2
colorama==0.4.4
decorator==4.4.2
defusedxml==0.6.0
entrypoints==0.3
Flask==1.1.2
Flask-Cors==3.0.10
importlib-metadata==3.7.0
ipykernel==5.5.0
ipython==7.21.0
ipython-genutils==0.2.0
ipywidgets==7.6.3
itsdangerous==1.1.0
jedi==0.18.0
Jinja2==2.11.3
jsonschema==3.2.0
jupyter==1.0.0
jupyter-client==6.1.11
jupyter-console==6.2.0
jupyter-core==4.7.1
jupyterlab-pygments==0.1.2
jupyterlab-widgets==1.0.0
MarkupSafe==1.1.1
mistune==0.8.4
nbclient==0.5.3
nbconvert==6.0.7
nbformat==5.1.2
nest-asyncio==1.5.1
notebook==6.2.0
numpy==1.20.1
packaging==20.9
pandas==1.2.2
pandocfilters==1.4.3
parso==0.8.1
path==15.1.0
pickleshare==0.7.5
prometheus-client==0.9.0
prompt-toolkit==3.0.16
py4j==0.10.7
pycparser==2.20
Pygments==2.8.0
pymongo==3.11.3
pypandoc==1.5
pyparsing==2.4.7
pyrsistent==0.17.3
pyspark==2.4.7
python-dateutil==2.8.1
pytz==2021.1
pywin32==300
pywinpty==0.5.7
pyzmq==22.0.3
qtconsole==5.0.2
QtPy==1.9.0
selenium==3.141.0
Send2Trash==1.5.0
six==1.15.0
soupsieve==2.2
terminado==0.9.2
testpath==0.4.4
tornado==6.1
tqdm==4.58.0
traitlets==5.0.5
typing-extensions==3.7.4.3
urllib3==1.26.3
wcwidth==0.2.5
webencodings==0.5.1
Werkzeug==1.0.1
widgetsnbextension==3.5.1
zipp==3.4.0


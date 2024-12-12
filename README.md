# Backend API Prediction Image for MaggotIn App

## Cloud Computing Team 
| Student ID | Name | University |
| ------ | ------ | ------ |
|C296B4KY2742| Muhammad Arizaldi Eka Prasetya | Universitas Pembangunan Nasional "Veteran" Jawa Timur|
|C296B4KX0841|Berlian Viga Septiani| Universitas Pembangunan Nasional "Veteran" Jawa Timur|

## APIs Services
- Predict Maggot Image

## Project structure
```bash
PROJECT ROOT
├── app            
│   ├── server
│   │   ├── handler.py  
│   │   └── routes.py    
│   └── services
│       ├── inferenceServices.py       
│       ├── initModel.py    
│   	├── loadModel.py      
│      	└── storeData.py                                
├── myenv
├── .env                           
├── .gitignore                     
├── env.example                                  
└── requirements.txt                   

README.md
```
## Project setup

```bash
$ python --version

$ pip install virtualenv

$ virtualenv myenv

$ myenv\Scripts\activate

$ pip install flask
```
## Install Project Dependencies

```bash
$ pip install -r requirements.txt
```
## Run the Application

```bash
$ python app.py
```

## Deployment 

## Dependency
* [Flask](https://flask.palletsprojects.com/en/stable/)
* [TensorFlow](https://pypi.org/project/tensorflow/)
* [Flask-Cors](https://pypi.org/project/Flask-Cors/)
* [Python-DotEnv](https://pypi.org/project/python-dotenv/)
* [Mysql-Connector](https://pypi.org/project/mysql-connector-python/)

## Endpoint
- Predict
  <pre>POST /predict</pre>

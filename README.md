# Image Prediction API Backend for MaggotIn App
This project implements a backend API for image prediction of maggots. The application uses `Flask` for handling web requests and `TensorFlow` for the prediction model.

## Cloud Computing Team 
| Student ID | Name | University |
| ------ | ------ | ------ |
|C296B4KY2742| Muhammad Arizaldi Eka Prasetya | Universitas Pembangunan Nasional "Veteran" Jawa Timur|
|C296B4KX0841|Berlian Viga Septiani| Universitas Pembangunan Nasional "Veteran" Jawa Timur|

## APIs Services
- Predict Maggot Image

## Project Structure
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
## Project Setup

```bash
# check python version. if Python is not yet installed, you can download and install it from the https://www.python.org/
$ python --version

# install virtual environment
$ pip install virtualenv

# create virtual environment
$ virtualenv myenv

# for windows, activate use
$ myenv\Scripts\activate

# install flask
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
To set up and deploy the backend model application, first clone the source code from the specified GitHub repository and navigate to the project directory. Create a `Dockerfile` to define the container configuration details can be found at [.Dockerfile](./.Dockerfile). Ensure that the required Google Cloud APIs, including Artifact Registry, Cloud Build, and Cloud Run, are enabled. Next, create an Artifact Registry repository to store the Docker image. Build the container image using the `Dockerfile`, then upload it to Artifact Registry using the `gcloud builds submit` command. Finally, deploy the application to Cloud Run using the created container image for scalable and serverless hosting with the `gcloud run deploy` command.

## Endpoint
  <pre>POST /predict</pre>

- Testing uses Postman 
* Endpoint  : /predict
* Method    : POST
* Example Request

```
POST /predict
Content-Type: multipart/form-data

image: [maggot_image.jpg]

```
* Status Code  : 200
* Content Type : application/json
* Result Response
 
```
{
  "status": "true",
  "message": "Model is predicted successfully",
  "data": {
    "id": "e326e8e5-ce70-46e9-8369-f3dc6fd43740",
    "result": 5,
    "phase": "Prepupa",
    "confidenceScore": 76.68556213378906,
    "created_at": "2024-12-08T17:35:04.827625"
}

```
## Dependency
* [Flask](https://flask.palletsprojects.com/en/stable/)
* [TensorFlow](https://pypi.org/project/tensorflow/)
* [Flask-Cors](https://pypi.org/project/Flask-Cors/)
* [Python-DotEnv](https://pypi.org/project/python-dotenv/)
* [Mysql-Connector](https://pypi.org/project/mysql-connector-python/)

## License
This repository's source code is available under [MIT License](https://opensource.org/licenses/MIT).

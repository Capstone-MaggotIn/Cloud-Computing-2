# Image Prediction API Backend for MaggotIn App 🐛
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
├── app.py
├── myenv
├── .env                           
├── .gitignore                     
├── env.example                                  
└── requirements.txt                   

README.md
```
## Project Setup
If Python is not yet installed, you can download and install it from [![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org).

#### Install
```bash
# check python version
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
#### Clone Project

```bash
https://github.com/Capstone-MaggotIn/Cloud-Computing-2.git
```
#### Install Project Dependencies

```bash
$ pip install -r requirements.txt
```
## Run the Application
- Edit .env files and specify with your [env.examples](https://github.com/Capstone-MaggotIn/Cloud-Computing-2/blob/master/env.example)
- Run the app

```bash
$ python app.py
```

## Deployment
To set up and deploy the backend model application, first clone the source code from the specified GitHub repository and navigate to the project directory. Create a `Dockerfile` to define the container configuration details can be found at [Dockerfile](https://github.com/Capstone-MaggotIn/Cloud-Computing-2/blob/master/Dockerfile)
- Run the app. Ensure that the required Google Cloud APIs, including Artifact Registry, Cloud Build, and Cloud Run, are enabled. Next, create an Artifact Registry repository to store the Docker image. Build the container image using the `Dockerfile`, then upload it to Artifact Registry using the `gcloud builds submit` command. Finally, deploy the application to Cloud Run using the created container image for scalable and serverless hosting with the `gcloud run deploy` command.

## Endpoint
  <pre>POST /predict</pre>

### Request 
* Endpoint  : /predict
* Method    : POST
* Example Request

```
Content-Type: multipart/form-data

image: [maggot_image.jpg]

```
### Response
* Status Code  : '200'
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

## Resources
* [Planning costs via Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator?hl=en&dl=CjhDaVJtWldGaU16Y3lPUzFqWXpJekxUUTVOR1l0WVdFME5TMHpZelZtWWpBd016Z3lNR1FRQVE9PRAHGiRDRDFBRTI1My1FNjk5LTQ5QjMtOTU3NC1GNURBMkJDMjQ5QUU)
* [Cloud Architecture] (https://drive.google.com/file/d/1wp_0DqtgxlcqHYI-55JiAsqNzVaytXrJ/view?usp=sharing)
* [Flask Documentation] (https://flask.palletsprojects.com/en/stable/)

## License
This repository's source code is available under [MIT License](https://opensource.org/licenses/MIT).

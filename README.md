# Search-Box
A simple ITR(Information Retrievel System) using DRF(Django Rest Framework) and JS

## Steps to run the code 
### 1
Clone the repo using the command<br>
`git clone https://github.com/Himanshu372/Search-Box.git`<br>
on your local system<br>

### 2 
The application is contaierized.<br>
After cloning the repo, run the following command at the docker-compose-local.yml file level<br>
`docker-compose -f docker-compose-local.yml up web`<br>
This will start http-server and Django server at 8080 and 8000 ports respectively<br>
By accessing localhost:8080 on host machine, UI can be seen.<br>

### 3 
Downloading required packages from requirements.txt<br>
`pip install -r requirements.txt`<br>
This is download all the required packages to virtual env<br>

### 4 
Executing code<br>
Go the level where you can manage.py file is in the repo(which is the base level) and execute this command<br> 
`python manage.py runserver`<br>
This is will start the application in development envrionment<br>
### Open index.html from frontend folder in repo on any browser and you should be able to see this UI<br>
---

![](Advarisk_UI.PNG)

---

### 5
Executing custom management command<br> 
Keep the text data file at the level of manage.py and execute the command<br>
`python manage.py populate_db --filename`<br>
From the file database will get populated<br>

### 6
Executing tests<br>
For executing tests, use the following command at the 'backend' directory level inside the repo<br>
`./manage.py test backend.tests.{test_filename}`<br>

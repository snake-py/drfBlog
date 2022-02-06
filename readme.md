# DRF Blog

Shall be a simple blog api which can easily be set up with docker and docker-compose.

It has the option to create different users and assign different users different permissions. 

The system can be used headless of with an admin panel - for now only django admin panel  is available. 

# Current Set Up

```bash
virtualenv venv
```	
unix:
```bash	
source venv/bin/activate
```

or 

Windows

```bash	
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```	

```bash	
python manage.py migrate
```


```bash	
python manage.py runserver
```


## Start test suit 

requires nodemon installed 


unix: 

```bash	
nodemon --ext py --exec "source venv/bin/activate && python manage.py test"
```

windows:

```bash	
nodemon --ext py --exec "venv\Scripts\activate && python manage.py test"
```
Utilize coverage to get the test coverage report:

```bash	
coverage run manage.py test
```

```bash	
coverage report
```	
Get idea what needs more testing
```bash	
coverage html
```	
open the html report in the default browser - with live-server then you have also hot reload. 


Could all be done in one go:

```bash	
nodemon --ext py --exec "venv\Scripts\activate && coverage run manage.py test && coverage html"
```

# JSON Field Article

The example of how a json field can be used in the model. See the example <a href="./doc/article.json">json</a>
This Json could be parsed to the below html:
```html
<h1 class="test" id="test"><span id="main-title">Some title</span></h1>
<p class="test" id="test-p">Some text</p>
```	 
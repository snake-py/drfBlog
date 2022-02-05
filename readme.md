# DRF Blog

Shall be a simple blog api which can easily be set up with docker and docker-compose.

It has the option to create different users and assign different users different permissions. 

The system can be used headless of with an admin panel - for now only django admin panel  is available. 

# Set Up for now


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
nodemon --ext py --exec "venv\Scripts\activate && python manage.py test"
```

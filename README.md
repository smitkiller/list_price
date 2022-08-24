# list_price
search everthing by image and display price list

#Deploy
	#github
		git add .
		git commit -m "comment"
		git push
	#heroku
		heroku config:set DISABLE_COLLECTSTATIC=1
		git push heroku main
		heroku run python manage.py makemigrations
		heroku run python manage.py migrate
		heroku config:unset DISABLE_COLLECTSTATIC
		heroku run python manage.py collectstatic
		heroku open


list_price
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
│   ├── images
│   └── index.csv
├── mydatabase
├── myprice
│   ├── admin.py
│   ├── apps.py
│   ├── colordescriptor.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── searcher.py
│   ├── templates
│   │   ├── base.html
│   │   ├── data.html
│   │   ├── home.html
│   │   ├── navbar.html
│   │   ├── update.html
│   │   └── upload.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
├── static
└── staticfiles
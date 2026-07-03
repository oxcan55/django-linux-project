#!/bin/bash

git pull origin main 
source venv/bin/activate
python3 manage.py runserver
pip install -r requirements.txt
pyhton manage.py migrate
pyhton manage.py collectstatic

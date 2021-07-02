#!/bin/bash

source venv/bin/activate
cd /home/ubuntu/cbs-admin-system
git pull
pip install -r requirements.txt
python manage.py migrate
sudo systemctl restart uwsgi_cbs-admin-system.service
#!/bin/bash
#
# Description: Setup the database assuming we are on a system with Python 3 in a fresh virtual environment
#
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata oadb/fixtures/databases.yaml
./manage.py loaddata oadb/fixtures/systemuser.yaml
./manage.py importkits ../data/oadb_illumina_raw_data.csv --username system
./manage.py collectstatic --clear --noinput


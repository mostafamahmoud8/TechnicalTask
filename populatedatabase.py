import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','TechnicalTask.settings')

import django
# Import settings
django.setup()

from csv import reader
from datetime import datetime
from movies.models import Movies
 
with open("TechnicalTask/MovieDatasetLatest.csv",encoding="utf8",mode='r') as csvfile:
    csvreader = reader(csvfile)
    fields = next(csvreader)
    print(fields)
    for row in csvreader:
        Movies.objects.create(number=int(row[0]),title=row[1],release_date=datetime.strptime(row[2],'%m/%d/%Y'),overview=row[3],popularity=row[4],vote_average=float(row[5]),vote_num=int(row[6]))
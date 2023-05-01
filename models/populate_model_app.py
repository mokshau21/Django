import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','models.settings')
import django
django.setup()
## faker population script
from faker import Faker
from models_app.models import Topic,Webpage,AccessRecord
import random
fake=Faker()
topics=['Search','Social','MarketPlace','News','Games']
def add_topics():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        #get topic for entry
        top=add_topics()
        # create fake data for that entry
        fake_url=fake.url()
        fake_name=fake.company()
        fake_date=fake.date()
        # creating new object for each model
        webpg=Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
        webpg.save()
        acc=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
        acc.save()
print('Populating scripts')
populate(20)
print('Done Population')
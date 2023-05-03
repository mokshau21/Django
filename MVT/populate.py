import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MVT.settings')
import django
django.setup()
# faker script start from here
from faker import Faker
from mvt_app.models import Topic,Webpage,AccessRecord
import random
fake=Faker()
topics=['Search ','Social','Marketplace','News','Games']
def add_topiic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for i in range(N):
        top=add_topiic()
        name=fake.company()
        url=fake.url()
        date=fake.date()
        wpg=Webpage.objects.get_or_create(topic=top,name=name,url=url)[0]
        wpg.save()
        acc=AccessRecord.objects.get_or_create(name=wpg,date=date)[0]
        acc.save()
print("Populating scripts")
populate(20)
print("Done populating")
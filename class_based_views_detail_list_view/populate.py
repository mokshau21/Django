import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','class_based_views_detail_list_view.settings')
import django
django.setup()
from faker import Faker
import random
from cbv_detail_list_view.models import School,Student
fake=Faker()
def populate(N=20):
    for i in range(N):
        school_names=['Monarch Learning Center Charter School','Eastwood High School','Galaxy School','Granite Bay High School','Pine Hills International School']
        name=fake.name()
        principal_name=fake.name()
        school_name=random.choice(school_names)
        age=random.randint(12,19)
        location=fake.city()
        sch=School.objects.get_or_create(name=school_name,location=location,principal=principal_name)[0]
        sch.save()
        stu=Student.objects.get_or_create(name=name,school=sch,age=age)[0]
        stu.save()
populate()

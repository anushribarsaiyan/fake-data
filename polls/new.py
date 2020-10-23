import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newproject.settings')
import django

django.setup()

import random
from polls.models import user, activity
from faker import Faker

# instance for the Faker object
fakegen = Faker()


def dummy(N=5):
    for entry in range(N):
        # Create Fake Data for entry
        fake_id = fakegen.bothify(text='??#?##?##')
        fake_name = fakegen.name()
        fake_tz = fakegen.timezone()
        fake_date = fakegen.date_time_between()

        # Create new user Entry
        usr = user.objects.get_or_create(id=fake_id, real_name=fake_name, tz=fake_tz)[0]
        acty = activity.objects.get_or_create(user_activity=usr, start_time=fake_date, end_time=fake_date)[0]


if __name__ == '__main__':
    print("Creating dummy data...Please Wait")
    dummy(10)
    print('dummy data successfully added')

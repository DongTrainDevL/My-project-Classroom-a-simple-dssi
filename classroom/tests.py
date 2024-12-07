from django.test import TestCase
from classroom.models import *

# Create your tests here.
if __name__ == '__main__':
    for c in Course.objects.all():
        print(c.id, c.subj_name)          
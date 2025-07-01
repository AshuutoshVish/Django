from mongoengine import Document, StringField, IntField, EmailField, DecimalField, DateTimeField
from datetime import datetime

class Employee(Document):
    name = StringField(max_length=50, required=True)
    age = IntField(min_value=18, max_value=65, required=True)
    position = StringField(max_length=50)
    salary = DecimalField(precision=2)
    email = EmailField(required=True, unique=True)
    date_joined = DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.name
    meta = {
        'collection': 'employees',
        'indexes': ['name', 'email']
    }
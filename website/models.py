from django.db import models as ml

class Record(ml.Model):
    created_at = ml.DateTimeField(auto_now_add=True)
    first_name = ml.CharField(max_length=50)
    last_name = ml.CharField(max_length=50)
    email = ml.CharField(max_length=100)
    phone = ml.CharField(max_length=15)
    address = ml.CharField(max_length=100)
    city = ml.CharField(max_length=50)
    state = ml.CharField(max_length=50)
    zipcode = ml.CharField(max_length=20)
    

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

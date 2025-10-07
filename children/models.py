from django.db import models

# Create your models here.
from django.db import models


class ChildrenInfo(models.Model):
    img = models.ImageField(upload_to='children_images/', blank=True, null=True)  # For storing image
    address = models.TextField()
    details = models.TextField()
    person_name = models.CharField(max_length=100)
    person_contact = models.CharField(max_length=15)
    is_safe = models.BooleanField(default=False)

    STATE_CHOICES = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CG', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OD', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TS', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
        ('DL', 'Delhi'),
        ('JK', 'Jammu and Kashmir'),
        ('LD', 'Ladakh'),
        ('PY', 'Puducherry'),
        ('CH', 'Chandigarh'),
    ]

    city = models.CharField(max_length=50, default="Indore")
    state = models.CharField(max_length=50, choices=STATE_CHOICES, default="MP")
    country = models.CharField(max_length=50, default="India")
    pincode = models.CharField(max_length=15, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)      

    def __str__(self):
        return f"{self.person_name}"

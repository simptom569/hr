from django.db import models
from uuid import uuid4

# Create your models here.
class Userss(models.Model):

    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_age = models.CharField(max_length=50)
    user_name = models.CharField(max_length=150)
    user_login = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=20)
    user_email = models.EmailField()
    user_gender = models.CharField(max_length=10)
    user_avatar = models.ImageField(upload_to="main/images/")
    user_cv = models.FileField(upload_to=f"main/documents/")
    user_category = models.CharField(max_length=50)

    class Meta:
        db_table = "Users"
        verbose_name = "Вакансии"
    
    def __str__(self):
        return self.user_name



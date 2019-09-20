from django.db import models

# Create your models here.
class userInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_first_name = models.CharField(max_length=15,null=False)
    user_last_name = models.CharField(max_length=15, null=False)
    user_email = models.CharField(max_length=50,null=False)
    user_phone = models.IntegerField(null=False)
    user_password = models.CharField(max_length=51,null=False)

    def __str__(self):
        return f"{self.user_first_name} and {self.user_email}  {self.user_phone} is awesome {self.user_last_name} "
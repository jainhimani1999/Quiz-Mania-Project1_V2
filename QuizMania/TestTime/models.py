from django.db import models
from login_register.models import userInfo
# Create your models here.


# Create your models here.
class testInfo(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=100,null=False)
    test_file = models.CharField(max_length=100,null=False)
    Max_score = models.IntegerField(null=False)

    def __str__(self):
        return f"Id: {test_id} Name: {test_name} Test File: {test_file} Max Score: {Max_score}"
    
class userScore(models.Model):
    score = models.IntegerField(null=False)
    user_id = models.ForeignKey(userInfo,on_delete=models.CASCADE,related_name="UserId")
    test_id = models.ForeignKey(testInfo,on_delete=models.CASCADE,related_name="TestId")

    def __str__(self):
        return f"You Scored: {score}"

class testQuestions(models.Model):
    ques_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100,null=False)
    option1 = models.CharField(max_length=100,null=False)
    option2 = models.CharField(max_length=100,null=False)
    option3 = models.CharField(max_length=100,null=False)
    option4 = models.CharField(max_length=100,null=False)

    def __str__(self):
        return f'''Question no: {ques_id} : {question}
        1. {option1}
        2. {option2}
        3. {option3}
        4. {option4}
        '''
        
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    mobile = models.IntegerField()
    plans = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.name
class Plan(models.Model):
    userfor=models.ForeignKey(User,on_delete=models.CASCADE,related_name='userfor')
    plan_name = models.CharField(max_length=70,null=True,blank=True)
    amount = models.IntegerField()
    discount = models.CharField(max_length=60,null=True,blank=True)
    def __str__(self):
        return self.plan_name
class Previous_Plans(models.Model):
    planfor = models.ForeignKey(Plan,on_delete=models.CASCADE,related_name='planfor')
    uerfors = models.ForeignKey(User,on_delete=models.CASCADE,related_name='uerfors')
    date = models.DateField()
    transection_id = models.CharField(max_length=40,null=True,blank=True)
    staus = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        return str(self.planfor)
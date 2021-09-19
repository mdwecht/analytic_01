from django.db import models

# Create your models here.
class Params(models.Model):
    analytic = models.CharField(max_length=20)
    var_01 = models.IntegerField(default=0)
    var_02 = models.IntegerField(default=0)
    var_03 = models.IntegerField(default=0)

    def __str__(self):
        return self.analytic
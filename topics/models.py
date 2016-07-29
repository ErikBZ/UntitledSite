from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Yes I am creating my models here

class Topic(models.Model):
    topic_text = models.CharField(max_length = 300)
    description_text = models.TextField(max_length=400, default="Put description here")
    pub_date = models.DateTimeField('Date Posted')
    number_of_replies = models.IntegerField(default=0)
    user_who_posted = models.ForeignKey(User, on_delete=models.CASCADE)

    def __rep__(self):
        return "%s:\n\t%s" %(self.user_who_posted.get_username(), self.topic_text)

    def __str__(self):
        return self.__rep__()

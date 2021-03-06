from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Yes I am creating my models here

class Topic(models.Model):
    topic_max_length = 300
    topic_text = models.CharField(max_length = topic_max_length)

    desc_max_length = 2000
    description_text = models.TextField(max_length=desc_max_length, default="Put description here")

    pub_date = models.DateTimeField('Date Posted')
    number_of_replies = models.IntegerField(default=0)
    user_who_posted = models.ForeignKey(User, on_delete=models.CASCADE)

    def __rep__(self):
        return "%s:\n\t%s" %(self.user_who_posted.get_username(), self.topic_text)

    def __str__(self):
        return self.__rep__()

class Reply(models.Model):
    user_who_posted = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_in_reply = models.ForeignKey(Topic, on_delete=models.CASCADE)
    reply_in_response = models.ForeignKey("self", on_delete=models.CASCADE)
    replies_to_this = models.ManyToManyField("self")

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topics_posted = models.ManyToManyField(Topic)
    replies_posted = models.ManyToManyField(Reply)


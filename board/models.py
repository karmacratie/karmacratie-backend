from django.db import models
from django.contrib.auth.models import User

class Ministry(models.Model):
    name = models.CharField("Nom du ministere", max_length=128, blank=False, null=False, unique=True)
    description = models.CharField("Description du ministère", max_length=1024, blank=False, null=False)
    admin = models.ForeignKey(User)

class Cycle(models.Model):
    CYCLE_TYPE = (
            (1, 'Premier débat'),
            (2, 'Seconde lecture'),
            (3, 'Vote'),)
    type = models.PositiveIntegerField(choices=CYCLE_TYPE, blank=False, null=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=False, null=False)
    active = models.BooleanField(default=True)
    next_cycle = models.ForeignKey(Cycle, null=True, blank=True)

class Post(models.Model):
    owner = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now_add=True)
    parent_post = models.ForeignKey(Post)
    parent_ministry = models.ForeignKey(Ministry)
    title = models.CharField("Titre de votre contribution", blank=False, null=False)
    content = models.CharField("Contenu de votre contribution", blank=False, null=False)
    votes = models.ManyToManyField(Vote)
    cycle = models.ForeignKey(Cycle)
    

class Karma(models.Model):
    user = models.ForeignKey(User)
    ministry = models.ForeignKey(Ministry)
    score = models.IntegerField(default=0, null=False, blank=False)

    class Meta:
        unique_together = ('user','ministry')

class Vote(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    instant_karma = models.IntegerField(blank=False, null=False)
    vote = models.IntegerField(blank=False, null=False)
    note = models.IntegerField(blank=False, null=False)

    class Meta:
        unique_together = ('post','user')


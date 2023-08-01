# api/models.py
from django.db import models
from django.contrib.auth.models import User

class Hackathon(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hackathons/')
    hackathon_image = models.ImageField(upload_to='hackathons/')
    SUBMISSION_TYPES = [
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    ]
    type_of_submission = models.CharField(max_length=5, choices=SUBMISSION_TYPES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    
    @classmethod
    def get_all_hackathons(cls):
        return cls.objects.all()

class Submission(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    summary = models.TextField()
    submission = models.FileField(upload_to='submissions/')
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @classmethod
    def get_user_submissions(cls, user):
        return cls.objects.filter(user=user)
    
    @classmethod
    def get_hackathon_user_submissions(cls, hackathon, user):
        return cls.objects.filter(hackathon=hackathon, user=user)

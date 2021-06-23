from django.db import models



class Subscribers(models.Model):
    email = models.CharField(max_length=128, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    en_title = models.CharField(max_length=128, blank=False, null=False)
    uz_title = models.CharField(max_length=128, blank=False, null=False)
    en_description = models.TextField(blank=False, null=False)
    uz_description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="image/", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Icon(models.Model):
    en_title = models.CharField(max_length=128, blank=False, null=False)
    uz_title = models.CharField(max_length=128, blank=False, null=False)
    en_comment = models.TextField(blank=False, null=False)
    uz_comment = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="image/", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    en_full_name = models.CharField(max_length=128, blank=False, null=False)
    en_comment = models.TextField(blank=False, null=False)
    uz_comment = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="image/", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models


class Region_Category(models.Model):
    name = models.CharField(max_length=50)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()


class Region(models.Model):
    region_category = models.ForeignKey(Region_Category,
                                        on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()


class User_Query(models.Model):
    region = models.ForeignKey(Region,
                               on_delete=models.CASCADE)
    user_id = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()


class Publishing_Organization(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()


class Article(models.Model):
    title = models.CharField(max_length=500)
    content_link = models.CharField(max_length=500)
    thumbnail_link = models.CharField(max_length=500)
    publishing_organization = models.ForeignKey(Publishing_Organization,
                                                on_delete=models.CASCADE)
    published_on = models.DateTimeField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()


class Article_Staging(models.Model):
    title = models.CharField(max_length=500)
    content_link = models.CharField(max_length=500)
    thumbnail_link = models.CharField(max_length=500)
    publishing_organization = models.ForeignKey(Publishing_Organization,
                                                on_delete=models.CASCADE)
    published_on = models.DateTimeField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

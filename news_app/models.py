from django.db import models


class Region_Category(models.Model):
    name = models.CharField(max_length=500)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()


class Region(models.Model):
    region_category = models.ForeignKey(Region_Category,
                                        on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    geo_id = models.CharField(max_length=500, null=True)
    state_number = models.IntegerField(null=True)
    census_area = models.DecimalField(max_digits=20,
                                      decimal_places=10,
                                      null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()


class User_Query(models.Model):
    region = models.ForeignKey(Region,
                               on_delete=models.CASCADE)
    user_id = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()


class Publishing_Organization(models.Model):
    name = models.CharField(max_length=500)
    abbreviation = models.CharField(max_length=10, default=None)
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

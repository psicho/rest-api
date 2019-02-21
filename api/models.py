from django.db import models


class ThreeInner(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)


class TwoInner(models.Model):
    name = models.CharField(max_length=500)
    children = models.ManyToManyField(ThreeInner, related_name='children_three')

    def __str__(self):
        return str(self.name)


class OneInner(models.Model):
    name = models.CharField(max_length=500)
    children = models.ManyToManyField(TwoInner, related_name='children_two')

    def __str__(self):
        return str(self.name)


class TopModel(models.Model):
    name = models.CharField(max_length=500)
    children = models.ManyToManyField(OneInner, related_name='children_one')

    def __str__(self):
        return str(self.name)


class Models(models.Model):
    name = models.CharField(max_length=500, verbose_name='Name')
    children = models.ManyToManyField("self", blank=True, verbose_name='children')

    def __str__(self):
        return str(self.name)

from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):

    name = models.CharField(max_length=200,null=True,blank=True)
    title = models.CharField(max_length=300,null=True,blank=True)
    body = models.TextField()
    # category = models.CharField(max_length=100,null=True,blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class ProjectFile(models.Model):

    project_name = models.ForeignKey(Project,on_delete=models.CASCADE)
    file = models.FileField(upload_to ='files/')

    def __str__(self):
        return self.project_name.title
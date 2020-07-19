from django.db import models

class AuthorModel(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.first_name+' '+self.last_name


class BlogModel(models.Model):
    blogs = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 
    author = models.ForeignKey(AuthorModel, on_delete= models.CASCADE)

    def __str__(self):
        return self.blogs

    


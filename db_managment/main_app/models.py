from django.db import models

# Create your models here.

class Stacks(models.Model):
    name = models.CharField(max_length=100, unique=True)
    stars = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return str(self.name)
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="students")
    
    
    def __str__(self):
        return str(self.name)



class Rating(models.Model):
    value = models.PositiveIntegerField(defaoult=0)
    article = models.ForeignKey(Article,  on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='post_comment')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    comment = models.TextField()
    
    def __str__(self):
        return str(self.name)


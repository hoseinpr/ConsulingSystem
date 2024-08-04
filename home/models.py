from django.db import models
from django.contrib.auth.models import AbstractUser


class Moshaver(models.Model):
    MoshaverID = models.IntegerField()
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    Madrak = models.CharField(max_length=50)
    
class Courses(models.Model):
    CourseID = models.IntegerField()
    Title = models.CharField(max_length=20)
    description = models.CharField(max_length=200, default='نامشخص')
    Moshaver = models.CharField(max_length=20, default='نامشخص')
    Course_Number = models.IntegerField()
    Price = models.IntegerField()

class Person(AbstractUser):
    phone = models.CharField(max_length=50)
    school_name = models.CharField(max_length=50)
    study = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    person_id = models.CharField(max_length=50)
    gpa = models.CharField(max_length=50)

# class User(models.Model):
#     Username = models.CharField(max_length=50)
#     Password = models.IntegerField()
#     PersonID = models.IntegerField()
#     Fname = models.CharField(max_length=50)
#     Lname = models.CharField(max_length=50)
#     Phone = models.IntegerField()
#     School_Name = models.CharField(max_length=50)
#     Study = models.CharField(max_length=50)
#     Degree = models.CharField(max_length=50)
#     GPA = models.CharField(max_length=50)
#     def __str__(self):
#         return f"{self.Fname} {self.Lname}"
    
class Course_has_Moshaver(models.Model):
    MoshaverID = models.ForeignKey(Moshaver, on_delete=models.PROTECT)
    CourseID = models.ForeignKey(Courses, on_delete=models.PROTECT)
  
class Courses_has_User(models.Model):
    PersonID = models.ForeignKey(Person, on_delete=models.PROTECT)
    CourseID = models.ForeignKey(Courses, on_delete=models.PROTECT)

#------------------------------------------------------------------------


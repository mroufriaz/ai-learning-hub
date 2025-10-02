from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    DURATION_CHOICES = [
        ('1m', '1 Month'),
        ('3m', '3 Months'),
        ('6m', '6 Months'),
        ('1y', '1 Year'),
    ]

    title = models.CharField(max_length=200)
    short_description = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="courses")
    duration = models.CharField(max_length=10, choices=DURATION_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    instructor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="courses/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-created_at']




class CoursePoint(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="points")
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.course.title} - {self.text[:30]}"

    class Meta:
        verbose_name_plural = "Course Points"
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="FontAwesome icon class (e.g., 'fas fa-robot')")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=80, help_text="Skill percentage (0-100)")
    category = models.CharField(max_length=100, choices=[
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('AI & Automation', 'AI & Automation'),
        ('Other', 'Other'),
    ])

    def __str__(self):
        return self.name

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"

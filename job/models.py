from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    job_type = models.CharField(
        max_length=50,
        choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract')]
    )
    status = models.CharField(
        max_length=50,
        choices=[('active', 'Active'), ('closed', 'Closed')]
    )
    description = models.TextField(blank=True, null=True)
    class Meta:
        app_label = 'job'  # Explicitly setting the app_label
    def __str__(self):
        return self.title
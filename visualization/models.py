from django.db import models

class Dataset(models.Model):
    heading = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    data = models.CharField(max_length=255)
    sort_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.heading} ({self.data})"



class Entity(models.Model):
    dataset = models.ForeignKey("Dataset", on_delete=models.CASCADE, related_name="entities")
    name = models.CharField(max_length=255)
    volume = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="entities/", blank=True, null=True)  # <-- changed

    def __str__(self):
        return self.name



class Detail(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="details")
    details = models.TextField()   # single field, can hold plain text or JSON

    def __str__(self):
        return self.details[:50]   # show preview

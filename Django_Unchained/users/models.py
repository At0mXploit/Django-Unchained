from django.db import models
from django.contrib.auth.models import User
from PIL import Image 

class Profile(models.Model):
    # One-to-one relationship: Each user has exactly one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Profile picture with default image and custom upload directory
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Override save method to resize large images
    def save(self, *args, **kwargs):  
        # Call the parent class save method first
        super().save(*args, **kwargs)  
        
        
        img = Image.open(self.image.path)

        # Check if image dimensions exceed 300px
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            
            img.thumbnail(output_size)
            
            img.save(self.image.path)
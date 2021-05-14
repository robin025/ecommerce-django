from django.db import models

# Create your models here.
class BlogContact(models.Model):
    contact_id_blog = models.AutoField(primary_key=True)
    contact_name_blog = models.CharField(max_length=50)
    contact_email_blog = models.CharField(max_length=100)
    contact_phone_blog = models.CharField(max_length=15)
    contact_desc_blog = models.CharField(max_length=1000)

    def __str__(self):
        return self.contact_name_blog

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_tile = models.CharField(max_length=50)
    head1 = models.CharField(max_length=100,default="")
    head2 = models.CharField(max_length=100,default="")
    head3 = models.CharField(max_length=100,default="")
    text_head1 = models.CharField(max_length=5000,default="")
    text_head2 = models.CharField(max_length=5000,default="")
    text_head3 = models.CharField(max_length=5000,default="")
    publish_date = models.DateField()
    thumbnail = models.ImageField(upload_to="blog/images",default="")

    def __str__(self):
        return self.post_tile

    


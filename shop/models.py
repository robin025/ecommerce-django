from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField  
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    category = models.CharField(max_length=100,default="")
    sub_category = models.CharField(max_length=100,default="")
    price = models.IntegerField(default=0)
    prod_img = models.ImageField(upload_to="shop/images",default="")

    pub_date = models.DateField()


    def __str__(self):
        return self.product_name

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=50)
    contact_email = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=15)
    contact_desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.contact_name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    # amount = models.IntegerField(default="")
    items_json = models.CharField(max_length=1000)
    order_name = models.CharField(max_length=100)
    order_email = models.CharField(max_length=100)
    order_phone = models.CharField(max_length=20)
    order_address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    



    def __str__(self):
        return self.order_name

class OrderInfo(models.Model):
    update_id = models.AutoField(primary_key = True)
    order_id = models.IntegerField(default="")
    order_desc = models.CharField(max_length=10000)
    timestamp = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.order_desc[0:10] + "......"
        


    




    
        
    



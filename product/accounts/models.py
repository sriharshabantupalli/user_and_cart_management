from django.db import models

class User(models.Model):
    objects = None
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    is_customer = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number

class UserProfileModel(models.Model):
    objects = None
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHERS', 'Others'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class UserLoginTopModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.owner)

class ProductMainModel(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    unique_id = models.CharField(max_length=8, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

class ProductImageModel(models.Model):
    objects = None
    product = models.ForeignKey(ProductMainModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.owner = None

    def __str__(self):
        return f"{self.owner}: {self.product.title if self.product else 'No product selected'}"

class UserCartProductModel(models.Model):
    objects = None
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductMainModel, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.owner.phone_number}: {self.product.title if self.product else 'No product selected'}"

class UserCartModel(models.Model):
    objects = None
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(UserCartProductModel, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return str(self.owner)
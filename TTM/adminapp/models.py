from django.db import models


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "admin_table"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Use a password hashing library for storage
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "user_table"


class Destination(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='destination_images')  # Store images locally

    class Meta:
        db_table = "destination_table"


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='hotel_images')  # Store images locally
    star_rating = models.IntegerField()
    address = models.CharField(max_length=255)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    class Meta:
        db_table = "hotel_table"


class Airport(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)  # Example: IATA or ICAO code


class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    airline = models.CharField(max_length=255)
    flight_number = models.CharField(max_length=10)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departing_flights')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arriving_flights')
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "flight_table"


class Package(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "package_table"


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Ensure data integrity
    package = models.ForeignKey('Package', on_delete=models.SET_NULL, null=True, blank=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True, blank=True)
    flight = models.ForeignKey('Flight', on_delete=models.SET_NULL, null=True, blank=True)
    travel_date = models.DateField()
    number_of_people = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "bookings_table"


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Ensure data integrity
    destination = models.ForeignKey('Destination', on_delete=models.SET_NULL, null=True, blank=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField()
    comment = models.TextField()

    class Meta:
        db_table = "review_table"

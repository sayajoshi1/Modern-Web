from django.db import models
#---------------------------------------------------------user model---------------------------------------------------------------------------------------------
class User(models.Model):
	id=models.AutoField(auto_created=True,primary_key=True)
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	image=models.ImageField(default="img.jpg")
	contactno=models.CharField(max_length=50, null=True)
	class Meta:
		db_table="user"

#---------------------------------------------------------Packages model------------------------------------------------------------
class Packages(models.Model):
	id=models.AutoField(auto_created=True,primary_key=True)
	name=models.CharField(max_length=50)
	image=models.ImageField(default="img.jpg")
	description=models.TextField(blank= True)
	price=models.CharField(max_length=50)
	
	class Meta:
		db_table="packages"

#-----------------------------------------------------------Booking model------------------------------------------------------------------
class Bookings(models.Model):
	id=models.AutoField(auto_created=True,primary_key=True)
	packages=models.ForeignKey(Packages,on_delete=models.CASCADE, null=True, default=None)
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	contactno=models.CharField(max_length=50)
	date=models.CharField(max_length=50)
	address=models.CharField(max_length=50)
	numberofpeople=models.IntegerField(null=False)
	class Meta:
		db_table="bookings"

# class Reviews(models.Model):
# 	name=models.CharField(max_length=50)
# 	packages=models.ForeignKey(Packages,on_delete=models.CASCADE, null=True, default=None)
# 	review=models.TextField(blank= True)
# 	class Meta:
# 		db_table="reviews"

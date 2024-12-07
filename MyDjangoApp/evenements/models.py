from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
  name=models.CharField('Venue name', max_length=120)
  address=models.CharField(max_length=300)
  zip_code=models.CharField('Post Code', max_length=15)
  phone=models.CharField('Contact Phone', max_length=25,blank=True)
  web=models.URLField('Website Address',blank=True)
  email_address= models.EmailField('Email Address',blank=True)
  
  image = models.ImageField(upload_to='venues/', blank=True)

  owner = models.IntegerField('Venue_Owner', blank=False,default=1)
  
  def __str__(self):
        return self.name



class MonClubUser(models.Model):
    first_name=models.CharField( max_length=30)
    last_name=models.CharField( max_length=30)
    email=models.EmailField('User Email')
    
    
    def __str__(self):
      return self.first_name + ' ' + self.last_name




class Evenement(models.Model):
    name =models.CharField('Evenement name', max_length=120)
    evenement_date=models.DateTimeField('Evenement date')
    venue=models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager= models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description= models.TextField(blank=True)
    attendees= models.CharField(User, max_length=120, blank=True)
    approved= models.BooleanField('Approved', default=False)
    
    
    def __str__(self):
        return self.name
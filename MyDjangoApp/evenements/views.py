from urllib import request
from django.shortcuts import redirect, render
import calendar 
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib import messages
from .models import Evenement, Venue
from .forms import VenueForm , EvenementForm,EvenementFormAdmin
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



def admin_approval(request):
  evenement_list=Evenement.objects.all()
  if request.user.is_superuser:
      if request.method=="POST":
        id_list=request.POST.getlist('boxes')
        
        #uncheck all events
        evenement_list.update(approved=False)
        
        #update the data base
        for x in id_list:
          Evenement.objects.filter(pk=int(x)).update(approved=True)
        
        
        
        messages.success(request, 'Selected events have been approved')
        return redirect('list-evenements')
      else:
        return render(request, 'evenements/admin_approval.html', 
        {"evenement_list": evenement_list,
        })
  else:
    messages.success(request, 'You are not authorized to view this page')
    return redirect('home')












def evenement_pdf(request):
  if request.user.is_superuser:
    buf = io.BytesIO()
    c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
    texttob= c.beginText()
    texttob.setTextOrigin(inch, inch)
    texttob.setFont("Helvetica", 14)
    
    evenements=Evenement.objects.all()
    lines=[]
    
    for evenement in evenements:
      lines.append(evenement.name)
      lines.append(evenement.venue.name)
      lines.append(evenement.manager.username)
      lines.append(evenement.evenement_date.strftime('%Y-%m-%d %H:%M:%S'))
      lines.append(evenement.description)
      lines.append("=====================================")
      
    for line in lines:
      texttob.textLine(line)  
      
    c.drawText(texttob)
    c.showPage()
    c.save() 
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename='evenement.pdf')
  else:
    messages.success(request, 'You are not authorized to make this task')
    return redirect('home')









def my_evenements(request):
  if request.user.is_authenticated:
    me=request.user
    evenements=Evenement.objects.filter(manager=me)
    return render(request, 'evenements/my_evenements.html', {
      "evenements": evenements})
  else:
    messages.success(request, 'You are not authorized to view this page')
    return redirect('home')





def delete_venue(request, venue_id):
  venue = Venue.objects.get(pk=venue_id)
  venue.delete()
  return redirect('list-venues')




def delete_evenement(request, evenement_id):
  evenement = Evenement.objects.get(pk=evenement_id)
  if request.user == evenement.manager or request.user.is_superuser:
    evenement.delete()
    messages.success(request, 'Evenement deleted successfully')
    return redirect('list-evenements')

  else:
    messages.error(request, 'You are not allowed to delete this event')
    return redirect('list-evenements')






def update_evenement(request, evenement_id):  
  evenement = Evenement.objects.get(pk=evenement_id)
  if request.user.is_superuser:
    form=EvenementFormAdmin(request.POST or None,instance=evenement)
  else:  
    form=EvenementForm(request.POST or None,instance=evenement)
  
  if form.is_valid():
    form.save()
    return redirect('list-evenements')
  
  return render(request, 'evenements/update_evenement.html', 
        {'evenement': evenement,'form': form})






def add_evenement(request):
  submitted = False
  if request.method == 'POST':
    if request.user.is_superuser:
      form = EvenementFormAdmin(request.POST)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect('/evenements?submitted=True')
      
    else:
      form = EvenementForm(request.POST)
      
      
      if form.is_valid():
          event = form.save(commit=False)
          event.manager = request.user
          event.save()
          return HttpResponseRedirect('/evenements?submitted=True')
  else:
    if request.user.is_superuser:
      form = EvenementFormAdmin
    else:
      form = EvenementForm
    if 'submitted' in request.GET:
      submitted = True
  return render(request, 'evenements/add_evenement.html', {'form': form , 'submitted': submitted})






def update_venue(request, venue_id):  
  venue = Venue.objects.get(pk=venue_id)
  form=VenueForm(request.POST or None,instance=venue)
  if form.is_valid():
    form.save()
    return redirect('list-venues')
  
  return render(request, 'evenements/update_venue.html', 
        {'venue': venue,'form': form})




def search_venues(request):
  if request.method == 'POST':
    search_text = request.POST['searched']
    venues = Venue.objects.filter(name__icontains=search_text)
    
    return render(request, 'evenements/search_venues.html', {'venues': venues, 'searched': search_text})
  else:
    return render(request, 'evenements/search_venues.html', {})
  



def show_venue(request, venue_id):
  venue = Venue.objects.get(pk=venue_id)
  venue_owner = User.objects.get(pk=venue.owner)
  return render(request, 'evenements/show_venue.html', 
        {"venue": venue,
        "venue_owner": venue_owner,})




def list_venues(request):
  venue_list = Venue.objects.all()
  return render(request, 'evenements/venue.html', 
        {"venue_list": venue_list,
  })


def add_venue(request):
  submitted = False
  if request.method == 'POST':
    form = VenueForm(request.POST)
    if form.is_valid():
      venue = form.save(commit=False)
      venue.owner = request.user.id
      venue.save()
      return HttpResponseRedirect('/add_venue?submitted=True')
  else:
    form = VenueForm
    if 'submitted' in request.GET:
      submitted = True
  return render(request, 'evenements/add_venue.html', {'form': form , 'submitted': submitted})





def all_evenements(request):
  evenement_list = Evenement.objects.all().order_by('name')
  return render(request, 'evenements/evenement_list.html', 
        {"evenement_list": evenement_list,
  })

  



@login_required (login_url='login')
def home(request,year=datetime.now().year,month=datetime.now().strftime('%B')):

  month = month.title()
  #convert month from name to number
  month_number=list(calendar.month_name).index(month)
  month_number = int(month_number)
  
  
  #create a calendar
  cal = HTMLCalendar().formatmonth(year, month_number)
  
  #Get current year
  now = datetime.now()
  current_year = now.year
  
  #Get current time
  time=now.strftime('%I:%M:%S ')
  
  
  
  
  return render(request,
    'evenements/home.html', {
    
    "year": year,
    "month": month,
    "month_number": month_number,
    "cal": cal,
    "current_year": current_year,
    "current_time": time,
    
  })
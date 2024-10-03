from django.urls import   path
from . import views


urlpatterns = [
    #int : numbers
    #str: string 
    #path : whole utls/
    #slug:hyphen-and-underscores_stuff
    #UUID: universal unique identifier
    
    
  path('', views.home, name="home"),
  path('<int:year>/<str:month>', views.home, name="home"),
  path('evenements', views.all_evenements, name="list-evenements"),
  path('add_venue', views.add_venue, name="add-venue"),
  path('list_venues', views.list_venues, name="list-venues"),
  path('show_venue/<venue_id>', views.show_venue, name="show-venue"),
  path('search_venues', views.search_venues, name="search-venues"),
  path('update_venue/<venue_id>', views.update_venue, name="update-venue"),
  path('add_evenement', views.add_evenement, name="add-evenement"),
  path('update_evenement/<evenement_id>', views.update_evenement, name="update-evenement"),
  path('delete_evenement/<evenement_id>', views.delete_evenement, name="delete-evenement"),
  path('delete_venue/<venue_id>', views.delete_venue, name="delete-venue"),
  path('my_evenements', views.my_evenements, name="my-evenements"),
  path('evenement_pdf', views.evenement_pdf, name="evenement_pdf"),
  path('admin_approval', views.admin_approval, name="admin_approval"),
]
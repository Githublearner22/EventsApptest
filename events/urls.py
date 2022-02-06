from calendar import month
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('events', views.all_events, name="list-events"), #This is to show the events apge
    path('<int:year>/<str:month>/', views.home, name="home"), #This is to change to url to show year and month.
    path('', views.home, name="home"),#This is to change to url to show year and month.
    path('add_venue', views.add_venue, name='add-venue'), #This is to the Venue Forms Check why it says add - venue, if it should add_venue like on the youtube video
    path('list_venues', views.list_venues, name='list-venues'), #This is list all the venues on venue page
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'), #This is to show venues 
    path('search_venues>', views.search_venues, name='search-venues'), #This is to search Venues 
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'), #IS IT VENUE OR VENUES?
    path('add_event', views.add_event, name='add-event'), #This links to views 
    path('update_event/<event_id>', views.update_event, name='update-event'), #This is to search Venues
    path('delete_event/<event_id>', views.delete_event, name='delete-event'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete-venue'),
    ]



#<int:year>/<str:month/
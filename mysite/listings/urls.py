from django.urls import path
from listings import views as l_views

app_name = 'listings'
urlpatterns = [
    path('', l_views.index, name='index'),
    path('<int:id>/', l_views.detail, name='detail'),
    path('add/', l_views.add, name='add'),
    path('<int:listing_id>/update_listing/', l_views.update_listing, name='update_listing'),
    path('<int:listing_id>/delete_listing/', l_views.delete_listing, name='delete_listing'),
]

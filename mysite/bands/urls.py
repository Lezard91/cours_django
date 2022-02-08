from django.urls import path
from bands import views as b_views

# On donne un nom à l'app
app_name = "bands"
urlpatterns = [
    path('', b_views.bands, name='index'),
    path('<int:band_id>/', b_views.band_detail, name='detail'),
    path('add_band/', b_views.add_band, name='add_band'),
    path('<int:band_id>/update_band/', b_views.update_band, name='update_band'),
    path('<int:band_id>/delete_band/', b_views.delete_band, name='delete_band'),
]

from django.urls import path
from . import views

app_name = "spaces"

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.sign_up, name="signup"),
    path('signin/', views.sign_in, name="signin"),
    path('logout/', views.log_out, name="logout"),
    path('client/profile/<int:id>', views.see_profile, name="see_client_profile"),
    path('landlord/profile/<int:id>',views.see_profile, name="landlord_profile"),
    path('user/edit/profile/<int:id>', views.edit_profile, name="edit_profile"),
    path('add/house/<int:id>', views.add_house, name="add_house"),
    path('see/houses/<int:id>' , views.see_houses , name="landlord_houses"),
    path('see/clients/<int:id>' , views.see_clients , name="landlord_clients"),
    path('see/statistics/<int:id>' , views.landlordStatistics, name="landlord_statistics"),
    path('see/notifications/<int:id>' , views.landlordNotifications, name="landlord_notifications"),
]

from django.urls import path
from . import views

app_name = "spaces"

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.sign_up, name="signup"),
    path('signin/', views.sign_in, name="signin"),
    path('logout/', views.log_out, name="logout"),
    path('client/profile/<int:id>', views.see_profile, name="client_profile"),
    path('landlord/profile/<int:id>',views.see_profile, name="landlord_profile"),
    path('client/profile/edit/<int:id>', views.edit_client_profile, name="edit_client_profile"),
    path('landlord/profile/edit/<int:id>', views.edit_landlord_profile, name="edit_landlord_profile"),
    path('add/house/<int:id>', views.add_house, name="add_house"),
    path('add/proposal/', views.client_proposal, name="client_proposal"),
    path('update/proposal/<int:proposal_id>', views.clientUpdateProposal, name="client_update_proposal"),
    path('remove/proposal/<int:proposal_id>', views.clientRemoveProposal, name="client_remove_proposal"),
    path('see/houses/<int:id>' , views.see_houses , name="landlord_houses"),
    path('see/clients/<int:id>' , views.see_clients , name="landlord_clients"),
    path('see/landlord/statistics/<int:id>', views.landlordStatistics, name="landlord_statistics"),
    path('see/client/statistics/<int:id>' , views.clientStatistics, name="client_statistics"),
    path('see/landlord/notifications/<int:id>', views.landlordNotifications, name="landlord_notifications"),
    path('see/client/notifications/<int:id>' , views.clientNotifications, name="client_notifications"),
    path('edit/house/<int:id>', views.edit_house, name="edit_house_founded"),
    path('delete/house/<int:house_id>', views.landlordRemoveHouse, name="landlord_delete_house"),
    path('news' ,views.news , name = "news" )
]

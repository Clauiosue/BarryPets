from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('pets/', views.pet_list, name='pet_list'),
    path('pets/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('pets/new/', views.pet_new, name='pet_new'),
    path('pets/<int:pk>/edit/', views.pet_edit, name='pet_edit'),
    path('pets/<int:pk>/delete/', views.pet_delete, name='pet_delete'),
    path('test/', views.test_view, name='test'),
    path('user/', views.user_detail, name='user_detail'),
    path('servicios/', views.servicios, name='servicios'),
    path('producto/', views.producto, name='producto'),
    path('QuienesSomos/', views.QuienesSomos, name='QuienesSomos'),
    path('contacto/', views.contacto, name='contacto'),
]

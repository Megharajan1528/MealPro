from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('open_signin', views.open_signin, name='open_signin'),
    path('open_signup', views.open_signup, name='open_signup'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),

    path('view_menu/<int:restaurant_id>/<str:username>/', views.view_menu, name='view_menu'),

    path('add_to_cart/<int:item_id>/<str:username>/', views.add_to_cart, name='add_to_cart'),

    path('view_cart/<str:username>/', views.view_cart, name='view_cart'),
    path('view_cart/<str:username>/', views.view_cart, name='view_cart'),
]
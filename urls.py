from django.urls import path
from .views import Userloginview,createShorturlview,shortURLDetailsview,userLogoutview,userRegistraionview


urlspatterns=[
    path('register/',userRegistraionview.as_view(),name='user_registration'),
    path('login/',Userloginview.as_view(),name='user_login'),
    path('shorten-url/',createShorturlview.as_view(),name='Create_short_URL'),
    path('url/<int:pk>/',shortURLDetailsview.as_view(),name='Short_url_details'),
    path('logout/',userLogoutview.as_view(),name='user_logout'),

]
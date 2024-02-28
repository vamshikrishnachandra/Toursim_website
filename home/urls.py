from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('favourite_places/', views.favourite_places_view, name='favourite_places'),
    path('favourite_places/taj_mahal/',views.taj_mahal,name='taj_mahal'),
    path('favourite_places/golden_temple/',views.golden_temple,name='golden_temple'),
    path('favourite_places/mysore_palace/',views.mysore_palace,name='mysore_palace'),
    path('favourite_places/varasani_temple/',views.varasani_temple,name='varasani_temple')
    
]

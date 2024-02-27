from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('favourite_places/', views.favourite_places_view, name='favourite_places'),
    path('taj_mahal/',views.taj_mahal,name='taj_mahal'),
    path('golden_temple/',views.golden_temple,name='golden_temple'),
    path('mysore_palace/',views.mysore_palace,name='mysore_palace'),
    path('varasani_temple/',views.varasani_temple,name='varasani_temple')
    
]

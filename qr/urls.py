from django.urls import path 
from . import views 

urlpatterns = [
    path('college/', views.c_view), 
    path('college/block/<int:bid>', views.b_view), 
    path('college/block/<int:bid>/floor/<int:fid>', views.f_view), 
    path('college/block/<int:bid>/floor/act/<int:fid>', views.qr_view), 
]
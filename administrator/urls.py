from django.urls import path
from .views import *

urlpatterns = [

    path('viewadmindashboard/',Viewadmindashboard.as_view(),name='viewadmindashboard'),
    path('viewcoursedashboard/',Viewcoursedashboard.as_view(),name='viewcoursedashboard'),
    path('viewcourse2dashboard/',Viewcourse2dashboard.as_view(),name='viewcourse2dashboard'),
    path('viewchangepassword1dashboard/',Viewchangepassword1dashboard.as_view(),name='viewchangepassword1dashboard'),
    path('viewchangepassword2dashboard/',Viewchangepassword2dashboard.as_view(),name='viewchangepassword2dashboard'),
    path('viewdepartment2dashboard/',Viewdepartment2dashboard.as_view(),name='viewdepartment2dashboard'),
    path('viewdept1dashboard/',Viewdept1dashboard.as_view(),name='viewdept1dashboard'),
    path('viewlogindashboard/',Viewlogindashboard.as_view(),name='viewlogindashboard'),

        

    path('viewnotificationdashboard/',Viewnotificationdashboard.as_view(),name='viewnotificationdashboard'),
    path('viewnotification2dashboard/',Viewnotification2dashboard.as_view(),name='viewnotification2dashboard'),
    path('viewnotification3dashboard/',Viewnotification3dashboard.as_view(),name='viewnotification3dashboard'), 
    path('viewnotification4dashboard/',Viewnotification4dashboard.as_view(),name='viewnotification4dashboard'),   
    path('viewnotification5dashboard/',Viewnotification5dashboard.as_view(),name='viewnotification5dashboard'), 
    path('viewotpdashboard/',Viewotpdashboard.as_view(),name='viewotpdashboard'), 
    path('viewstaffdashboard/',Viewstaffdashboard.as_view(),name='viewstaffdashboard'), 
    path('viewstudentprofiledashboard/',Viewstudentprofiledashboard.as_view(),name='viewstudentprofiledashboard'), 
    path('viewviewcoursedashboard/',Viewviewcoursedashboard.as_view(),name='viewviewcoursedashboard'), 

      

]




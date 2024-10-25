from django.shortcuts import render
from django.views import View

# Create your views here.
class Viewadmindashboard(View):
    def get(self,request):
        return render(request,'ADMIN/home.html')
    
class Viewcoursedashboard(View):
    def get(self,request):
        return render(request,'ADMIN/course.html')
    
class Viewcourse2dashboard(View):
    def get(self,request):
        return render(request,'ADMIN/course2.html')
class Viewchangepassword1dashboard(View):
    def get(self,request):
        return render(request,'ADMIN/changepassword1.html')
class Viewchangepassword2dashboard(View):
    def get(self,request):
        return render(request,'ADMIN/changepassword2.html')   
class Viewdepartment2dashboard(View):
    def get(self,request):
        return render(request,'ADMIN/department2.html')
class Viewdept1dashboard(View):
    def get(self,request):
        return render(request,'ADMIN/dept1.html')
class Viewlogindashboard(View):
    def get(self,request):
        return render(request,'ADMIN/login.html')
    
class Viewnotificationdashboard(View):
    def get(self,request):
        return render(request,'ADMIN/notification.html')
class Viewnotification2dashboard(View):
    def get(self,request):
        return render(request,'ADMIN/notification2.html')
class Viewnotification3dashboard(View):
    def get(self,request):
        return render(request,'ADMIN/notification3.html')
class Viewnotification4dashboard(View):
    def get(self,request):
        return render(request,'ADMIN/notification4.html')
class Viewnotification5dashboard(View):
    def get(self,request):
        return render(request,'ADMIN/notification5.html')

class Viewotpdashboard(View):
    def get(self,request):
        return render(request,'ADMIN/otp.html')
class Viewstaffdashboard(View):
    def get(self,request):
        return render(request,'ADMIN/staff.html')
class Viewstudentprofiledashboard(View):
    def get(self,request):
        return render(request,'ADMIN/studentprofile.html')
class Viewviewcoursedashboard(View):
    def get(self,request):
        return render(request,'ADMIN/viewcourse.html')
                                        
            
    
from django.shortcuts import render, redirect
from SEDAYA_IMS.models import User,Login,Admin,Member;
from django.contrib.auth import login

# Create your views here.
def homepage(request):
    return render (request,"homepage.html")

def booking(request):
    return render (request,"booking.html")

def loginselection(request):
    return render (request, "loginselection.html")

def registration(request):
    return render (request, "registration.html")

def aboutus(request):
    return render (request, "aboutus.html")

def chart(request):
    return render (request, "chart.html")

def adminhomepage(request):
    return render (request,"adminhomepage.html")

def adminbooking(request):
    return render (request,"adminbooking.html")

def adminregistration(request):
    return render (request, "adminregistration.html")

def adminaboutus(request):
    return render (request, "adminaboutus.html")

def adminchart(request):
    return render (request, "adminchart.html")



def home(request):
    user_fullname = request.session.get('user_fullname')
    return render(request, 'home.html', {'user_fullname': user_fullname})


def signup(request):
    if request.method == 'POST':
        userfullname = request.POST.get('userfullname')
        useremail = request.POST.get('useremail')
        userphone = request.POST.get('userphone')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User(userfullname=userfullname, useremail=useremail, userphone=userphone)
        user.save()
        
        login = Login(username=username, password=password, user=user)
        login.save()

        request.session['user_fullname'] = userfullname
        
        return redirect('login')
    
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            login_instance = Login.objects.get(username=username, password=password)
            
            # Set the session key based on the user's fullname
            request.session['user_fullname'] = login_instance.user.userfullname
            
            # Pass user's fullname to the template
            return render(request, 'home.html', {'user_fullname': login_instance.user.userfullname})
        except Login.DoesNotExist:
            pass

    alldata = Login.objects.all()
    context = {
        'alldata': alldata
    }
    return render(request, 'login.html', context)


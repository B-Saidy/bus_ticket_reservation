from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from pages.models import Bus, Booking


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        #check if passwords match
        if password==password2:
             #check if username exists
             if User.objects.filter(username=username).exists():
                #  messages.error(request, 'Username taken! ')
                 return redirect('register')
             else:
                 #check if email exist
                 if User.objects.filter(email=email).exists():
                    # messages.error(request, 'email exist')
                    return redirect('register')
                 else:
                    #looks good
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                    
                    # #login after registration
                    # auth.login(request, user)
                    # messages.error(request, 'you have been logged in')
                    # return redirect('index')
                    user.save()
                    # messages.error(request, 'you are now registered, log in')  
                    return redirect('login')     
        else:                  
            # messages.error(request, 'passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'your are now logged in ')
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('bookings')
        else:
            # messages.error(request, 'Invalid credentials ')
            return redirect('login')   
    else:
        return render(request, 'accounts/login.html')
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')

@login_required(login_url='login')  
def bookings(request):
    bookings = Booking.objects.filter(user = request.user)
    
    context = {
        'bookings': bookings
    }
    return render(request, 'accounts/booking.html', context)
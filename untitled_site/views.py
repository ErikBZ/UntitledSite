from django.contrib.auth import authenticate, login, views
'''
#putting my views over heah
def login_view(request):
    template = views.login(request)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            print("User is valid")
            #redirect to success
            return render(request, template)
        else:
            print("user doesn't exist anymore")
            return render(request, template)
    else:
        print("Invalid something")
        return render(request, template)

# i'll try this in my topics app to see if it works there
'''

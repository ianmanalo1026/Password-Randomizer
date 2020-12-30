import random
import string
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    raw_password = list(string.ascii_lowercase)
    random_password = ""
    
    email = request.POST.get('email')
    name = request.POST.get('name')
    new_password = request.POST.get('new_password')
    if request.method == 'POST' and 'password_button' in request.POST:

        if request.POST.get('uppercase_letter'):
            raw_password.extend(list(string.ascii_uppercase))
        if request.POST.get('numbers'):
            raw_password.extend(list(string.digits))
        if request.POST.get('special_character'):
            raw_password.extend(list('!@#$%^&*'))
        length = int(request.POST.get('length', 12))
            
        for x in range(length):
            random_password += random.choice(raw_password)
       
    if request.method == "POST" and 'send_email' in request.POST:
        new_password = {'thepassword':random_password}
        content = ('Hi ' + name + ',' + '\n' 
                + '\n' + '\n' + 'Thank you for using the Password Randomizer.' 
                + '\n' + '\n' + 'Here is your password: ' + str(new_password)
                + '\n' + '\n' + '\n' + '\n' +
                'Thank you!,' + '\n' + '\n' + 'Password Randomizer'
                )
        send_mail('Password Randomizer', content, 'manalo.website@gmail.com', [email], fail_silently=False)
        
        return render(request, 'password/home.html', new_password)    
    
    return render(request, 'password/home.html', new_password)





    
   
    
    
    



    
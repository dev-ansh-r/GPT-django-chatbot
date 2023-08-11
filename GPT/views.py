from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib import auth
from django.contrib.auth.models import User 
from .models import chat
from django.utils import timezone


openai_api_key = "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"
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 150,
        n=1,
        stop = None,
        temperature = 0.7,
    )

    answer = response.choice[0].text.strip()
    return answer

# Create your views here.
def GPT(request):
    chats = chat.objects.filter(user=request.user)
    
    if request.method == 'POST':
        message  = request.POST.get('message')
        response = ask_openai(message)
        Chat = chat(user=request.user, message=message, response=response, created_at=timezone.now())
        Chat.save()

        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html',{'chats':chats})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate( username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('GPT')
        else:
            error_message = "Invalid Credentials"
            return render(request, 'login.html', {'error_message': error_message})
        
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cnfrm_password = request.POST['cnfrm_password']

        if password == cnfrm_password:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                auth.login(request, user)
                return redirect('GPT')
            except:
                error_message = "Username already exists"
                return render(request, 'register.html', {'error_message': error_message})
            else:
                error_message = "Password and Confirm Password does not match"
                return render(request, 'register.html', {'error_message': error_message})
    
    return render(request, 'register.html')

    
def logout(request):
    auth.logout(request)
    return redirect('login')
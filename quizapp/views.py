from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Quiz,Question,Answer,Category
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#Registeration for new User
def registerUser(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            messages.error(request,'An error occured during registration Try Again!')    
    return render(request,'quizapp/register.html',{"form":form})


#User Login
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'✅ Logged in successfully!')

            return redirect('quiz_list')
        else:
            messages.error(request,'Invalid Username or Password...')
    return render(request,'quizapp/login.html')        


#User Logout
def logoutUser(request):
    logout(request)
    return redirect('quiz_list')


@login_required(login_url='login')
def quiz_list(request):
    quizzes = Quiz.objects.all()
    context = {"quizzes":quizzes}
    return render(request,'quizapp/quiz_list.html',context)

def quiz_detail(request,pk):
    category = Category.objects.all()
    quiz = get_object_or_404(Quiz,id=pk)
    questions = quiz.questions.all().order_by('id')
    if request.method == "POST":
        score = 0
        total = questions.count()*5
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                answer = Answer.objects.get(id=selected)
                if answer.is_correct:
                    score+=5
        context = {
            'score':score,
            'total':total,
            'quiz':quiz,
            'percentage':(score/total)*100
        }            
        return render(request,'quizapp/quiz_result.html',context)

    context = {'quiz':quiz,'questions':questions,'category':category}
    return render(request,'quizapp/quiz_detail.html',context)


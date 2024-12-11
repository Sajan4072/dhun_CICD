from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from .apps import PredictorConfig
from .forms import DocumentForm
from .models import Document
from .Metadata import getmetadata
import warnings
from .predict import predict_gen
from django.contrib import messages
warnings.simplefilter('ignore')

from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForms
from .models import BlogPost
from datetime import datetime



class IndexView(ListView):
    template_name= 'music/index.html'
    def get_queryset(self):
        return True

def model_form_upload(request):

    documents = Document.objects.all()
    if request.method == 'POST':
        if len(request.FILES) == 0:
            messages.error(request,'Upload a file')
            return redirect("predictor:index")

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploadfile = request.FILES['document']
            print(uploadfile.name)
            print(uploadfile.size)
            if not uploadfile.name.endswith('.wav'):
                messages.error(request,'Only .wav file type is allowed')
                return redirect("predictor:index")
            meta = getmetadata(uploadfile)
            
            genre = predict_gen(meta)
            print(genre)

            context = {'genre':genre}
            return render(request,'music/result.html',context)

    else:
        form = DocumentForm()

    return render(request,'music/result.html',{'documents':documents,'form':form})


def log(request):
    if not request.user.is_authenticated:
        return render(request,"music/login1.html",{"message":None})
    
    context={
        "user":request.user
    }
    return render(request,"music/index.html",context)

def login_view(request):
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("predictor:log"))
    else:
        return render(request,"music/login1.html",{"message":"invalid credential." })      




def logout_view(request):
    logout(request)
    return render(request,"music/login1.html",{"message":"Logged out"})


def registerPage(request):
    form=CreateUserForms()
    
    if request.method == 'POST':
        form = CreateUserForms(request.POST)
        if form.is_valid():
            form.save()
    
    context={"form":form}
    return render(request,"music/register.html",context)



   

def signup_view(request):
    return render(request,"music/register.html")


def about(request):
    return render(request,"music/about.html")


def blogs(request):
    '''get all the data from the database and display it in the blogs.html'''
    posts = BlogPost.objects.all().order_by('-date_posted')
    print(posts)
    context = {'posts': posts}   

    return render(request,"music/article.html",context)

def add(request):
    return render(request,"music/add.html")


def post(request):
    '''get inputs from the from add.html and post the inputs to the database Blogpost and after that redirect to url blogs'''
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        subtitle = request.POST['subtitle']
        BlogPost.objects.create(title=title, content=content, author=author, subtitle=subtitle, date_posted=datetime.now())
        return HttpResponseRedirect(reverse('predictor:blogs'))
    else:
        return render(request, 'music/add.html')


def detail(request, id):
    '''get the id of the post and display the post in detail.html'''
    post = BlogPost.objects.get(id=id)
    context = {'post': post}
    return render(request, 'music/detail.html', context)
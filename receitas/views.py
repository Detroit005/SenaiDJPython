from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',context={'nome':'Receitas Django',})
def sobre(request):
    return render(request,'sobrenomes.html')
def receitas(request):
    return render(request,'receita.html')

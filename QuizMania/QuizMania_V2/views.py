from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"QuizMania_V2/Catalog.html")

def admin_V(request):
    return render(request,"QuizMania_V2/admin.html")


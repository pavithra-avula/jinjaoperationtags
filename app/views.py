from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'pavithra','age':14,'marks':85,'grade':9}
    return render(request,'conditions.html',context=d)
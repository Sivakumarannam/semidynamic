from django.shortcuts import render

# Create your views here.



def first(request):
    data='This data is our assumption'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)


def login(request):
    data='Siva'
    d={'username':data}
    return render(request,'login.html',context=d)
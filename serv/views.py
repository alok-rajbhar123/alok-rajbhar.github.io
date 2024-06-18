from django.shortcuts import render

# Create your views here.
def ser(request):
    context = {'ser': 'active'}
    return render(request, 'serv/services.html',context)
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def receipes(request):
    if request.method == "POST":
        data=request.POST
        rec_name = data.get('rec_name')
        rec_desc =  data.get('rec_desc')
        rec_images =  request.FILES.get('rec_images')
        print(rec_images)
        Receipe.objects.create(
            rec_name = rec_name,
            rec_desc = rec_desc,
            rec_images = rec_images
        )

    queryset = Receipe.objects.all()
    context = {'receipes': queryset}
    return render(request, 'receipe.html', context)


def delete_receipe(request, id):
    querySet = Receipe.objects.get(id=id)
    querySet.delete()
    return redirect('/receipes')


from django.shortcuts import redirect, render
from .models import feedbacks
from .forms import feedbacksForm



def main(request):
    return render(request,'main.html')
def cv(request):
    return render(request,'cv/cv.html')
def contact_info(request):
    table = feedbacks.objects.all()
    context={'table':table}
    return render(request,'cv/contact_info.html',context)
def image(request,pk):
    record= feedbacks.objects.get(id=pk)
    return render(request ,'cv/see_image.html',{'img':record})

def contact(request):
    form = feedbacksForm()
    if request.method=='POST':
        data = feedbacksForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            return redirect('main')
    context ={'form': form}
    return render(request,'cv/contact.html',context)

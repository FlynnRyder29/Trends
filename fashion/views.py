from django.shortcuts import render
from django.http import HttpResponse
from fashion.models import fashion
from fashion.forms import loginForm

def login(request):
    username='not logged in'
    if request.method=="POST":
        MyloginForm=loginForm(request.POST)
        if MyloginForm.is_valid():
            username=MyloginForm.cleaned_data['username']
        else:
            MyloginForm=loginForm()
        return render(request,'loggedin.html',{'username':username})
      



def crudops(request):

    objects=fashion.objects.all()
    res='printing all users name and product name in the database:<br>'
    
    for elt in objects:
        res+=elt.product+elt.name+'<br>'


    '''
    #read a specific entry
    mobile=fashion.objects.get(name='mohan')
    res+='printing one entry<br>'
    res+=mobile.name
    '''
    
    '''
    #delete an entry
    mobile=fashion.objects.get(name='mohan')
    rest='<br>Deletion of a entry<br>'
    mobile.delete()
    '''
    
    #updating

    res+='Updating entry<br>'
    Fashion=fashion.objects.get(name='paul')
    fashion.product='casual-wear shirt'
    Fashion.save()
    

    
    return HttpResponse(res)


    
    
    

# Create your views here.
def shirts(request):
    return render(request,'shirts.html')

def trousers(request):
    return render(request,'trousers.html')

def shoes(request):
    return render(request,'shoes.html')

def watches(request):
    return render(request,'watches.html')
def trends(request):
    return render(request,'trends.html')
import csv
def orders(request):
    if request.method=='POST':
        dict1=request.POST
        with open('userdata.csv','a')as csvfile:
            wrt=csv.writer(csvfile)
            for key,value in dict1.items():
                wrt.writerow([key,value])
    return render(request,'order.html')


def deletion(request):
    if request.method=='POST':
        dict1=request.POST
        with open('userdata.csv','w')as csvfile:
            csvfile.truncate()
            csvfile.close()
    return render(request,'delete.html')        





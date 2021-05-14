from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogContact,Blogpost

# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request,'blog/index.html',{'mypost':myposts})

def about(request):
    return render(request,'blog/about.html')

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id=id)
    print(post[0])
    p = id-1
    n =id+1
    return render(request,'blog/blogpost.html',{'post':post[0],'next':n,'prev':p})

def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name','Error')
        
        email = request.POST.get('email','Error')
       
        phone = request.POST.get('phone','error')
        
        desc = request.POST.get('desc','error')

        blog_info =BlogContact(contact_name_blog=name,contact_email_blog=email,contact_phone_blog=phone,contact_desc_blog=desc)
        print(blog_info)
        blog_info.save()
        thank = True
    return render(request,'blog/contact.html',{'thank':thank})
    

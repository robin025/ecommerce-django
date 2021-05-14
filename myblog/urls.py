from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="myblog"),
    path("blogpost/<int:id>",views.blogpost,name="blogpost"),
    path("about/",views.about,name="About Us"),
    path("contact/",views.contact,name="myblog")
]


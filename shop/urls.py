from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="shopHome"),
    path("about/",views.about,name="About Us"),
    path("contact/",views.contact,name="Contact Us"),
    path("tracker/",views.tracker,name="Tracking Status"),
    path("Search/",views.search,name="Search"),
    path("prodview/<int:my_id>",views.prodview,name="Product View Page"),
    path("checkout/",views.checkOut,name="Checkout"),
]


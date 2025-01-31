from django.urls import path

from . import views

appname = "mainapp"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("divesites/", views.DiveSiteView.as_view(), name="divesites"),
    path("products/", views.ProductsView.as_view(), name="products"),
    path("socials/", views.SocialsView.as_view(), name="socials"),
    path("staff/", views.StaffView.as_view(), name="staff"),
]
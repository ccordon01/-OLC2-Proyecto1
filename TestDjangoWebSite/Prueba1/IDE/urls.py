from django.conf.urls import url
from IDE import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^name/$', views.get_name), # Add this /about/ route
]
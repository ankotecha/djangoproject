from django.contrib import admin
from django.urls import path,include
from comment.views import comment
from django.conf.urls import url
from django.shortcuts import render_to_response


urlpatterns = [
   #  path('admin/', admin.site.urls),
   url(r'^comment/$',comment)
    ] 
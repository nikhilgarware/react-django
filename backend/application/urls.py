from django.urls import path
from application import api
urlpatterns = [path('', api.Test.as_view(), name="testing")]

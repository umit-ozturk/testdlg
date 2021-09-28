from django.urls import path

from api.v1.views import TotalNumberView

app_name = "api_v1"

urlpatterns = [
    path("total/", view=TotalNumberView.as_view(), name="total"),
]

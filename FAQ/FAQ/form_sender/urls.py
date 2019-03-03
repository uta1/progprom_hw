from django.urls import path, re_path

from FAQ.form_sender.views import (
    recieve_form,
    response
)

app_name = "form_sender"
urlpatterns = [
    path("", view=recieve_form),
    path("response.html", view=response, name="detail"),
]

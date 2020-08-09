from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('comment/', views.comment, name="comment"),
  path('blog/', views.blog, name="blog"),
]

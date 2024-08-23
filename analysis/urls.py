from django.urls import path
from .views import home, upload_file

urlpatterns = [
    path('', home, name='home'),  # Home page
     path('upload/', upload_file, name='upload_file'),
    # path('result/', result_view, name='result'),
]

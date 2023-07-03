from moviedash.dash import movies_diagram
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
]

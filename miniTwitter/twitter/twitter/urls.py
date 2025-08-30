from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tweet import views as tweet_views   # import index view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tweet_views.index, name='home'),   # root URL shows index.html
    path('tweet/', include('tweet.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

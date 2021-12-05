from django.contrib import admin
from django.urls import path
from amity.views import studentListView, blockListView
from django.conf.urls.static import static

urlpatterns = [
    path('api/students', studentListView),
    path('admin/', admin.site.urls),
    path('api/blocks', blockListView),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
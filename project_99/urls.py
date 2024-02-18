from django.contrib import admin
from django.urls import path
from inventory import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='index'),
    path('table/', views.table, name='table'),
    path('add/', views.add_item, name='add'),
    path('edit/<str:id>', views.edit_item, name='edit'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
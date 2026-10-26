from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from core import views # core adında bir app oluşturduğunu varsayıyorum

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')), # Dil değiştirme rotası
]

# Çok dilli URL'ler (Örn: /az/oyunlar/, /en/oyunlar/)
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('kategori/<str:cat_slug>/', views.index, name='kategori'), # ?cat= parametresi yerine modern URL
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
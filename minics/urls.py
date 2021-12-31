from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("web.urls",namespace="web")),
    path('product/', include("product.urls",namespace="product")),
    path('cart/', include("product.urls",namespace="product")),
    path('update_cart/', include("product.urls",namespace="product")),
    path('about/', include("user.urls",namespace="user")),
    path('whyus/',include("why.urls",namespace="why"))

]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""waiter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from cart.views import CartViewSet
from Food.views import FoodViewSet
from category.views import CategoryViewSet
from restaurent.views import RestaurentViewSet


router = routers.DefaultRouter()
router.register('cart',CartViewSet)
router.register('food',FoodViewSet)
router.register('category',CategoryViewSet)
router.register('restaurent',RestaurentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('account.urls'),name="account"),
    path('', include(router.urls)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "VWAITER"
admin.site.site_title = "VWAITER"
admin.site.index_title = "Welcome to VWAITER"
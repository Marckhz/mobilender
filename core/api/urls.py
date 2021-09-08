from api.views import OrderStatusViewSet
from api.views import SiteViewSet
from django.conf.urls import url
from api.views import OrdersViewSet
from api.views import PersonViewSet, ArticlesViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework import routers


schema_view = get_schema_view(
    openapi.Info(
        title='Mobilender',
        default_version='v1',
        description='just for fun',
        contact=openapi.Contact(email='marcohdes94i@gmail.com')
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('client', PersonViewSet)
router.register('articles', ArticlesViewSet)
router.register('orders', OrdersViewSet)
router.register('sites', SiteViewSet)
router.register('orders-status', OrderStatusViewSet)


urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from .views import ProviderViewSet, ConsumerViewSet, ProviderLoanViewSet, ConsumerLoanViewSet

router = DefaultRouter()
router.register(r'providers', ProviderViewSet)
router.register(r'consumers', ConsumerViewSet)
router.register(r'provider-loans', ProviderLoanViewSet)
router.register(r'consumer-loans', ConsumerLoanViewSet)

urlpatterns = router.urls
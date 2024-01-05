from rest_framework.routers import DefaultRouter
from app.views.view_set import AppViewSet


router = DefaultRouter()
router.register("", AppViewSet, basename='app')
urlpatterns = router.get_urls()

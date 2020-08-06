from rest_framework.routers import DefaultRouter
from legalapp import views
router = DefaultRouter()
router.register('User', views.UserViewSet,basename='User')
router.register('Plan', views.PlanViewSet,basename='Plan')
router.register('Previous_Plans', views.Previous_PlansViewSet,basename='Previous_Plans')
urlpatterns = router.urls
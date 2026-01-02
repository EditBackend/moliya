from rest_framework.routers import DefaultRouter
from .views import (
    TolovViewSet,
    ExpenseViewSet,
    ExpenseCategoryViewSet,
    IshHaqqiViewSet,
    QarzdorViewSet,
    QarzMiqdoriViewSet
)

router = DefaultRouter()

router.register('tolovlar', TolovViewSet)
router.register('expense-categories', ExpenseCategoryViewSet)
router.register('expenses', ExpenseViewSet)
router.register('ish-haqqi', IshHaqqiViewSet)
router.register('qarzdorlar', QarzdorViewSet)
router.register('qarz-miqdori', QarzMiqdoriViewSet)

urlpatterns = router.urls



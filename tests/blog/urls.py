from rest_framework_date_archive import DateArchiveRouter

from .views import BlogViewSet, BlogTimeViewSet


router = DateArchiveRouter()
router.register('blogs', BlogViewSet)
router.register('blogtimes', BlogTimeViewSet)

urlpatterns = router.urls

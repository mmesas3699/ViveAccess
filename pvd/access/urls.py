from django.urls import include, path

from rest_framework.routers import DefaultRouter

from access.views import grades as grade_views
from access.views import classroom as classroom_views
from access.views import accessory as accesory_views
from access.views import computers as computer_views
from access.views import students as student_views
from access.views import access as access_views


router = DefaultRouter()
router.register(r'grades', grade_views.GradeViewSet, basename='grade')
router.register(r'classrooms', classroom_views.ClassroomViewSet, basename='classroom')
router.register(r'accesories', accesory_views.AccessoryViewSet, basename='accesory')
router.register(r'computers', computer_views.ComputerViewSet, basename='computer')
router.register(r'students', student_views.StudentViewSet, basename='students')
router.register(r'access', access_views.AccessViewSet, basename='access' )

urlpatterns = [
    path('', include(router.urls)),
]

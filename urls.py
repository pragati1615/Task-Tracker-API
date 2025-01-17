"""The app's urls.py uses DRF's router to automatically create URLs:

GET /api/tasks/: List tasks
POST /api/tasks/: Create task
GET /api/tasks/{id}/: Retrieve task
PUT /api/tasks/2/: Update task
DELETE /api/tasks/{id}/: Delete task"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = router.urls



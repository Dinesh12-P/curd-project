from django.urls import path
from store.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', hero, name='myview'),
    path('table/',table,name ='table'),
    path('create/',CreateTaskView.as_view(),name='create'),
    # path('create/',create_task, name = 'create'),
    path('use/', scroll ,name ='use'),
    path('mark/<pk>/', mark ,name = 'mark'),
    path('unmark/<pk>/', unmark, name="unmark"),
    # path('delete/<pk>/',DeleteTaskView.as_view(),name='delete'),
    path('delete/<pk>/', delete, name="delete"),
    # path('update/<pk>/', UpdateTaskView.as_view(),name='update'),
    path('update/<pk>',update_Task,name='update'),
    path('pricing/', pricing,name='pricing'),
    path('forms/',form_create,name='forms'),
    path('dinesh/',dinesh,name='dinesh'),
    path('register/',register_form,name='register'),
    path('login/',login_form,name='login'),
    path('logout/',logout_form,name='logout'),
    path('<pk>/',view_details,name='view_details'),
]
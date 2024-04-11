from django.urls import path
from .views import TodoListCreate, ToDoRetrieveUpdateDestroy,ToDoToggleComplete,signup,login

urlpatterns = [
    path('todos/', TodoListCreate.as_view(), name='list'), 
    path('todos/<int:pk>', ToDoRetrieveUpdateDestroy.as_view()), 
    path('todos/<int:pk>/complete', ToDoToggleComplete.as_view()), 
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),

]



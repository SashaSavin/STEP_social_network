
from django.urls import path
from . views import ElemsView, ElemView

urlpatterns = [
    path('', ElemsView.as_view()),
    path('<int:pk>/', ElemView.as_view(), name='detail')
]



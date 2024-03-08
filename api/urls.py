from django.urls import path
from api.views import ExpressionEvaluate

urlpatterns = [
  path('exp_evaluate/', ExpressionEvaluate.as_view()),
]
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ExpressionSerializer
from django.http import JsonResponse

class ExpressionEvaluate(APIView):
  def post(self, request):
    serializer = ExpressionSerializer(data=request.data)
    if serializer.is_valid():
      expression = serializer.validated_data['expression']

      if serializer.invalid_operator(expression) or serializer.hasNestedOperators(expression):
        return JsonResponse({
          'success': False,
          'expression': "The string contains an invalid operator. Supported only +, - operator and not be nested.",
        }, status=400)

      try:
        result = eval(expression)
        return JsonResponse({
          'success': True,
          'result': result
        }, status=200)
      except Exception as e:
        return JsonResponse({
          'success': False,
          'error': str(e)
        }, status=400)
    return JsonResponse(serializer.errors, status=400)

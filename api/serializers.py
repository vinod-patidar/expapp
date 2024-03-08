from rest_framework import serializers

class ExpressionSerializer(serializers.Serializer):
  expression = serializers.CharField(max_length=50, required=True)

  @staticmethod
  def invalid_operator(s):
    valid_operators = set('+-')
    for char in s:
      if char not in valid_operators and not char.isdigit() and char != ' ':
        return True
    return False

  @staticmethod
  def hasNestedOperators(expressionValue):
    allowedOperators = tuple('+-')
    if allowedOperators[0] in expressionValue and allowedOperators[1] in expressionValue:
      return True

    eachCharCount = {}
    for eachChar in expressionValue:
        if eachChar in allowedOperators:
          eachCharCount[eachChar] = eachCharCount.get(eachChar, 0) + 1
          if eachCharCount[eachChar] == 2:
              return True
    return False

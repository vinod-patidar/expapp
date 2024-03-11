"""Unit Tests Cases."""
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status


class ExpressionApiTests(TestCase):
    """Unit Test Cases for expression API."""

    def setUp(self):
        self.client = APIClient()
        self.endpoint_url = 'http://127.0.0.1:8000/api/exp_evaluate/'

    def test_addition_success(self):
        """ Successful Addition expression. """
        payload = {
            'expression': '1 + 1'
        }

        res = self.client.post(
            self.endpoint_url,
            data=payload,
        )

        response = res.json()
        self.assertEqual(
            res.status_code, 
            status.HTTP_200_OK
        )
        self.assertEqual(
            response['result'], 
            2,
            'Addition Successful'
        )
    
    def test_subtraction_success(self):
        """ Successful Subtraction expression. """
        payload = {
            'expression': '3 - 2'
        }

        res = self.client.post(
            self.endpoint_url,
            data=payload,
        )

        response = res.json()
        self.assertEqual(
            res.status_code, 
            status.HTTP_200_OK
        )
        self.assertEqual(
            response['result'], 
            1,
            'Subtraction Successful!'
        )
    
    def test_validation_failure(self):
        """ Failure Addition expression. """
        payload = {
            'expression': '1 + 1 + 1'
        }

        res = self.client.post(
            self.endpoint_url,
            data=payload,
        )

        response = res.json()
        self.assertEqual(
            res.status_code, 
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(
            response['expression'], 
            'The string contains an invalid operator. Supported only +, - operator and not be nested.',
            'Validation Failure!'
        )

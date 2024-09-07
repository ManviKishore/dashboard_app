from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

class CandlestickDataViewTests(APITestCase):
    def test_get_candlestick_data(self):
        """
        Test the API endpoint for fetching candlestick data.
        """
        # Send a GET request to the endpoint
        response = self.client.get('/api/candlestick-data/')
        
        # Assert that the status code of the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert that 'data' key is present in the response
        self.assertIn('data', response.data)
        
        # Assert that the value of 'data' is a list
        self.assertTrue(isinstance(response.data['data'], list))

class LineChartDataViewTests(APITestCase):
    def test_get_line_chart_data(self):
        """
        Test the API endpoint for fetching line chart data.
        """
        # Send a GET request to the endpoint
        response = self.client.get('/api/line-chart-data/')
        
        # Assert that the status code of the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert that 'labels' key is present in the response
        self.assertIn('labels', response.data)
        
        # Assert that 'data' key is present in the response
        self.assertIn('data', response.data)

class BarChartDataViewTests(APITestCase):
    def test_get_bar_chart_data(self):
        """
        Test the API endpoint for fetching bar chart data.
        """
        # Send a GET request to the endpoint
        response = self.client.get('/api/bar-chart-data/')
        
        # Assert that the status code of the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert that 'labels' key is present in the response
        self.assertIn('labels', response.data)
        
        # Assert that 'data' key is present in the response
        self.assertIn('data', response.data)

class PieChartDataViewTests(APITestCase):
    def test_get_pie_chart_data(self):
        """
        Test the API endpoint for fetching pie chart data.
        """
        # Send a GET request to the endpoint
        response = self.client.get('/api/pie-chart-data/')
        
        # Assert that the status code of the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert that 'labels' key is present in the response
        self.assertIn('labels', response.data)
        
        # Assert that 'data' key is present in the response
        self.assertIn('data', response.data)

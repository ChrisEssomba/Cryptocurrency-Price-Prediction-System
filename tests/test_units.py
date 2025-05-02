'''
What does it test?

    Tests the get_data() function when the API call succeeds.

    Mocks the API response to return a predefined JSON structure.

    Checks if:

        The function returns a pandas.DataFrame.

        The DataFrame has the correct number of rows (2 in this case).

        The expected cryptocurrency (Bitcoin) is present.

Why is this important?

    Ensures that when the API returns valid data, get_data() processes it correctly.

    Prevents regressions if the API response structure changes.
'''


import pytest
from app import get_data
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd
import json

def test_get_data_success(requests_mock):
    # Mock the API response
    mock_response = {
        'data': [
            {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC'},
            {'id': 2, 'name': 'Ethereum', 'symbol': 'ETH'}
        ]
    }
    
    requests_mock.get(
        'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',
        json=mock_response,
        status_code=200
    )
    
    result = get_data()
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert 'Bitcoin' in result['name'].values

def test_get_data_failure(requests_mock):
    # Simulate a connection error
    requests_mock.get(
        'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',
        exc=ConnectionError
    )
    
    result = get_data()
    
    # Should return an empty DataFrame on error
    assert isinstance(result, pd.DataFrame)
    assert result.empty
    
    
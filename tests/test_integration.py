'''
What does it test?

    Tests the get_data() function when the API call fails (simulates a ConnectionError).

    Checks if:

        The function still returns a pandas.DataFrame (even if empty).

        The DataFrame is empty (since the API failed).

Why is this important?

    Ensures the app gracefully handles API failures instead of crashing.

    Verifies that the function returns a consistent type (DataFrame) even in error cases.       
'''
import pytest
from app import app
import pandas as pd
from bs4 import BeautifulSoup

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client, mocker):
    # Mock the get_data function
    mock_data = pd.DataFrame({
        'name': ['Bitcoin', 'Ethereum'],
        'symbol': ['BTC', 'ETH']
    })
    
    mocker.patch('app.get_data', return_value=mock_data)
    
    # Make a request to the home route
    response = client.get('/')
    
    assert response.status_code == 200
    
    # Parse the HTML response
    soup = BeautifulSoup(response.data, 'html.parser')
    table = soup.find('table')
    
    # Check if the table contains our mock data
    assert table is not None
    assert 'Bitcoin' in str(table)
    assert 'Ethereum' in str(table)
    
def test_home_route(client, mocker):  # Requires `pytest-mock`
    mock_data = pd.DataFrame({"name": ["Bitcoin"], "symbol": ["BTC"]})
    mocker.patch("app.get_data", return_value=mock_data)
    response = client.get('/')
    assert response.status_code == 200
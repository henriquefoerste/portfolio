#to run the test, use the command: pytest tests/test_data_loader.py
import pytest
import pandas as pd
from pipeline.data_loader import DataLoader

@pytest.fixture
def data_loader():
    return DataLoader()

# Test loading from CSV
def test_load_from_csv(data_loader):
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    data = data_loader.load_from_csv(url)
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

# Test loading from API
def test_load_from_api(data_loader):
    api_url = "https://jsonplaceholder.typicode.com/users"
    data = data_loader.load_from_api(api_url)
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert 'name' in data.columns

# Test loading from Yahoo Finance
def test_load_from_yahoo_finance(data_loader):
    ticker = "AAPL"
    data = data_loader.load_from_yahoo_finance(ticker, start_date="2022-01-01", end_date="2022-12-31")
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert 'Close' in data.columns

# Test loading from CSV with invalid path
def test_load_from_invalid_csv(data_loader):
    data = data_loader.load_from_csv("invalid_path.csv")
    assert data is None

# Test loading from API with invalid URL
def test_load_from_invalid_api(data_loader):
    data = data_loader.load_from_api("https://invalid-url.com")
    assert data is None

# Test loading from Yahoo Finance with invalid ticker
def test_load_from_invalid_yahoo_finance(data_loader):
    data = data_loader.load_from_yahoo_finance("INVALIDTICKER", start_date="2022-01-01", end_date="2022-12-31")
    assert data is None

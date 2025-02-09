import pandas as pd
import sqlalchemy
import requests
yf = None

try:
    import yfinance as yf
except ImportError:
    print("yfinance library not found. Install it with 'pip install yfinance'")

class DataLoader:
    def load_from_csv(self, filepath):
        """Load data from a CSV file."""
        try:
            data = pd.read_csv(filepath)
            print(f"Data loaded from {filepath}")
            return data
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return None

    def load_from_database(self, connection_string, query):
        """Load data from a SQL database."""
        try:
            engine = sqlalchemy.create_engine(connection_string)
            data = pd.read_sql(query, engine)
            print("Data loaded from database")
            return data
        except Exception as e:
            print(f"Error loading from database: {e}")
            return None

    def load_from_api(self, url, params=None):
        """Load data from an API."""
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data)
            print(f"Data loaded from API: {url}")
            return df
        except Exception as e:
            print(f"Error loading from API: {e}")
            return None

    def load_from_yahoo_finance(self, ticker, start_date=None, end_date=None):
        """Load historical stock data from Yahoo Finance."""
        if yf is None:
            raise ImportError("yfinance library is not installed.")

        try:
            data = yf.download(ticker, start=start_date, end=end_date)
            if data.empty:
                print(f"No data found for {ticker} on Yahoo Finance")
                return None
            print(f"Data loaded for {ticker} from Yahoo Finance")
            return data
        except Exception as e:
            print(f"Error loading data from Yahoo Finance: {e}")
            return None
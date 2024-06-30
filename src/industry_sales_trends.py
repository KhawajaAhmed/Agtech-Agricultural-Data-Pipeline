# industry_sales_trends.py
import pandas as pd
import requests
from .data_collector import DataCollector  # Adjust the import path based on your project structure
from .utils import fetch_data, load_config
import logging
from json import JSONDecodeError

class IndustrySalesTrendsCollector(DataCollector):
    def __init__(self):
        super().__init__('industry_sales_trends')

    def fetch_data(self):
        base_url = self.source_config['base_url']
        api_key = self.source_config['api_key']
        params = {
            'key': 'api_key',
            'commodity_desc': 'CORN',
            'year__GE' : '2012',
            'state_alpha' : 'VA',
            'format': 'JSON'
        }
        
        response = fetch_data(base_url, params)

        if response is not None:
            try:
                json_data = response.json()
                if 'data' in json_data:
                    self.data = pd.DataFrame(json_data['data'])
                else:
                    logging.error("JSON response does not contain 'data' key")
            except JSONDecodeError as e:
                logging.error(f"Error decoding JSON response: {e}")
            except ValueError as e:
                logging.error(f"Error processing JSON data: {e}")
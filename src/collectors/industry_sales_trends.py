# industry_sales_trends.py
import pandas as pd
import requests
from .data_collector import DataCollector
from ..utils import fetch_data, log_error, log_info
import logging
from json import JSONDecodeError

class IndustrySalesTrendsCollector(DataCollector):
    def __init__(self):
        log_info("Initializing IndustrySalesTrendsCollector")

        # Call the parent class (DataCollector) initializer with the source name 'industry_sales_trends'
        super().__init__('industry_sales_trends')

    def fetch_data(self):
    
        # Extract the base URL and API key from the source configuration
        base_url = self.source_config['base_url']
        api_key = self.source_config['api_key']

        # Prepare the parameters for the API request using the source configuration
        params = {
            'key': 'api_key',
            'source_desc' : self.source_config['source_desc'],
            'sector_desc' : self.source_config['sector_desc'],
            'group_desc' : self.source_config['group_desc'],
            'commodity_desc' : self.source_config['commodity_desc'],
            'statisticcat_desc' : self.source_config['statisticcat_desc'],
            'short_desc' : self.source_config['short_desc'],
            'domain_desc' : self.source_config['domain_desc'],
            'agg_level_desc' : self.source_config['agg_level_desc'],
            'format': self.source_config['format']
        }
        
        response = fetch_data(base_url, params)
        
        # Parse the json response and convert the 'data' part to a dataframe
        if response is not None:
            try:
                json_data = response.json()
                if 'data' in json_data:
                    self.data = pd.DataFrame(json_data['data'])
                else:
                    log_error("JSON response does not contain 'data' key")
            except JSONDecodeError as e:
                log_error(f"Error decoding JSON response: {e}")
            except ValueError as e:
                log_error(f"Error processing JSON data: {e}")
    
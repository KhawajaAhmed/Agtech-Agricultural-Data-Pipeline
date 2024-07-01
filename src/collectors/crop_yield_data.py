import pandas as pd
from .data_collector import DataCollector
import logging
import faostat # Import the faostat library for fetching agricultural data 
from ..utils import log_info, log_error

class CropYieldDataCollector(DataCollector):
    def __init__(self):
        log_info("Initializing CropYieldDataCollector")

        # Call the parent class (DataCollector) initializer with the source name 'crop_yield_data'
        super().__init__('crop_yield_data')

    def fetch_data(self):
        try:
            log_info("Fetching crop yield data")

            # Prepare the parameters for the FAOSTAT API request using the source configuration
            mypars = {
                'area': self.source_config['usa'],
                'element': self.source_config['yield'],
                'item': self.source_config['crops']
                }
            
            # Fetch data from FAOSTAT using the prepared parameters
            self.data = faostat.get_data_df('QCL', pars=mypars, strval=False)
            
        except Exception as e:
            log_error(f"An error occurred while fetching data: {e}")
    
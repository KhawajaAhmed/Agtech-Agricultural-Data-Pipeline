import pandas as pd
from .data_collector import DataCollector
import logging
import faostat 

class CropYieldDataCollector(DataCollector):
    def __init__(self):
        logging.info("Initializing CropYieldDataCollector")
        super().__init__('crop_yield_data')

    def fetch_data(self):
        try:
            logging.info("Fetching crop yield data")
            mypars = {
                'area': self.source_config['usa'],
                'element': self.source_config['yield'],
                'item': self.source_config['crops']
                }
            
            self.data = faostat.get_data_df('QCL', pars=mypars, strval=False)
            
        except Exception as e:
            logging.error(f"An error occurred while fetching data: {e}")
    
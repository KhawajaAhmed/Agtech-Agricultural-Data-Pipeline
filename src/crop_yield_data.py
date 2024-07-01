import pandas as pd
from .data_collector import DataCollector
import logging
import faostat 

class CropYieldDataCollector(DataCollector):
    def __init__(self):
        super().__init__('crop_yield_data')

    def fetch_data(self):

        mypars = {
            'area': self.source_config['region'],
            'element': self.source_config['element'],
            'item': self.source_config['itemsagg']
            }
        
        self.data = faostat.get_data_df('QCL', pars=mypars, strval=False)
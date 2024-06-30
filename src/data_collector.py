from abc import ABC, abstractmethod
import pandas as pd
import logging
from .utils import load_config, fetch_data

class DataCollector(ABC):
    def __init__(self, source_name):
        self.config = load_config()
        self.source_config = self.config['data_sources'][source_name]
        self.data = None
    
    @abstractmethod
    def fetch_data(self):
        pass
    
    def save_to_csv(self, filename):
        if self.data is not None:
            self.data.to_csv(f'data/{filename}', index=False)
            logging.info(f"Data saved to data/{filename}")
        else:
            logging.error(f"No data to save for {filename}")


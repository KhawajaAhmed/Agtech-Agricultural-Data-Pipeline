from abc import ABC, abstractmethod
import pandas as pd
import logging
from .utils import load_config, fetch_data
import os

class DataCollector(ABC):
    def __init__(self, source_name):
        self.config = load_config()
        self.source_config = self.config['data_sources'][source_name]
        self.data = None
    
    @abstractmethod
    def fetch_data(self):
        pass
    
    def save_to_csv(self, filename):

        directory = 'data'
        if not os.path.exists(directory):
            os.makedirs(directory)
            logging.info(f"Directory {directory} created")

        file_path = os.path.join(directory, filename)
        if self.data is not None:
            self.data.to_csv(file_path, index=False)
            logging.info(f"Data saved to {file_path}")
        else:
            logging.error(f"No data to save for {file_path}")


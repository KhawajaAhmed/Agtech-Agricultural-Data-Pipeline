from abc import ABC, abstractmethod
import pandas as pd
import logging
from ..utils import load_config, fetch_data, log_error, log_info
import os

class DataCollector(ABC):
    def __init__(self, source_name):

        # Load the configuration from config.yaml
        self.config = load_config()

        # Extract the specific source configuration based on the source name provided
        self.source_config = self.config['data_sources'][source_name]

        self.data = None
    
    @abstractmethod
    def fetch_data(self):
        # Abstract method that must be implemented by subclasses to fetch data
        pass
    
    def save_to_csv(self, filename):

        directory = 'data'

        # Create the directory if it does not exist
        if not os.path.exists(directory):
            os.makedirs(directory)
            log_info(f"Directory {directory} created")

        file_path = os.path.join(directory, filename)
        if self.data is not None:
            self.data.to_csv(file_path, index=False)
            log_info(f"Data saved to {file_path}")
        else:
            log_error(f"No data to save for {file_path}")


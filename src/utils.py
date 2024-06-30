import requests
import logging
import yaml
from json import JSONDecodeError

# Set up logging
logging.basicConfig(
    filename='logs/app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def load_config():
    try:
        with open('config.yaml', 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError as e:
        logging.error(f"Configuration file not found: {e}")
        return {}
    except yaml.YAMLError as e:
        logging.error(f"Error parsing configuration file: {e}")
        return {}

def fetch_data(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from {url}: {e}")
        return None
    except JSONDecodeError as e:
        logging.error(f"Error decoding JSON response from {url}: {e}")
        return None

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
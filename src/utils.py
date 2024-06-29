import requests
import logging
import yaml

# Set up logging
logging.basicConfig(
    filename='logs/app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

def fetch_data(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from {url}: {e}")
        return None

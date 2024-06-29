import pandas as pd
from bs4 import BeautifulSoup
from collectors.data_collector import DataCollector
from utils import fetch_data

class IndustrySalesTrendsCollector(DataCollector):
    def __init__(self):
        super().__init__('industry_sales_trends')
    
    def fetch_data(self):
        url = self.source_config['url']
        response = fetch_data(url)
        if response:
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table')
            headers = [header.text for header in table.find_all('th')]
            rows = []
            for row in table.find_all('tr')[1:]:
                rows.append([cell.text for cell in row.find_all('td')])
            
            self.data = pd.DataFrame(rows, columns=headers)

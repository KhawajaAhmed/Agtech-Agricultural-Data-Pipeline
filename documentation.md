# Detailed Project Documentation

## Introduction
This document outlines the steps undertaken and the integration of data sources in the this project. The goal is to provide clarity on how data is collected and integrated into the project pipeline.

### Step 1: Data Collection
- **Data Collectors**: Data is collected using specialized collectors (`DataCollector` subclasses) tailored for each data source.
  - **Example**: The `IndustrySalesTrendsCollector` collects industry sales trends data from an USDA NASS API using parameters configured in `config.yaml`.

### Step 2: Data Fetching and Parsing
- **Fetch Data**: Data is fetched from external sources using HTTP requests.
  - **Example**: The `fetch_data` function in `utils.py` handles HTTP requests and error handling.

- **Parse Data**: JSON responses are parsed into pandas DataFrames for further processing.
  - **Example**: Parsed data from JSON responses is stored in pandas DataFrames within respective collector classes (`self.data`).

### Step 3: Data Conversion
- **Transformation**: Data is transformed to meet specific requirements, such as aggregating values or filtering outliers. It is converted from json_request->text->dataFrame->csv
  - **Example**: `save_to_csv` method in `DataCollector`.

## Data Source Integration

- **Add a new Data Source**
    1. Create a new subclass of `DataCollector` in the `src/collectors/` directory.
    2. Implement the `fetch_data` method for the new data source.
    3. Update `config.yaml` to include the new data source.
    4. Modify `src/main.py` to include the new data collector class.


### FAOSTAT Integration
- **Data Source**: FAOSTAT provides agricultural statistics data globally.
- **Integration**: Data integration involves querying FAOSTAT API for specific datasets (e.g., crop yield data).
  - **Example**: The `CropYieldDataCollector` integrates FAOSTAT data by querying for crop yield statistics based on configured parameters (`mypars`).

### External APIs
- **Data Source**: External APIs provide industry-specific trends and economic data. Here are the APIs used: 
    - [USDA QuickStats API](https://quickstats.nass.usda.gov/api)
    - [X API](https://developer.x.com/en/docs/twitter-api/getting-started/about-twitter-api)

- **Integration**: APIs are queried using HTTP requests with parameters from configuration files.
- **Example**: The `IndustrySalesTrendsCollector` integrates industry sales trends by fetching and parsing data from external APIs (`base_url`, `params`).

### External Libraries
- [pandas](https://pandas.pydata.org/)
- [requests](https://pypi.org/project/requests/)
- [PyYaml](https://pypi.org/project/PyYAML/)
- [faostat](https://pypi.org/project/faostat/)
- [textblob](https://textblob.readthedocs.io/en/dev/) : only if you are pulling tweets from twitter
- [tweepy](https://www.tweepy.org/) : only if you are pulling tweets from twitter

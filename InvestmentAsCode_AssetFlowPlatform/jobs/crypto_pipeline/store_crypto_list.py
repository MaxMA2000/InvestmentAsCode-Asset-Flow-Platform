# Import Loaders & Savers
from InvestmentAsCode_AssetFlowPlatform.data_processing.loaders.api_loader import ApiLoader
from InvestmentAsCode_AssetFlowPlatform.data_processing.savers.mongo_saver import MongoSaver

from InvestmentAsCode_AssetFlowPlatform.utils.common_utils import add_date_to_data

import os
os.environ["no_proxy"] = "*"

def task():
  ###########################################################
  # Load Data
  ###########################################################

  # Load the data from API
  api_loader_config = {
    "api_url": "https://financialmodelingprep.com/api/v3/symbol/available-cryptocurrencies",
    "api_key_name": "FMP_API_KEY",
    "parameters": {}
  }

  api_loader = ApiLoader(api_loader_config)
  new_data = api_loader.fetch_data()

  ###########################################################
  # Transform Data
  ###########################################################

  new_data_with_date = add_date_to_data(new_data)

  ###########################################################
  # Save Data
  ###########################################################

  # Save the data into MongoDB
  saver_config= {
      "database_name": "ingestion-general_info",
      "collection_name": "crypto_list"
  }

  saver = MongoSaver(saver_config)
  saver.replace_collection(new_data_with_date)

if __name__ == "__main__":
    task()

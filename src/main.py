from .collectors.industry_sales_trends import IndustrySalesTrendsCollector
# from .social_media_trends import SocialMediaTrendsCollector
from .collectors.crop_yield_data import CropYieldDataCollector

def main():
    print("Collecting Industry Sales Trends...")
    industry_collector = IndustrySalesTrendsCollector()
    industry_collector.fetch_data()
    industry_collector.save_to_csv('industry_sales_trends.csv')
    print("Industry Sales Trends Data Collected and Saved.")
    
    # print("Collecting Social Media Trends...")
    # social_media_collector = SocialMediaTrendsCollector()
    # social_media_collector.fetch_data()
    # social_media_collector.save_to_csv('social_media_trends.csv')
    # print("Social Media Trends data collected and saved.")

    print("Collecting Crop Yield Data..")
    crop_yield_collector = CropYieldDataCollector()
    crop_yield_collector.fetch_data()
    crop_yield_collector.save_to_csv('crop_yield_data.csv')
    print("Crop Yield Data Collected and Saved.")

if __name__ == "__main__":
    main()


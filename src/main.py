from .industry_sales_trends import IndustrySalesTrendsCollector
from .social_media_trends import SocialMediaTrendsCollector

def main():
    print("Collecting Industry Sales Trends...")
    industry_collector = IndustrySalesTrendsCollector()
    industry_collector.fetch_data()
    industry_collector.save_to_csv('industry_sales_trends.csv')
    print("Industry Sales Trends data collected and saved.")
    
    print("Collecting Social Media Trends...")
    social_media_collector = SocialMediaTrendsCollector()
    social_media_collector.fetch_data()
    social_media_collector.save_to_csv('social_media_trends.csv')
    print("Social Media Trends data collected and saved.")

if __name__ == "__main__":
    main()


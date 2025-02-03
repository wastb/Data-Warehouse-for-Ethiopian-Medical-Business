# Data Warehouse For Ethiopian Medical Business

## Overview
The EthioMedDataWarehouse project is designed to collect, clean, process, and analyze data related to Ethiopian medical businesses from various online sources like websites and Telegram channels. The project also incorporates object detection using YOLO (You Only Look Once) to enhance data analysis capabilities. The final product is a robust data warehouse that facilitates comprehensive reporting and insights into the Ethiopian medical sector.

## Business Need
This project was initiated by Kara Solutions, a leading data science company with over 50+ data-centric solutions, to build a scalable data warehouse for storing and analyzing Ethiopian medical business data. The data warehouse will support insights on trends and patterns in the medical field by processing data scraped from Telegram channels and web sources. Additionally, object detection using YOLO will be integrated to help identify specific elements within collected image data.

## Objective
### Data Scraping and Collection Pipeline
- Scrape data from public Telegram channels related to Ethiopian medical businesses using Python packages such as Telethon, Scrapy, and Selenium.
- Collect images for object detection.
### Data Cleaning and Transformation
- Clean and transform raw data using ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) processes.
- Use DBT (Data Build Tool) for data transformation and ensuring data consistency.
### Object Detection with YOLO
- Integrate YOLO for object detection within images collected from Telegram channels.
- Store and analyze object detection data for business insights.
### Data Warehouse Design and Implementation
- Design a scalable data warehouse to support efficient querying and reporting.
- Store cleaned and transformed data in a relational database (PostgreSQL).
### Data Integration and Enrichment
- Enrich scraped data by integrating multiple data sources.
- Implement pipelines to continuously update the data warehouse.

## Conclusion
The first two tasks of the project are completed:
- Medical data, including media, has been scraped from five different Telegram channels.
- The scraped data has been loaded into a PostgreSQL database.
- DBT has been successfully configured.

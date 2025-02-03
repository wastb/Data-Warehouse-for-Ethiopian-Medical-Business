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

## Installation

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/wastb/Data-Warehouse-for-Ethiopian-Medical-Business
cd EthioMedDataWarehouse
```

### 2. Install Dependencies
You will need to install the required dependencies for data scraping, processing, and object detection:

```bash
pip install -r requirements.txt
```

### 3. Set Up Database
Make sure you have PostgreSQL installed and create a new database for the project:

```bash
CREATE DATABASE telegram_raw;
```

### 4. Set Up YOLO Environment
Clone the YOLOv5 repository and install the necessary dependencies:

```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
```

### 5. Running the Project
You can run individual scripts for different tasks (scraping, data processing, etc.):

```bash
python src/scraping/telegram_scraper.py
```
## Contact Information

- **Name**: Wasihun Tesfaye
- **Email**: [wasihunpersonal@gmail.com](mailto:wasihunpersonal@gmail.com)
- **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/wasihunt/)



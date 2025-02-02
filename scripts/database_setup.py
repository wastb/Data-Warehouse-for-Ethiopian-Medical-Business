import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pandas as pd

# Ensure logs folder exists
os.makedirs("../logs", exist_ok=True)

# Configure logging to write to file & display in Jupyter Notebook
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("../logs/database_setup.log"),  # Log to file
        logging.StreamHandler()  # Log to Jupyter Notebook
    ]
)

"""# Load environment variables
load_dotenv("../.env")

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")"""

# Load environment variables from the .env file
load_dotenv()

# Get the database URL from the environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    """ Create and return database engine. """
    try:
        ### DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))  # Test connection
        logging.info("Successfully connected to the PostgreSQL database.")
        return engine
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        raise


def create_table(engine):
    """ Create telegram_messages table if it does not exist. """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS telegram_messages (
        id SERIAL PRIMARY KEY,
        channel_title TEXT,
        channel_username TEXT,
        message_id BIGINT UNIQUE,
        message TEXT,
        message_date TIMESTAMP,
        media_path TEXT,
        emoji_used TEXT,       -- New column for extracted emojis
        youtube_links TEXT     -- New column for extracted YouTube links
    );
    """
    try:
        with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as connection:
            connection.execute(text(create_table_query))
        logging.info("Table 'telegram_messages' created successfully.")
    except Exception as e:
        logging.error(f"Error creating table: {e}")
        raise

import logging
from sqlalchemy import create_engine, text

def create_table_yolo(engine):
    """ Create yolo_detection table if it does not exist. """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS yolo_detection (
        id SERIAL PRIMARY KEY,
        Image TEXT,
        Class_Id INTEGER,
        Confidence FLOAT,
        X_center FLOAT,
        Y_center FLOAT,
        Width FLOAT,
        Height FLOAT
    );
    """
    try:
        with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as connection:
            connection.execute(text(create_table_query))
        logging.info("Table 'yolo_detection' created successfully.")
    except Exception as e:
        logging.error(f"Error creating table: {e}")
        raise

def insert_data_yolo(engine, cleaned_df):
    """ Inserts YOLO detection data into PostgreSQL database. """
    try:
        insert_query = """
        INSERT INTO yolo_detection 
        (Image, Class_Id, Confidence, X_center, Y_center, Width, Height) 
        VALUES (:Image, :Class_Id, :Confidence, :X_center, :Y_center, :Width, :Height);
        """

        with engine.begin() as connection:  # ✅ Auto-commit enabled
            for _, row in cleaned_df.iterrows():
                # Debug log to ensure data is being inserted correctly
                logging.info(f"Inserting: {row['Image']} with Class ID: {row['Class_Id']}")

                connection.execute(
                    text(insert_query),
                    {
                        "Image": row["Image"],
                        "Class_Id": row["Class_Id"],
                        "Confidence": row["Confidence"],
                        "X_center": row["X_center"],
                        "Y_center": row["Y_center"],
                        "Width": row["Width"],
                        "Height": row["Height"]
                    }
                )

        logging.info(f"{len(cleaned_df)} records inserted into 'yolo_detection' table.")
    except Exception as e:
        logging.error(f"Error inserting data: {e}")
        raise

def insert_data(engine, cleaned_df):
    """ Inserts Message data into PostgreSQL database. """
    try:
        # Convert NaT timestamps to None (NULL in SQL)
        cleaned_df["message_date"] = cleaned_df["message_date"].apply(lambda x: None if pd.isna(x) else str(x))

        insert_query = """
        INSERT INTO telegram_messages 
        (channel_title, channel_username, message_id, message, message_date, media_path, emoji_used, youtube_links) 
        VALUES (:channel_title, :channel_username, :message_id, :message, :message_date, :media_path, :emoji_used, :youtube_links)
        ON CONFLICT (message_id) DO NOTHING;
        """

        with engine.begin() as connection:  # ✅ Auto-commit enabled
            for _, row in cleaned_df.iterrows():
                # Debug log to ensure data is being inserted
                logging.info(f"Inserting: {row['message_id']} - {row['message_date']}")

                connection.execute(
                    text(insert_query),
                    {
                        "channel_title": row["channel_title"],
                        "channel_username": row["channel_username"],
                        "message_id": row["message_id"],
                        "message": row["message"],
                        "message_date": row["message_date"],  # ✅ No NaT values
                        "media_path": row["media_path"],
                        "emoji_used": row["emoji_used"],
                        "youtube_links": row["youtube_links"]
                    }
                )

        logging.info(f"{len(cleaned_df)} records inserted into PostgreSQL database.")
    except Exception as e:
        logging.error(f"Error inserting data: {e}")
        raise

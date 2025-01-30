from telethon import TelegramClient
import csv
import os
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(
    filename='../logs/message_scraping.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load environment variables once
load_dotenv()
api_id = os.getenv("TG_API_ID")
api_hash = os.getenv("TG_API_HASH")
phone = os.getenv("phone")

# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer, media_dir):
    try:
        entity = await client.get_entity(channel_username)
        channel_title = entity.title  # Extract the channel's title
        async for message in client.iter_messages(entity, limit=1000):
            media_path = None
            if message.media and hasattr(message.media, 'photo'):
                # Create a unique filename for the photo
                filename = f"{channel_username}_{message.id}.jpg"
                media_path = os.path.join(media_dir, filename)
                # Download the media to the specified directory if it's a photo
                await client.download_media(message.media, media_path)
                logging.info(f"Downloaded media for message ID {message.id}.")
            
            # Write the channel title along with other data
            writer.writerow([channel_title, channel_username, message.id, message.message, message.date, media_path])
            logging.info(f"Processed message ID {message.id} from {channel_username}.")

    except Exception as e:
        logging.error(f"Error while scraping {channel_username}: {e}")

# Initialize the client once
client = TelegramClient('scraping_session', api_id, api_hash)

async def main():
    try:
    
        await client.start()
        
        # Create a directory for media files
        media_dir = '../data/photos'
        os.makedirs(media_dir, exist_ok=True)

        # Open the CSV file and prepare the writer
        with open('../data/telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])  # Include channel title in the header
            
            # List of channels to scrape
            channels = [
                    '@DoctorsET',
                    '@CheMed123',
                    '@lobelia4cosmetics',
                    '@yetenaweg',
                    '@EAHCI'
            ]
            
            # Iterate over channels and scrape data into the single CSV file
            for channel in channels:
                await scrape_channel(client, channel, writer, media_dir)
                logging.info(f"Scraped data from {channel}.")

    except Exception as e:
        logging.error(f"Error in main function: {e}")

with client:
    client.loop.run_until_complete(main())
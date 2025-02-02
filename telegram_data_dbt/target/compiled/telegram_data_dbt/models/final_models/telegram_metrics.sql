

WITH message_data AS (
    SELECT
        message_id,
        message,
        media_path,
        emoji_used,
        youtube_links,
        -- Check if the message contains media (media_path is not 'No Media')
        CASE
            WHEN media_path != 'No Media' THEN 1
            ELSE 0
        END AS has_media,
        -- Check if the message contains a YouTube link
        CASE
            WHEN youtube_links != 'No Youtube link' THEN 1
            ELSE 0
        END AS has_youtube_link,
        -- Check if the message contains YouTube links
        CASE
            WHEN message != 'No Message' THEN 1
            ELSE 0
        END AS has_message,
        -- Check if the message contains YouTube links
        CASE
            WHEN emoji_used != 'No emoji' THEN 1
            ELSE 0
        END AS has_emoji
        -- Check if the message contains YouTube links
    FROM "telegram_raw"."public"."telegram_messages"
)

SELECT
    COUNT(message_id) AS total_messages,
    SUM(has_media) AS total_media_messages,
    SUM(has_youtube_link) AS messages_with_youtube_links,
    SUM(has_emoji) AS messages_with_emoji
FROM message_data
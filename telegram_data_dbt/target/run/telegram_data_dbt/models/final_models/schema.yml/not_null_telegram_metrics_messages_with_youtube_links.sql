select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select messages_with_youtube_links
from "telegram_raw"."public"."telegram_metrics"
where messages_with_youtube_links is null



      
    ) dbt_internal_test
select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select messages_with_emoji
from "telegram_raw"."public"."telegram_metrics"
where messages_with_emoji is null



      
    ) dbt_internal_test
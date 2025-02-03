select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select total_messages
from "telegram_raw"."public"."telegram_metrics"
where total_messages is null



      
    ) dbt_internal_test
select 
  id, 
  name, 
  quotes, 
  quotes->'USD'->>'adjusted_volume_24h' as "adjusted_volume_24h" 
from {{ source('cloudquery_coinpaprika', 'coinpaprika_exchanges')}} ce 
where active

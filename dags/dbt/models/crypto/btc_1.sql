select 
  coin_id,
  timestamp,
  price,
  volume_24h,
  market_cap
from  {{ source('cloudquery_coinpaprika', 'coinpaprika_tickers')}}
order by price DESC
limit 10


with base as (
  select
  	coin_id,
	  "timestamp",
	  price,
	  dense_rank() over (partition by coin_id order by price desc)
  from  
    {{ source('cloudquery_coinpaprika', 'coinpaprika_tickers')}}
  order by
	  coin_id,
	  price desc
  )
select * from base where dense_rank <= 10

select * from {{ ref('active_exchanges')}} where adjusted_volume_24h::float >= 100000000

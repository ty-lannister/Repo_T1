Read the CSV and then calculate the percentage contribution of each product to the total revenue in the Orders.csv.
	Revenue = Quantity*Price.. 
	Write into aws db/path
 
   
  +-----+-------+-----+-------+
  |Order_id|Product|Quantity| Price |
  +-----+-------+-----+-------+
  | 1001|  A    |   10  |  5.99 |
  | 1002|  B    |   15  |  8.49 |
  | 1003|  A    |   20  |  7.99 |
  | 1004|  C    |   5   |  12.99|
  | 1005|  B    |   12  |  9.99 |
  | 1006|  D    |   8   |  6.49 |
  | 1007|  A    |   25  |  7.49 |
  | 1008|  C    |   18  |  11.99|
  +-----+-------+-----+-------+`


sol 1:
with main as (

select product, sum(quantity*price) as prod_rev from orders_tbl
group by product),

sub as (
select *,sum(prod_rev) over (order by (select null)) as basser from main)

select *,(prod_rev/basser * 100) as product_contribution from sub



sol 2: 

with main as (

select product, sum(quantity*price) as prod_rev from orders_tbl
group by product),

sub as (
select sum(prod_rev) as basser from main)

select *,(prod_rev/basser * 100) as product_contribution  from main cross join sub





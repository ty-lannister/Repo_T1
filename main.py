>> what is liquid clustering in databricks

Liquid Clustering is a Databricks Delta Lake table optimization technique where table data is organized around clustering keys in a flexible, dynamic way, adapting over time to maintain query speed.

Why it's needed
In Delta tables, we often use Partitioning and Z‑ordering but these have challenges:

Static partitions can become uneven over time (skew).
A strict sort order (like Z‑order) can be expensive to maintain if incoming data is random

What Liquid Clustering does
It dynamically manages the layout of data across the table on certain "clustering keys".
Instead of fixed partitions, it uses a liquid approach — file groups can "flow" between clusters as data changes.

-- Example: Create new Delta table with Liquid Clustering
CREATE TABLE sales (
    sale_id BIGINT,
    country STRING,
    product_id BIGINT,
    sale_date DATE,
    amount DOUBLE
)
USING DELTA
LOCATION 'dbfs:/mnt/data/sales_lc'
CLUSTER BY (country, sale_date);


-- Convert to Liquid Clustering
ALTER TABLE sales
SET TBLPROPERTIES (
    'delta.liquidClusteredColumns' = 'country,sale_date'
);


Log files are only automatically cleaned up through log retention policies, which are separate from VACUUM.

_delta_log → cleaned separately via checkpoint/log retention, controlled by:


spark.databricks.delta.logRetentionDuration = 'interval'
Default: 30 days

Auto Optimize is a capability for Delta Lake tables in Databricks that automatically optimizes As data is written to a Delta table, small files are automatically compacted into larger files.

    ALTER TABLE my_table SET TBLPROPERTIES (
  delta.autoOptimize.optimizeWrite = true,
  delta.autoOptimize.autoCompact = true
)

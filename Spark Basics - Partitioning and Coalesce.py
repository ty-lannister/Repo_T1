# Databricks notebook source
## It will give you the default partition for generating data in spark, 4 because we have 4 core cluster:
sc.defaultParallelism

# COMMAND ----------

## This will show at what size the files are splitted
spark.conf.get("spark.sql.files.maxPartitionBytes")

# COMMAND ----------

## To change the partition size:
spark.conf.set("spark.sql.files.maxPartitionBytes",[Enter the size in bytes])

# COMMAND ----------

### Here we are creating data within the spark(no external file) to see how it gets distributed in diff partitions:
data=[('Genece' , 2 , 75000),
('𝗝𝗮𝗶𝗺𝗶𝗻' , 2 , 80000 ),
('𝗣𝗮𝗻𝗸𝗮𝗷' , 2 , 80000 ),
('Tarvares' , 2 , 70000),
('Marlania' , 4 , 70000),
('Briana' , 4 , 85000),
('𝗞𝗶𝗺𝗯𝗲𝗿𝗹𝗶' , 4 , 55000),
('𝗚𝗮𝗯𝗿𝗶𝗲𝗹𝗹𝗮' , 4 , 55000),  
('Lakken', 5, 60000),
('Latoynia' , 5 , 65000) ]
schema="emp_name string,dept_id int,salary int"
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

## To check the number of partitions:
df.rdd.getNumPartitions()

# COMMAND ----------

## To see how it gets distributed in diff partitions:
df.rdd.glom().collect()

# COMMAND ----------

## We can reduce the partitions of the datafram to a sinle partition to improve performance:
df_repartitioned = df.repartition(1)
df_coalesced = df.coalesce(1)

df_repartitioned.rdd.glom().collect()

# COMMAND ----------

df1 = spark.read.option().csv('dbfs:/user/hive/warehouse/my_table/Pivot.csv')
df1.display()


# COMMAND ----------

## To see how it gets distributed in diff partitions:
df1.rdd.glom().collect()
df1.rdd.getNumPartitions()

# COMMAND ----------

# MAGIC %md
# MAGIC ***From the above output we can see that the df got generated in a sinle partition beacuse the size of file is less then 128 MB hence everything got processed in the single partition only***
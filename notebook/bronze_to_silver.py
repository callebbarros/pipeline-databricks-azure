# Databricks notebook source
# MAGIC %md
# MAGIC ##Conferindo se os dados foram montados e se temos acesso a pasta bronze

# COMMAND ----------

display(dbutils.fs.ls('/mnt/dados/bronze'))

# COMMAND ----------

# MAGIC %md
# MAGIC ##Lendo os dados na camada bronze

# COMMAND ----------

path = 'dbfs:/mnt/dados/bronze/dataset_imoveis'
dados = spark.read.format("delta").load(path)

# COMMAND ----------

display(dados)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Transformas os campos JSON em Colunas

# COMMAND ----------

df_to_col = dados.select('anuncio.*', "anuncio.endereco.*")

# COMMAND ----------

display(df_to_col)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Removendo colunas

# COMMAND ----------

df_silver = df_to_col.drop('caracteristicas', 'endereco')

# COMMAND ----------

display(df_silver)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Salvando na camada bronze

# COMMAND ----------

path_final = "dbfs:/mnt/dados/silver/dataset_imoveis"
df_silver.write.format('delta')\
    .mode('overwrite')\
    .save(path_final)

# COMMAND ----------



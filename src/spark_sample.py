from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# Criar sessão Spark
spark = SparkSession.builder.appName("DatabricksExample").getOrCreate()

# Carregar dataset (exemplo fictício)
data = [("Produto A", 1000), ("Produto B", 1500), ("Produto C", 700)]
df = spark.createDataFrame(data, ["Produto", "Vendas"])

# Transformação: sumarizar vendas
df_sum = df.groupBy("Produto").agg(sum(col("Vendas")).alias("Total_Vendas"))

# Exibir resultado
df_sum.show()
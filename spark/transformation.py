from pyspark.sql import SparkSession

if __name__ == "__main__":
        spark = SparkSession\
                .builder\
                .appName("twitter_transformation")\
                .getOrCreate()

        df = spark.read.json(
            "/home/andre-pereira/projects/data_engineer/datapipeline_twitter/datalake/twitter_aluraonline"
        )
        df.printSchema()
        df.show()
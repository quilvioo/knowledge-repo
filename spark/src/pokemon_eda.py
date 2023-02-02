## Program Notes
## 2023-01-29: Create simple Spark application to display Pokemon counts by type (descending)

# import packages
import sys

from pyspark.sql import SparkSession
import pyspark.sql.types as pytype
import pyspark.sql.functions as f

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pokemon_type <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession.builder.appName("PokemonEDA").getOrCreate()

    # read in input file
    pokemon_csv = sys.argv[1]
    pokemon_schema = pytype.StructType([pytype.StructField('PokedexNo', pytype.IntegerType(), True),
                                 pytype.StructField('Name', pytype.StringType(), True),
                                 pytype.StructField('Type 1', pytype.StringType(), True),
                                 pytype.StructField('Type 2', pytype.StringType(), True),
                                 pytype.StructField('Total', pytype.IntegerType(), True),
                                 pytype.StructField('HP', pytype.IntegerType(), True),
                                 pytype.StructField('Attack', pytype.IntegerType(), True),
                                 pytype.StructField('Defense', pytype.IntegerType(), True),
                                 pytype.StructField('Sp. Atk', pytype.IntegerType(), True),
                                 pytype.StructField('Sp. Def', pytype.IntegerType(), True),
                                 pytype.StructField('Speed', pytype.IntegerType(), True),
                                 pytype.StructField('Generation', pytype.IntegerType(), True),
                                 pytype.StructField('Legendary', pytype.BooleanType(), True)])
    pokemon_df = spark.read.csv(pokemon_csv, header=True, schema=pokemon_schema)
    pokemon_df.show(n=5, truncate=False)

    pokemon_df.cache()
    rows = pokemon_df.count()
    print(f"There are {rows} records found in the Pokedex!")
    rows_distinct = pokemon_df.select("PokedexNo").distinct().count()
    print(f"There are {rows_distinct} distinct records found!")
    pokemon_df.printSchema()

    water_types = pokemon_df.select("Name", "Type 1", "Type 2", "Total").filter(f.col("Type 1") == "Water")
    water_types.show(5, truncate=False)

    # How many water types have a second type?
    water_multi_type = water_types.select("Name", "Type 2").where(f.col("Type 2").isNotNull())
    water_multi_type_count = water_multi_type.count()
    print(f"There are {water_multi_type_count} Water Pokemon with a second type")
    water_multi_type.show(5, truncate=False)

    # What are all the distinct primary Pokemon types?
    pokemon_df.select("Type 1").distinct().show(20, False)

    # What are all the non-legendary Pokemon with Stat Totals above 600?
    new_pokemon_df = pokemon_df.withColumnRenamed("Total", "StatTotal")
    over_600 = new_pokemon_df.select("Name", "StatTotal").where(f.col("StatTotal") > 600)
    print(f"There are {over_600.count()} Pokemon with stat totals over 600")
    over_600.show(5, False)

    # What is the most common type?
    (pokemon_df
     .select("Type 1").where(f.col("Type 1").isNotNull())
     .groupBy("Type 1")
     .count()
     .orderBy("count", ascending=False)
     .show(n=10, truncate=False)
    )

    # What are the most common type pairings?
    (pokemon_df
     .select("Type 1", "Type 2")
     .where(f.col("Type 2").isNotNull())
     .groupBy("Type 1", "Type 2")
     .count()
     .orderBy("count", ascending=False)
     .show(10, truncate=False)
    )

    # What type combinations exist for Fire types?
    (pokemon_df
     .select("Type 1", "Type 2")
     .where((f.col("Type 2").isNotNull()) & (f.col("Type 1") == "Fire"))
     .distinct()
     .show(10, truncate=False)
    )

    # What is the sum, average, min, max speed for Dragon types?
    (pokemon_df
     .where(f.col("Type 1") == "Dragon")
     .select(f.sum("Speed"), f.avg("Speed"), f.min("Speed"), f.max("Speed"))
     .show()
    )

    # How many generations are present in the data file?
    pokemon_df.select("Generation").distinct().orderBy("Generation").show()

    # How many Pokemon of each type were in Generation 2?
    pokemon_df.filter(f.col("Generation") == 2).groupBy("Type 1").count().orderBy("count", ascending=False).show()

    # What type has the lowest average Total stats?
    (pokemon_df
     .select("Type 1", "Total")
     .groupBy("Type 1")
     .avg("Total")
     .orderBy("avg(Total)")
     .show()
    )


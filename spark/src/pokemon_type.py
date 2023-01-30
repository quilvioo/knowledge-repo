## Program notes
## 2023-01-29: Create simple Spark application to display Pokemon counts by type (descending)

# import packages
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import desc

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: pokemon_type <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession.builder.appName("PokemonSorter").getOrCreate()

    # read in input file
    pokemon_csv = sys.argv[1]
    pokemon_df = (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(pokemon_csv)
    )
    pokemon_df.show(n=5, truncate=False)

    # filter down to necessary columns
    pokemon_no_and_type = pokemon_df.select("#", "Type 1")
    count_pokemon_type = (
        pokemon_no_and_type.groupBy("Type 1").count().orderBy(desc("count"))
    )
    count_pokemon_type.show(truncate=False)
    print(f"Total Rows = {count_pokemon_type.count()}")

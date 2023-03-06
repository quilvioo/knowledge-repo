# Spark SQL and DataFrames

## Spark SQL and Apache Hive
* Spark allows engineers to create their own UDFs and use them directly in Spark SQL
* Spark SQL does not guarantee order of evaluation for subexpression (ex. multiple where expression)
    * As a result, make your UDFs null-aware and check nulls explicitly
    * Use `IF` or `CASE WHEN` expressions to check the `null` check and call the UDF
* Define pandas UDF (vectorized) with `pandas_udf` decorator (or wrap)  to speed up PySpark UDFs

## Querying with Spark SQL, Beeline, and Tableau
* exercises to practice with the above technologies

## External Data Sources
* Spark can return the results of a DB query as a DataFrame
* Specify your JDBC connection with the standard properties: user, password, url, dbtable, query, driver
* Partition large data by setting the following: numPartitions, partitionColumn, lowerBound, upperBound
    * best practice is using a multiple of the number of Spark workers
    * calculate lowerBound and upperBound based on the minimum and maximum partitionColumn values
    * use a partitionColumn that can distribute the data uniformly
* shows examples with common databases (Postgres, MySQL, Azure Cosmos, MS SQL Server

## Higher-Order Functions in DataFrames and Spark SQL
* explode allows you to create a new row for each element
* collect\_list returns a list of objecs with duplicates
* using the two in conjunction allows you to apply a function to a nested structure
* alternatively, you can use a UDF to map a function over the vector space
    * pro: order is preserved
    * con: order preservation is expensive
* built-in functions for complex data types: array\_distinct, array\_intersect, array\_union, array\_join,
  array\_except, max, min, position, remove, overlap, sort, concat, flatten, repeat, reverse, sequence, shuffle, slice,
  zip, element\_at, cardinality
* map functions: form\_arrays, from\_entries, concat, element\_at, cardinality
* higher order functions can use lambda functions as well
    * ex: `transform(values, value -> lambda expression)
    * `filter(array, value -> boolean expression)`
    * `exists(array, value -> boolean expression)`
    * `reduce(array, buffer, (array, buffer) -> function, buffer -> function)`

## Common DataFrames and Spark SQL Operations
* Extensive [list of operations](https://spark.apache.org/docs/latest/api/sql/index.html)
* functions for : unions, joins, windowing, modifications
* exercises for the above


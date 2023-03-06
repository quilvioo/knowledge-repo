# Apache Spark's Structured APIs

## What's Underneath an RDD?

* The RDD (Resiliant Distributed Dataset) is the underlying structure for all higher levels of Spark's functionality
* The three concepts to know with them are:
    * Dependencies: instruction to construct RDD for its inputs 
    * Partitions: split the work to parallelize computation
    * Compute functions: essentially lambda function to iterate over row objects (mapReduce)

## Structuring Spark

* By introducing high-level DSL operators code becomes far more expressive 
    * this also allows Spark to optimmize the operations
    * allows code to carry a level of similarity across languages

## DataFrame API

* similar to pandas DataFrames in concept
* objects are immutable
* support for basic (i.e. int/float/str/bool) and complex (i.e. list, dict, date) data types
* *schema* defines the column names and associated data types for a DataFrame
    * encouraged to always define your schema up-front (Spark can inferSchema if needed)
    * two ways to define the schema: programatically or using Data Definition Language (DDL) string
    ```
    # DDL string example in Python
    schema = "author STRING, title STRING, pages INT"
    ```
    * `printSchema()` will give you a nicely printed view of your schema
    * `.schema` will return your schema definition
* columns are treated much like a pandas series/column
    * can perform logical and mathematical operations on them (See [Spark documentation](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/Column.html)
* A `Row` is an object with an ordered collection of fields(columns) so we can access the field with indexing
* NOTE: you can hace Spark infer schema on a small subset of that dataframe
* `spark.read.csv()` is the function to read in a csv
* can easily save dataframe to parquet or SQL table (refer to documentation)
* *projection*: return only rows matching a certain conditinon (thinking mathematical mapping)
    * `select`, `filter`, `where`
* rename column: `withColumnRenamed` or specifying in `StructField`
* convert column types with function from `spark.sql.functions` (ex. `to_timestamp`)
* can perform SQL like aggregation using `groupBy`, `orderBy`, `count`
* can find descriptive statistice like `min`, `max`, `describe`, etc.

## Dataset API

* typed object that only make sense in Java or Scala (bc Python is dynamically typed)
* dataframe can be thought of as aliases for Dataset[Row]
* can perform transformation and actions similar to dataframes

## DataFrames vs DataSets

* in many cases they are interchangeable
* strict type safety will lead to Datasets being preferrable
* using SQL-like operations and queries, use DataFrames
* familiarity of API across components, use DataFrames
* using Python, use DataFrames
* space and speed efficiency, use DataFrames

## Spark SQL

* allows you to
    * connect to Apache Hive
    * abstraction across languages
    * read and write from structured file formats
    * interactive SQL shell
    * JDBC/ODBC connectors
    * optimize query plans
* catalyst optimizer converts it into an execution plan
* `explain(True)` to get insight on the stages the Python code goes through
* Analysis -> Logical Optimization -> Physical Planning -> Code Generation

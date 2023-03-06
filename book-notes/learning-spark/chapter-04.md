# Spark SQL and DataFrames

## Spark SQL

* engine used for Structured API (DataFrames)
* read and write structured formats (JSON, csv, etc.)
* interactive shell to execute queries
* Any `spark.sql` queries will return a dataframe, where `spark` is a `SparkSession` instance
* can use `createOrReplaceTempView()` to create a temporary view to run SQL on
    * remember you can use DDL syntax to declare schemas
* writing a query or using API operations give equivalent results

## SQL Tables and Views

* "tables hold data"
* each table has associated metadata (schema, description, table name, db name, etc)
    * all this is store in a central metastore (Apache Hive)
* Spark supports managed and unmanaged tables
    * managed tables: let Spark manage metadata AND data (file store)
    * unmanaged table: let Spark manage metadata, and you manage data
* `default` database is the default location for created tables
    * use `CREATE DATABASE` to use your own name
* `saveAsTable` by default creates a managed table
    * specify `path` option for unmanaged table
* Spark can do views just as well tables (global, session-scoped, or temporary)
* use `createOrReplaceGlobalTempView` or `createOrReplaceTempView`
* same SQL idea, once created you can run queries against views
* global temp views need to be prefixed with `global_temp`
* metadata is captured in the `Catalog` (view databases, tables, columns, etc)
* to be explored more next chapter but tables can be cached `CACHE [LAZY] TABLE`
* `spark.table` to read a table as dataframe

## Data Sources for DataFrames and SQL Tables
* `DataFrameReader` is the base for reading data from data source
    * accessed via `SparkSession.read`
* `DataFrameWriter` counterpart of `DataFrameReader` to save data to format
    * instance accesed through DataFrame
* book goes on to describe various data formats and their interactions with Spark
* interesting to call out Spark supports images as a data source

## Summary
* tables with Spark SQL and DataFrame API
* different data sources and their functionality with Spark
* `Catalog` for metadata


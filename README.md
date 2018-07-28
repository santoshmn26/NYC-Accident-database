# NYC-Accident-database
Big data project to analyze road accidents in NYC.
Project implemented using Map reduce, Hive and spark programming

## HIVE

## 1. Create a table to store the database of the file data.csv
```
create external table data (dates string, time string, location string, zip int, lat decimal, long decimal,loc string, add 	string, street string, addr2 string, street2 string, injured int, killed int, pedestraians int, pedestrians_k int, cyclist_i int, cyclist_k int, motorist_i int, motorist_k int, factor1 string, factor2 string, factor3 string, factor4 string, factor5 string, vehicle string, vehicle2 string, temp string, temp1 string, temp2 string)
row format delimited
fields terminated by ',';
```

## 2. Load the data into the table with the following command

-Note: if the data.csv file is present in the HDFS
```
load data inpath /path_of_the_file_in_hdfs into table data;
```

-Note: if the data.csv file is present in the local system
```
load data local inpath /path_of_the_file_in_local_system into table data;
```

-Or upload the data into HDFS
```
hdfs fs -copyFromLocal /path_of_the_file_in_local_system /dst_path_in_hdfs
```

-Once the data is in HDFS use the following command
```
load data inpath /path_of_the_file_in_hdfs into table data;
```
## 3. Create a table to store partitions of location
```
create table locations (dates string, time string, zip string, lat float, long float, injured int, killed int, f1 string, f2 string, f3 string, f4 string, f5 string)
```

## 4. Determine total locations avaliable in the data.csv file

```
select distinct(location) from data;
```
-Note: we can directly write the output to a file 
```
insert overwrite directory "/Path_in_HDFS" select distinct(location) from data;
```
## OUTPUT:
> 
> 0
> BOROUGH
> BROOKLYN
> MANHATTAN
> STATEN ISLAND
> BRONX
> QUEENS

Note: There are two invalid location;


## 5. Input the data into location table
Inserting data into table for location BROOKLYN
```
insert overwrite table locations partition(location="BROOKLYN") select t.dates, t.time, t.zip, t.lat, t.long, t.injured, t.killed, t.factor1, t.factor2, t.factor3, t.factor4, t.factor5 from data t where location="BROOKLYN";
```

## 6. Check the data in the table (OPTIONAL)
```
select * from locations where location="BROOKLYN" limit 5;
```




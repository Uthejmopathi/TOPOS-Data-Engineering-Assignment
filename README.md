# TOPOS-Data-Engineering-Assignment
Project Title : Web Scraping assignment for Summer Internship opportunity 2019

Motivation : To improve my programming skills in my most interested field of webscraping and data science. It is always
fascinating to learn about data science and look at what a small line fo code can perform. It is this interest of mine in the
field of data science which provided me with an internship opportunity from TOPOS for Summer 2019. I have gone through the blogs
and website of TOPOS and I am really amazed with the job performed by fellow IT workers and this really motivated me and inspired
me to obtain a job at TOPOS.

Technology : Built with Canopy and BigQuery by Google

Features : A small project which scrapes a wikipedia webpage and can be queried when uploaded into the Bigtable. BigQuery API
can be performed on these Bigtables when uploaded and yield results which cen be used for processing necessary data. The most 
standout feature of this project is that the code I have written for this assignment is pretty efficient and is just four lines
and has yielded the necessary csv file in the required.

Installation : 
1) Loading data into Big query from a local source
Open the BigQuery web UI in the GCP Console.
In the navigation panel, in the Resources section, expand your project and select a dataset.
On the right side of the window, in the details panel, click Create table. The process for loading data is the same as the process for creating an empty table.

2)Create table
On the Create table page, in the Source section:
For Create table from, select Upload.
Below Select file click Browse.

3)Browse Files
Browse to the file, and click Open. Note that wildcards and comma-separated lists are not supported for local files.
For File format, select CSV.

4)For Dataset name, choose the appropriate dataset.
Select dataset
In the Table name field, enter the name of the table you're creating in BigQuery.
Verify that Table type is set to Native table.
In the Schema section, enter the schema definition.For CSV, you can check the Auto-detect option to enable schema auto-detect.

Test : 
Once the csv table has been uploaded into the Big table. Run test using SQL Queries. I have perfromed a series of queries
and results proved my code to be working in the required and exact method.
Example1 : SELECT City FROM `nth-bucksaw-241419.TOPOS.Largecities`
          ORDER BY WaterAreakm ASC
          (This query displays the cities in ascending order according to their water area)
Example2 :SELECT Rank FROM `nth-bucksaw-241419.TOPOS.Largecities`
          WHERE City = "Fremont"
          (This Query displays the rank of the city "FREMONT" in the table)
          
How To Use:
Download the code from the repository and generate a csv file in your local system by running the code in command line or canopy etc.
Now upload this csv file into the BigTble by Google using the above steps decribed. Examine the table using the SQL queries.
 



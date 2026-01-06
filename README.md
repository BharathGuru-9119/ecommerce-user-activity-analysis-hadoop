# E-commerce User Activity Log Analysis using Hadoop Data Lake

## Description
This project analyzes e-commerce user activity logs using a Hadoop-based data lake.  
Modern e-commerce platforms generate large volumes of user interaction data such as clicks, searches, product views, and session durations. Traditional relational databases struggle to handle this scale and velocity of data. This project uses Hadoop and its ecosystem to store, process, and analyze user activity logs efficiently and extract meaningful insights.

## Problem Statement
E-commerce platforms generate massive user activity data every second. Traditional RDBMS systems are not suitable for handling high-volume, high-velocity, and semi-structured log data. A scalable and cost-effective solution is required to store and analyze this data.

## Technologies Used
- Hadoop HDFS  
- YARN  
- Apache Spark  
- Apache Hive  
- Python / PySpark  
- Flask  
- HTML, CSS, JavaScript  

## Architecture
User interactions from the e-commerce web application are captured as activity logs.  
These logs are stored in HDFS as raw data.  
Apache Spark processes and aggregates the data.  
Hive is used to query the processed data using SQL-like syntax.  
The final output is used for analytics and reporting.

## Key Features
- Distributed storage using HDFS  
- Scalable data processing  
- Clickstream and session analysis  
- SQL-based querying with Hive  
- Analytical insights for decision-making  

## Use Cases
- User behavior analysis  
- Personalization and recommendation systems  
- Product performance analysis  
- Marketing and traffic analysis  
- Business intelligence reporting  

## Conclusion
This project demonstrates how a Hadoop Data Lake can efficiently manage and analyze large-scale e-commerce user activity data. The solution provides scalability, fault tolerance, and flexibility, making it suitable for modern big data analytics applications.

## Author
Bharath Guru  
Bachelor of Engineering – Computer Science

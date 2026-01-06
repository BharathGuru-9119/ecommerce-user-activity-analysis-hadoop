# E-commerce User Log Activity Analysis using Hadoop Data Lake

## 📌 Project Overview

Modern e-commerce platforms generate a huge amount of user interaction data such as clicks, searches, product views, add-to-cart events, and session durations. Analyzing this data helps businesses understand user behavior, improve personalization, and make better business decisions.

This project uses a **Hadoop-based Data Lake** to store and process large-scale e-commerce user log data efficiently.

---

## 🎯 Problem Statement (Simple Terms)

Traditional databases struggle to handle:

* Very large volumes of user activity data
* Fast incoming data (high velocity)
* Different data formats (schema variability)

The goal of this project is to:

* Collect and store e-commerce user log data
* Process and analyze it using Hadoop
* Extract useful insights like user behavior and activity patterns

---

## 🧩 Where This Project Is Used

* User behavior analysis
* Product recommendation systems
* Website performance analysis
* Marketing and sales analytics
* Business decision-making support

---

## 🛠️ Technologies Used

* Hadoop (HDFS)
* Hive
* MapReduce (optional)
* Linux
* Java / Python (for data generation or processing)

---

## 📂 Project Structure

```
Ecommerce-User-Log-Analysis/
│
├── data/
│   ├── raw_logs/
│   └── processed_logs/
│
├── hive_queries/
│   ├── create_tables.hql
│   └── analysis_queries.hql
│
├── scripts/
│   ├── data_ingestion.sh
│   └── preprocessing.py
│
├── output/
│   └── results/
│
└── README.md
```

---

## ⚙️ How to Run the Project (Step-by-Step)

### 1️⃣ Start Hadoop Services

```bash
start-dfs.sh
start-yarn.sh
```

### 2️⃣ Create HDFS Directories

```bash
hdfs dfs -mkdir /ecommerce
hdfs dfs -mkdir /ecommerce/raw_logs
```

### 3️⃣ Upload Log Files to HDFS

```bash
hdfs dfs -put data/raw_logs/* /ecommerce/raw_logs/
```

### 4️⃣ Create Hive Tables

```bash
hive -f hive_queries/create_tables.hql
```

### 5️⃣ Run Analysis Queries

```bash
hive -f hive_queries/analysis_queries.hql
```

### 6️⃣ View Results

```bash
hdfs dfs -ls /ecommerce/output/
hdfs dfs -cat /ecommerce/output/part-00000
```

---

## 📊 Sample Insights Generated

* Most viewed products
* Peak user activity time
* Average session duration
* User engagement patterns

---

## ✅ Advantages of Using Hadoop Data Lake

* Handles large-scale data efficiently
* Supports structured and unstructured data
* Scalable and cost-effective
* Suitable for real-time and batch processing

---

## 🚀 Future Enhancements

* Integrate Spark for faster processing
* Add real-time data ingestion using Kafka
* Build dashboards using Power BI / Tableau
* Apply machine learning for recommendations

---

## 👨‍💻 Author

**Bharath Guru**
Bachelor of Engineering – Computer Science

---

## 📄 License

This project is for educational purposes only.

# 📊 Wikipedia Data Engineering Pipeline

This Python-based data engineering project extracts data from Wikipedia using Apache Airflow, processes it through a robust pipeline, and stores it in Azure Data Lake Gen2 for advanced analytics and visualization using tools like Power BI, Tableau, and Looker Studio.


---

## 🚀 Project Overview

This project demonstrates the end-to-end data engineering lifecycle:

- **Data Source**: Wikipedia
- **Ingestion**: Apache Airflow orchestrates the extraction of data.
- **Processing & Storage**: Cleaned data is pushed into Azure Data Lake Gen2.
- **ETL/ELT**: Azure Data Factory is used to transform and move data across storage layers.
- **Analytics & Modeling**: Data is accessed via Azure Synapse and Databricks for further transformation and modeling.
- **Visualization**: Final datasets are visualized using Tableau, Power BI, and Looker Studio.

---

## 🧰 Tech Stack

| Component        | Tool / Service               |
|------------------|------------------------------|
| Orchestration    | Apache Airflow (Dockerized)  |
| Storage          | Azure Data Lake Gen2         |
| ETL / ELT        | Azure Data Factory           |
| Processing       | Azure Synapse, Databricks    |
| Source           | Wikipedia (Public Dataset)   |
| Analytics        | PostgreSQL                   |
| Visualization    | Power BI, Tableau, Looker Studio |
| Containerization | Docker                       |

---

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8+
- Docker & Docker Compose
- Azure Subscription with Data Lake and Synapse access
- Access to Power BI / Tableau / Looker Studio (optional for visualization)

### Clone the Repo

```bash
git clone https://github.com/sushithks/Soccer_E2E_DE.git
cd Soccer_E2E_DE



🤝 Contributing
Contributions and suggestions are welcome! Please open an issue or submit a pull request.
import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main.data_fetch import extract_wikipedia_data, transform_wikipedia_data, write_wikipedia_data

dag = DAG(
    dag_id='wikipedia_flow',
    default_args={
        "owner": "sushith",
        "start_date": datetime(2025, 7, 14),
    },
    schedule_interval=None,
    catchup=False
)
dag_start = DummyOperator(
    task_id='dag_start',
    dag=dag)


extract_data_from_wikipedia = PythonOperator(
    task_id="extract_data_from_wikipedia",
    python_callable=extract_wikipedia_data,
    provide_context=True,
    op_kwargs={"url": "https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity"},
    dag=dag
)

transform_wikipedia_data = PythonOperator(
    task_id='transform_wikipedia_data',
    provide_context=True,
    python_callable=transform_wikipedia_data,
    dag=dag
)

write_wikipedia_data = PythonOperator(
    task_id='write_wikipedia_data',
    provide_context=True,
    python_callable=write_wikipedia_data,
    dag=dag
)

dag_end = DummyOperator(
    task_id='dag_end',
    dag=dag)

dag_start.set_downstream(extract_data_from_wikipedia)
extract_data_from_wikipedia.set_downstream(transform_wikipedia_data)
transform_wikipedia_data.set_downstream(write_wikipedia_data)
write_wikipedia_data.set_downstream(dag_end)
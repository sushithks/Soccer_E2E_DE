
from airflow import DAG

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

dag = DAG(
    dag_id='wikipedia_flow',
    default_args={
        "owner": "sushith",
        "start_date": datetime(2025, 7, 14),
    },
    schedule_interval=None,
    catchup=False
)


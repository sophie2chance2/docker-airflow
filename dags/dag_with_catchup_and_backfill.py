from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "sophie",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
    "catchup": False
}

with DAG(
    dag_id="catchup_and_backfill_dag",
    default_args=default_args,
    start_date=datetime(2023, 10, 20),
    description="DAG with catchup and backfill",
    schedule_interval="@daily"
) as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo This is a DAG with catchup and backfill"
    )
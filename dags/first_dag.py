from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "sophie",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id="first_dag_v5",
    default_args=default_args,
    start_date=datetime(2023, 10, 20),
    description="My first DAG",
    schedule_interval="@daily"
) as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo 'hello world, this is the first task'"
    )
    task2 = BashOperator(
        task_id="task2",
        bash_command="echo 'hello world, this is the second task'"
    )
    task3 = BashOperator(
        task_id="task3",
        bash_command="echo 'hello world, this is the third task'"
    )

    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # task1 >> task2
    # task1 >> task3

    task1 >> [task2, task3]
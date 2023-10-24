from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "sophie",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids="get_name", key='first_name')
    last_name = ti.xcom_pull(task_ids="get_name", key='last_name')
    age = ti.xcom_pull(task_ids="get_age", key='age')
    print(f"hello world, this is {first_name} {last_name} and I am {age} years old")

def get_name(ti):
    ti.xcom_push(key="first_name", value="sophie")
    ti.xcom_push(key="last_name", value="chance")

def get_age(ti):
    ti.xcom_push(key="age", value=25)

with DAG(
    default_args=default_args,
    dag_id="create_dag_with_py_operator_v6",
    description="My first DAG using Python Operator",
    start_date=datetime(2023, 10, 23),
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
    )
    task2 = PythonOperator(
        task_id="get_name",
        python_callable=get_name
        )
    task3 = PythonOperator(
        task_id="get_age",
        python_callable=get_age
        )
    task2 >> task3 >> task1
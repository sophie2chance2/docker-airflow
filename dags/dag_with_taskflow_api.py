from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    "owner": "sophie",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

@dag(
        dag_id="dag_with_taskflow_api_v2",
        default_args=default_args,
        start_date=datetime(2023, 10, 23),
        schedule_interval="@daily"
)
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        first_name = "sophie"
        last_name = "chance"
        return {
            "first_name": first_name,
            "last_name": last_name
        }

    @task()
    def get_age():
        age = 25
        return age

    @task()
    def greet(first_name, last_name, age):
        print(f"hello world, this is {first_name} {last_name} and I am {age} years old")

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], 
          last_name=name_dict['last_name'], 
          age=age)

greet_dag = hello_world_etl()
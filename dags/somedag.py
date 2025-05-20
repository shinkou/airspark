import datetime

from airflow.sdk import dag
from airflow.providers.standard.operators.empty import EmptyOperator


@dag(start_date=datetime.datetime(2025, 5, 1), schedule='@daily')
def generate_dag():
    EmptyOperator(task_id="task")


generate_dag()

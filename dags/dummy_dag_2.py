import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

my_dag = DAG(
    dag_id="my_dummy_dag_2",
    start_date=datetime.datetime(2023, 12, 20),
    schedule="@daily",
)

continue_op = EmptyOperator(task_id="start_task", dag=my_dag)
stop_op = EmptyOperator(task_id="stop_task", dag=my_dag)

continue_op >> stop_op

import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

my_dag = DAG(
    dag_id="my_dag_name",
    start_date=datetime.datetime(2023, 12, 1),
    schedule="@daily",
)

continue_op = EmptyOperator(task_id="start_task", dag=my_dag)
stop_op = EmptyOperator(task_id="stop_task", dag=my_dag)

continue_op >> stop_op

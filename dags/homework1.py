from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy import DummyOperator

default_args = {
    "owner": "Joe Kim",
    "start_date": timezone.datetime(2021, 9, 28)
}
with DAG(
    "homework1",
    schedule_interval="*/10 * * * *",
    default_args=default_args,
    catchup=False,
    tags=["homework"]
) as dag:
    
    taks1 = DummyOperator(task_id="1")
    task2 = DummyOperator(task_id="2")
    task3 = DummyOperator(task_id="3")
    task4 = DummyOperator(task_id="4")
    task5 = DummyOperator(task_id="5")
    task6 = DummyOperator(task_id="6")
    task7 = DummyOperator(task_id="7")
    task8 = DummyOperator(task_id="8")
    task9 = DummyOperator(task_id="9")

    taks1 >> [task2, task5] >> task6 >> task8 >> task9
    task2 >> task3 >> task4 >> task9
    task5 >> task7 >> task8 >> task9
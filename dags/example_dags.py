 import datetime

 from airflow import DAG
 from airflow.operators.empty import EmptyOperator

 with DAG(
     dag_id="example_dag",
     start_date=datetime.datetime(1999, 10, 20),
     catchup=False,
     schedule="@daily",
 ):
   
     EmptyOperator(task_id="task1")
   

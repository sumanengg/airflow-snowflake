from airflow import DAG
from airflow.operators.python_operator import PythonOperator # type: ignore
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook# type: ignore
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 13),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG('snowflake_query_dag',
          default_args=default_args,
          description='A DAG to run Snowflake queries',
          schedule_interval='@once',
          )

query = """
SELECT * FROM customers_table;
"""

snowflake_task = SnowflakeOperator(
    task_id='execute_snowflake_query',
    sql=query,
    snowflake_conn_id='snowflake_conn',  # Snowflake connection ID as configured in Airflow
    dag=dag,
)

snowflake_task

from airflow import DAG
from datetime import timedelta
from datetime import datetime as dt
from airflow.operators.bash_operator import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.email_operator import EmailOperator

default_args = {
    'owner': 'zelalem',
    'depends_on_past': False,
    'email': ['zelalemgetahun9374@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'start_date': dt(2021, 9, 13),
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'populate_data_psql',
    default_args=default_args,
    description='An Airflow DAG to populate data into postgresql',
    schedule_interval="@once",
)

# insert_I80_davis = PostgresOperator(
#     task_id='insert_I80_davis',
#     postgres_conn_id='postgres_conn_id',
#     sql='/postgresql/insert_I80_davis.sql',
#     dag=dag
# )

insert_I80_stations = PostgresOperator(
    task_id='insert_I80_stations',
    postgres_conn_id='postgres_conn_id',
    sql="/postgresql/insert_I80_stations.sql",
    dag=dag
)

insert_richards = PostgresOperator(
    task_id='insert_richards',
    postgres_conn_id='postgres_conn_id',
    sql="/postgresql/insert_richards.sql",
    dag=dag
)

insert_station_summary = PostgresOperator(
    task_id='insert_station_summary',
    postgres_conn_id='postgres_conn_id',
    sql='/postgresql/insert_station_summary.sql',
    dag=dag
)

email = EmailOperator(task_id='send_email',
                      to='zelalemgetahun9374@gmail.com',
                      subject='Daily report generated',
                      html_content=""" <h1>Congratulations! Data populated.</h1> """,
                      dag=dag
                      )

# insert_I80_davis, 
[insert_I80_stations,
    insert_richards, insert_station_summary] >> email

# [insert_I80_stations, insert_station_summary] >> email

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime as dt
from datetime import timedelta


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
    'create_tables_psql',
    default_args=default_args,
    description='An Airflow DAG to create tables in postgreSQL',
    schedule_interval='@once',
)

create_I80_davis_table = PostgresOperator(
    task_id='create_table_I80_davis',
    postgres_conn_id='postgres_conn_id',
    sql='/postgresql/I80_davis_schema.sql',
    dag=dag,
)

create_I80_stations_table = PostgresOperator(
    task_id='create_table_I80_stations',
    postgres_conn_id='postgres_conn_id',
    sql='/postgresql/I80_stations_schema.sql',
    dag=dag,
)

create_richards_table = PostgresOperator(
    task_id='create_table_richards',
    postgres_conn_id='postgres_conn_id',
    sql='/postgresql/richards_schema.sql',
    dag=dag,
)

create_station_summary_table = PostgresOperator(
    task_id='create_table_station_summary',
    postgres_conn_id='postgres_conn_id',
    sql='/postgresql/station_summary_schema.sql',
    dag=dag,
)

email = EmailOperator(task_id='send_email',
                      to='zelalemgetahun9374@gmail.com',
                      subject='Daily report generated',
                      html_content=""" <h1>Congratulations! The tables are created.</h1> """,
                      dag=dag,
                      )

[create_I80_davis_table, create_I80_stations_table,
    create_richards_table, create_station_summary_table] >> email
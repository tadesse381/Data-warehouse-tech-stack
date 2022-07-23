from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from airflow.operators.mysql_operator import MySqlOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow.utils.dates import datetime as dt
from airflow.utils.dates import timedelta
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator

import mysql.connector as mysql
from sqlalchemy import create_engine, types, text
import pandas as pd
import json

mysql_user = 'root'
mysql_password = 'root'
mysql_host = 'mysqldb'
mysql_db_name = 'dbtdb'
mysql_port = 3306

postgres_user = 'dbtuser'
postgres_password = 'pssd'
postgres_host = 'postgres-dbt'
postgres_db_name = 'dbtdb'
postgres_port = 5432

selec_batch_size = 100000

def create_mysql_connection():

    connection = f'mysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db_name}'
    engine = create_engine(connection)
    return engine

def get_record_count(table_name):
   engine = create_mysql_connection()
   conn = engine.connect()
   query = text(f'SELECT COUNT(*) FROM {table_name}')
   result = conn.execute(query)
   return result.fetchone()[0]


def load_to_postgres(mysql_df, table_name):
    mysql_df.columns= mysql_df.columns.str.lower()
    conn_str = f'postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db_name}'
    engine = create_engine(conn_str)
    mysql_df.to_sql(table_name.lower(), con=engine, index=False, if_exists='append')
    


def get_src_table_names():
   engine = create_mysql_connection()
   conn = engine.connect()
   query = text(f'show tables')
   result = conn.execute(query)
   return result



def migrate(**kwargs):
    table_name = kwargs['table_name']

    engine = create_mysql_connection()
    row_count = get_record_count(f'{table_name}')

    cur = 0
    while cur < row_count :
        query = f'select * from {table_name} Limit {cur}, {selec_batch_size}'
        result_df = pd.read_sql(query, con=engine)
        load_to_postgres(result_df, table_name)
        cur += selec_batch_size
    print("select statment finished")

default_args = {
    'owner': 'zelalem',
    'depends_on_past': False,
    'email': ['zelalemgetahun9374@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'start_date': dt(2021, 9, 25),
    'retry_delay': timedelta(minutes=5)
}



dag = DAG(
    'data_migration_to_postgres',
    default_args=default_args,
    description='A data migration dag from mysql to postgresql',
    schedule_interval='@once',
    # schedule_interval='*/ * * * *'
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




migrate_station_summary = PythonOperator(
    task_id=f'migrate_station_summary',
    python_callable=migrate,
    op_kwargs={'table_name': 'station_summary' },
    dag=dag
)

migrate_I80Stations = PythonOperator(
    task_id=f'migrate_station_metadata',
    python_callable=migrate,
    op_kwargs={'table_name': 'I80Stations' },
    dag=dag
)

migrate_richards = PythonOperator(
    task_id=f'migrate_observation',
    python_callable=migrate,
    op_kwargs={'table_name': 'richards' },
    dag=dag
)
    

create_I80_stations_table >> migrate_I80Stations
create_richards_table >> migrate_richards 
create_station_summary_table >> migrate_station_summary
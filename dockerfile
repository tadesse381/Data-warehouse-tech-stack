FROM python:3.8
RUN pip install 'apache-airflow[postgres]==2.1.4' && pip install dbt
RUN pip install SQLAlchemy
RUN pip install apache-airflow-providers-postgres
RUN pip install apache-airflow-providers-mysql
RUN pip install dbt-mysql
RUN pip install mysql-connector-python
RUN pip install pandas
RUN pip install pymysql

RUN mkdir /project
COPY scripts_airflow/ /project/scripts/
COPY dbt/profiles.yml /root/.dbt/profiles.yml
RUN chmod +x /project/scripts/init.sh
ENTRYPOINT [ "/project/scripts/init.sh" ]

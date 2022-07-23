# Data-warehouse-tech-stack
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](#)

A fully dockerized scalable ELT pipeline using MySQL, Airflow, DBT and Redash.


### Built With

Tech Stack used in this project
* [MYSQL](https://mysql.com)
* [Apache Airflow](https://airflow.apache.org/)
* [dbt](https://www.getdbt.com/)
* [Redash](https://redash.io/)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Make sure you have docker installed on local machine.
* Docker
* DockerCompose
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/zelalemgetahun9374/sensor-data-ELT.git
   ```
2. Run
   ```sh
    docker-compose build
    docker-compose up
   ```
3. Open Airflow web browser
   ```JS
   Navigate to `http://localhost:8010/` on the browser
   activate and trigger the `create_tables` dag
   activate and trigger the `populate_data` dag
   activate and trigger the `dbt_dag` dag
   ```
4. Access redash dashboard
   ```JS
   Navigate to `http://localhost:5000/` on the browser
   ```
5. Access your mysql database using adminer
   ```JS
   Navigate to `http://localhost:8090/` on the browser
   use `mysqldb` for server
   use `root` for username
   use `root` for password
   Watch for dbdtdb and analytics databses
   ```

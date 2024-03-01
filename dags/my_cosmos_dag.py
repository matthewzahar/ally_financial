from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping
import os
from airflow.datasets import Dataset
import pendulum

# use local profile
profile_config = ProfileConfig(
    profile_name="ally",
    target_name="dev",
    profiles_yml_filepath=f"{os.environ['AIRFLOW_HOME']}/dags/dbt/profiles.yml",
)

# single dag with several task groups for each model
my_cosmos_dag = DbtDag(
    project_config=ProjectConfig(
        "/usr/local/airflow/dags/dbt",
    ),
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",
    ),
    # normal dag parameters
    schedule=[Dataset("source.ally.btc.coinpaprika_tickers")],
    start_date=pendulum.datetime(2023, 2, 1, tz="America/New_York"),
    catchup=False,
    dag_id="my_cosmos_dag",
    default_args={"retries": 2},
)

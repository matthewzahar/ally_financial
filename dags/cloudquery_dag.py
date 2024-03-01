import json
import pendulum
import subprocess
import os

from airflow.datasets import Dataset
from airflow.decorators import dag, task

@dag(
    schedule_interval='@daily', # run it daily
    start_date=pendulum.datetime(2024, 2, 1, tz="America/New_York"),
    catchup=False,
    tags=["example"],
)
def run_cloudquery():
    # single task to run the cloudquery cli in airflow
    @task(outlets=[Dataset("source.ally.btc.coinpaprika_tickers")])
    def call_sync(): 
        commands = [f"{os.environ['AIRFLOW_HOME']}/./cloudquery", "sync", "conf.yml", "postgres.yml"]
        subprocess.run(commands, capture_output=True, text=True)
    call_sync()

run_cloudquery()


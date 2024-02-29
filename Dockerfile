FROM quay.io/astronomer/astro-runtime:10.4.0

RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-sqlite && deactivate

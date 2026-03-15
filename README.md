# OptiChain - Supply Chain Intelligence Platform (Cloud-ready MLOps)

OptiChain is a production-style ML platform for demand forecasting (28-day horizon)
and inventory optimization.

## Stack

- Python
- MLflow
- FastAPI
- Docker
- Airflow orchestration
- Prometheus and Grafana monitoring

## Quickstart

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1

make install
make test
make lint
make api
```

Health endpoint: http://127.0.0.1:8000/health

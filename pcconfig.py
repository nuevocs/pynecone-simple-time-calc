import os
import pynecone as pc

fast_api_url = os.environ.get('FASTAPI_URL')
fast_api_port = os.environ.get('PORTS_API')
# api_url = "http://192.168.3.82:27210"




config = pc.Config(
    app_name="pynecone_simple_time_calc",
    # api_url="http://192.168.3.82:27210",
    api_url=f"http://{fast_api_url}:{fast_api_port}",
    bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    # telemetry_enabled=False,
    # env=pc.Env.DEV,
)

import os
import pynecone as pc

fast_api_url = os.environ.get('FASTAPI_URL')
fast_api_port = os.environ.get('PORTS_API')

config = pc.Config(
    app_name="pynecone_simple_time_calc",
    api_url=f"http://{fast_api_url}:{fast_api_port}",
    bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    # telemetry_enabled=False,
    # env=pc.Env.DEV,
)

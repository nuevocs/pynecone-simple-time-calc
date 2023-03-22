import os
import pynecone as pc

api_url = os.getenv('API_URL')
# api_url = "http://192.168.3.82:27210"
api_url2 = f'"{api_url}"'


config = pc.Config(
    app_name="pynecone_simple_time_calc",
    # api_url="http://192.168.3.82:27210",
    api_url=api_url2,
    bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    # telemetry_enabled=False,
    # env=pc.Env.DEV,
)

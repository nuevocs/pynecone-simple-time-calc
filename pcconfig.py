import os
import pynecone as pc

# api_url = os.getenv('API_URL')
# api_url = f'"{api_url}"'

api_url = "http://192.168.3.82:27210"

config = pc.Config(
    app_name="pynecone_simple_time_calc",
    # api_url="http://192.168.3.82:27210",
    api_url=api_url,
    bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    # telemetry_enabled=False,
    # env=pc.Env.DEV,
)

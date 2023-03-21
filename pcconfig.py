import os
import pynecone as pc

# api_url = os.getenv('TEST_VAR')

config = pc.Config(
    app_name="pynecone_simple_time_calc",
    # api_url=api_url,
    api_url="http://192.168.0.1:8000",
    bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    telemetry_enabled=False,
    # env=pc.Env.DEV,
)

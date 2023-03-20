import os
import pynecone as pc
# from dotenv import load_dotenv
#
# load_dotenv()

config = pc.Config(
    app_name="pynecone_simple_time_calc",
    # api_url="http://192.168.3.100:2721",
    api_url=ACCESS_API_URL,
    bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    telemetry_enabled=False,
    # env=pc.Env.DEV,
)

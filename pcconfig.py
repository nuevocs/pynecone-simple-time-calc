import os
import pynecone as pc

mode = os.environ.get('PC_APP_MODE')
local_ip = os.environ.get('FASTAPI_URL_LOCAL_IP')
fast_api_url = os.environ.get('FASTAPI_URL')
fast_api_port = os.environ.get('PORTS_API')

if mode == "PROD":
    config = pc.Config(
        app_name="pynecone_simple_time_calc",
        # api_url=f"https://{fast_api_url}",
        api_url=f"http://{local_ip}:{fast_api_port}",
        bun_path="/app/.bun/bin/bun",
        db_url="sqlite:///pynecone.db",
        # telemetry_enabled=False,
        # env=pc.Env.DEV,
    )

elif mode == "DEV":
    config = pc.Config(
        app_name="pynecone_simple_time_calc",
        api_url=f"http://{local_ip}:{fast_api_port}",
        bun_path="/app/.bun/bin/bun",
        db_url="sqlite:///pynecone.db",
        # telemetry_enabled=False,
        # env=pc.Env.DEV,
    )

else:
    config = pc.Config(
        app_name="pynecone_simple_time_calc",
        api_url=f"http://{local_ip}:{fast_api_port}",
        bun_path="/app/.bun/bin/bun",
        db_url="sqlite:///pynecone.db",
        # telemetry_enabled=False,
        # env=pc.Env.DEV,
    )


# config = pc.Config(
#     app_name="pynecone_simple_time_calc",
#     api_url=f"http://{fast_api_url}:{fast_api_port}",
#     bun_path="/app/.bun/bin/bun",
#     db_url="sqlite:///pynecone.db",
#     # telemetry_enabled=False,
#     # env=pc.Env.DEV,
# )

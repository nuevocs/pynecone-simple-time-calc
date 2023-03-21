import pynecone as pc

config = pc.Config(
    app_name="pynecone_simple_time_calc",
    # api_url="http://192.168.3.100:27210",
    api_url="http://localhost:8000",
    bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    telemetry_enabled=False,
    # env=pc.Env.DEV,
)

import pynecone as pc

config = pc.Config(
    app_name="pynecone_simple_time_calc",
    # api_url="0.0.0.0:8000",
    env=pc.Env.DEV,
    bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    # env=pc.Env.DEV,
    telemetry_enabled=False,
)

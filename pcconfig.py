import pynecone as pc


config = pc.Config(
    app_name="pynecone_simple_time_calc",
    api_url="http://130.29.55.100/:8000",
    bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    # env=pc.Env.DEV,
)

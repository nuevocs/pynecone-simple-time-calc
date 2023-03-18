import pynecone as pc


config = pc.Config(
    app_name="pynecone_simple_time_calc",
    api_url="0.0.0.0:8000",
    bun_path="/pynecone_simple_time_calc/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)

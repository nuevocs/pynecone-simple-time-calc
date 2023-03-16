import pynecone as pc


config = pc.Config(
    app_name="pynecone_simple_time_calc",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)

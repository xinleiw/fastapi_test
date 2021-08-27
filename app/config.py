import os
from dynaconf import Dynaconf  # type: ignore

config = Dynaconf(
    envvar_prefix="MATRIX",
    load_dotenv=True,
    environments=True,
    env_switcher="CONTEXT_FOR_EXTRACT",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    settings_files=[os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.yaml")],
)

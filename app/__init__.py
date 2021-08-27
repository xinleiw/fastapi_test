import os

from app.config import config
from app.lib.logging import init_log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLITE_URI = f"sqlite:///{os.path.join(BASE_DIR, config.SQLITE_PATH)}"
logger = init_log("matrix", f"{BASE_DIR}/logs/matrix")

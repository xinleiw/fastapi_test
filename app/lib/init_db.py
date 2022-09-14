import os
from app import BASE_DIR, SQLITE_URI
from alembic import config, command
from app.lib.logging import init_log

logger = init_log("db", f"{BASE_DIR}/logs/init_db")


def init_database(sql_url=SQLITE_URI):
    try:
        alembic_config_path = os.path.join(BASE_DIR, "alembic.ini")
        logger.info(f"alembic config file is {alembic_config_path}")
        cfg = config.Config(alembic_config_path)
        cfg.attributes["configure_logger"] = False
        cfg.set_main_option("sqlalchemy.url", sql_url)
        cfg.set_main_option("script_location", "alembic")
        command.upgrade(cfg, "head")
        logger.info(f"alembic upgrade success")
    except Exception as e:
        logger.error(f"更新数据库失败， 失败原因： {e}", exc_info=True)
        raise
    return

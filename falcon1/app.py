from falcon1.Utils.ConfigUtils import init_configs; init_configs()
from falcon1.Utils.DBUtils import init_db; init_db()
from falcon1.routes import get_app

application = get_app()

from airiflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator
from airflow.hooks.base_hook import BaseHook

class SqlOperator(BaseOperator):
    algo

class SqlHook(BaseHook):
    algo

class SqlPlugin(AirflowPlugin):
    name = 'sql_plugin'
    operators = [SqlOperator]
    hooks = [SqlHook]
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []


# Una vez guardado el archivo en la carpeta de plugins, podemos llamar a los nuevos objetos
# de la siguiente manera:

    # from airflow.operators.sql_plugin import SqlOperator
    # from airflow.hooks.sql_plugin import SqlHook
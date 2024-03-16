from pathlib import Path
import sqlfluff
from sqlfluff.core import FluffConfig

config_path = '.sqlfluff'

with open(config_path, 'r') as f:
    config_str = f.read()
    config = FluffConfig.from_string(config_str)


def format_sql(request) -> dict:
    """
    request経由でSQLを受け取り、SQLを整形して返す

    Args:
        request (_type_): ブラウザからのリクエスト。'sql'キーに整形したいSQLが入っている

    Returns:
        dict: 整形されたSQLが入った辞書
    """
    request_json = request.get_json()
    sql = request_json['sql']
    formattedSql = sqlfluff.fix(sql, config=config) # type: ignore
    violations = sqlfluff.lint(sql, config=config) # type: ignore
    
    response = {
        'formattedSql': formattedSql,
        'violations': violations
    }
    
    return response

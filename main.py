from pathlib import Path
import sqlfluff

BASE_DIR = Path(__file__).resolve().parent
config_file_path = BASE_DIR / '.sqlfluff'

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
    fixed_sql = sqlfluff.fix(sql, config=config_file_path) # type: ignore
    
    return {'formattedSql': fixed_sql}

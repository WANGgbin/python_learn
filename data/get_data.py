import pkgutil

def visit_local_config():
    data = pkgutil.get_data(__package__, "./local_config.yml")
    return data
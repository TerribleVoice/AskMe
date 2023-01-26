from sqlalchemy.engine import URL


def make_pg_url(user: str, password: str, host: str, name: str, port: int) -> URL:
    drivername = 'postgresql'
    url = URL.create(drivername=drivername, username=user, password=password, host=host, port=port,
                     database=name)
    return url
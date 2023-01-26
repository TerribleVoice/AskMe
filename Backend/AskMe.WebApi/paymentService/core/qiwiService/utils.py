from datetime import datetime, timedelta, timezone


def create_datetime_link_and_expiration(delay):
    values = datetime.utcnow().replace(microsecond=0, tzinfo=timezone.utc)
    datetime_link = f":{values:%Y-%m-%d-%H-%M-%S}-UTC"
    datetime_expiration = values + timedelta(minutes=delay)
    datetime_expiration = datetime_expiration.isoformat()
    return datetime_link, datetime_expiration

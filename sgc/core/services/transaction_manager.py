from django.db import transaction, connection
from contextlib import contextmanager

class TransactionManager:
    @contextmanager
    def atomic(self):
        with connection.cursor() as cursor:
            try:
                yield cursor
                connection.commit()
            except Exception:
                connection.rollback()
                raise
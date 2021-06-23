from django.db import connection
from contextlib import closing

def get_courses():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""fgdghdf""")

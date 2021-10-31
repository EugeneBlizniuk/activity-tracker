import os
import sqlite3
from typing import Dict, List

connection = sqlite3.connect(os.path.join("db", "activity-tracker-db.sqlite"))
cursor = connection.cursor()


def insert(table: str, column_values: Dict):
    """Insert incoming value"""
    columns = ", ".join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
    cursor.executemany(
        f"insert into {table} "
        f"({columns}) "
        f"values ({placeholders})",
        values)
    connection.commit()


def get_all(table: str, columns: List[str]) -> List[Dict]:
    """Return all rows"""
    joined_columns = ", ".join(columns)
    cursor.execute(f"select {joined_columns} from {table}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


def delete(table: str, row_id: int):
    """Delete row by its id"""
    cursor.execute(f"delete from {table} where id={row_id}")
    connection.commit()


def _init_db():
    """Activity Tracker database initialization"""
    with open("db/createdb.sql", "r") as file:
        sql = file.read()
    cursor.executescript(sql)
    connection.commit()


def check_db_exists():
    """Check if the required database actually exists, initialize if it does not"""
    cursor.execute("select name from sqlite_master "
                   "where type='table' and name='activity'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


check_db_exists()

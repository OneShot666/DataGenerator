from math import *
from random import *
from time import *


class DataRequestsGiver:
    def __init__(self):
        pass

    @staticmethod
    def get_all_attributes_request(table_name):
        return f"PRAGMA table_info({table_name});"

    @staticmethod
    def get_all_tables_request():
        return f"SELECT name FROM sqlite_master WHERE type='table';"

    @staticmethod
    def get_add_table_requests(table_name, table_attributes):
        request = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for att in table_attributes:
            request += att
        request += ");"
        return request

    @staticmethod
    def get_insert_data_request(table_name, attributes):
        attributes = list(attributes)
        request = f"INSERT INTO {table_name} {attributes} VALUES ("
        for _ in range(len(attributes)):
            request += "?, "
        request += ")"
        return request

    @staticmethod
    def get_select_data_request(table_name, attributes="*"):
        request = f"SELECT {attributes} FROM {table_name}"
        return request

    @staticmethod
    def get_delete_data_request(table_name, attributes):
        request = f"DELETE FROM {table_name} WHERE "
        for att in attributes:
            request += f"{att}=?, "
        return request

    @staticmethod
    def __get_request(request):                                                   # Ctrl + D this
        return request

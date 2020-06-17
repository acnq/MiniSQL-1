import Catalog
import Index
import time


# import RecordManager


def initialize(path: str):
    Catalog.__initialize__(path)
    Index.__initialize__(path)


def save():
    Catalog.__finalize__()
    Index.__finalize__()
    print("All tables have been saved.")


# an example of upcoming args
# S
# [{'attribute_name': 'ID', 'type': 'int', 'type_len': 0, 'unique': True},
# {'attribute_name': 'name', 'type': 'char', 'type_len': 12, 'unique': True},
# {'attribute_name': 'age', 'type': 'int', 'type_len': 0, 'unique': False},
# {'attribute_name': 'gender', 'type': 'char', 'type_len': 1, 'unique': False}]
# ID
def create_table(table_name: str, attributes: list, pk: str):
    time_start = time.time()
    Catalog.exists_table(table_name)
    Index.create_table(table_name)
    Catalog.create_table(table_name, attributes, pk)
    time_end = time.time()
    print("Successfully create table '%s', time elapsed : %fs." %
          (table_name, time_end - time_start))


# e.g. name_index S name
# FAKE!
def create_index(index_name: str, table_name: str, indexed_attr: str):
    Catalog.exists_index(index_name)
    Catalog.create_index(index_name, table_name, indexed_attr)
    Index.create_index(index_name, table_name, indexed_attr)


def drop_table(table_name: str):
    time_start = time.time()
    Catalog.not_exists_table(table_name)
    Catalog.drop_table(table_name)
    Index.delete_table(table_name)
    time_end = time.time()
    print("Successfully drop table '%s', time elapsed : %fs." %
          (table_name, time_end - time_start))


def drop_index(index_name: str):
    Catalog.not_exists_index(index_name)
    Catalog.drop_index(index_name)


# e.g.
# student
# ['*']
# [{'operator': '>', 'l_op': 'sage', 'r_op': 20},
# {'operator': '=', 'l_op': 'sgender', 'r_op': 'F'},
# {'operator': '<', 'l_op': 'sscore', 'r_op': 89.5}]
def select(table_name: str, attributes: list, where: list = None):
    time_start = time.time()
    Catalog.not_exists_table(table_name)
    Catalog.check_select_statement(table_name, attributes, where)
    Index.select_from_table(table_name, attributes, where)
    time_end = time.time()
    print(" time elapsed : %fs." % (time_end - time_start))


# e.g. student ['12345678', 'wy', 22, 'M']
def insert(table_name: str, values: list):
    time_start = time.time()
    Catalog.not_exists_table(table_name)
    Catalog.check_types_of_table(table_name, values)
    Index.insert_into_table(table_name, values)
    time_end = time.time()
    print(" time elapsed : %fs." % (time_end - time_start))


# e.g. student [{'operator': '=', 'l_op': 'sno', 'r_op': '88888888'}]
def delete(table_name: str, where: list = None):
    time_start = time.time()
    Catalog.not_exists_table(table_name)
    Catalog.check_select_statement(table_name, ['*'], where)  # 从insert中借用的方法
    Index.delete_from_table(table_name, where)
    time_end = time.time()
    print(" time elapsed : %fs." % (time_end - time_start))


def show_table(table_name: str):
    pass
    # Catalog.exist_table(table_name)
    # Catalog.show_table(table_name) # 显示属性名、类型、大小（char）、是否unique、是否主键、index情况等等


def show_tables():
    pass
    # Catalog.show_tables() # 列出所有表名
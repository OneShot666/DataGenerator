import sys
from math import *
from random import *
from time import *
from requests import DataRequestsGiver
import sqlite3


# [v0.0.1] Structure of the project
# [v0.0.2] Make basics functions
# ... [v0.0.3] Create real database and test all functions
# [v0.0.4] Add class to manage requests
# ! [v0.0.5] Make table a class (params as attributes) ?
# ! [v0.0.6] Add menu to use functions (ask user)
# ! [v0.0.7] Add graphics interface for menu (use tkinter ?)
# ! [v1.0.0] Final tasks to complete project
class DataGenerator:
    def __init__(self):
        # Project data
        self.name = "DataGenerator"
        self.creator = "One Shot"
        self.version = "v0.0.4"
        self.birthday = "12/10/12024"
        # Database data
        self.DATABASE = None
        self.database_name = "Étres vivants"
        self.database_filename = "etres_vivants.db"
        self.database_tables = ["Végétaux", "Animaux", "Champignons", "Microorganismes"]
        self.date_format = "%d%m%Y"
        # requests data
        self.REQUESTER = DataRequestsGiver()
        # Main functions
        self.run()

    def run(self):                                                              # Main function
        self.create_database()
        self.close_program()

    def menu(self):
        pass

    def change_current_database(self):
        self.database_name = input("Entrer le nom de la base de données actuelle : ")
        self.database_filename = input("Entrer le nom du fichier de la base (format db) : ")
        self.database_filename += ".db" if not self.database_filename.endswith(".db") else ""
        self.create_database()

    def display_database(self):
        pass

    def check_data_correct(self):                                               # Browses database + check if data correct
        pass

    def create_database(self):                                                  # Connect to a database
        print(f"Création de la base de données '{self.database_name}'...")
        self.DATABASE = sqlite3.connect(self.database_filename)                 # Create if doesn't exist

    def modify_database(self):
        pass

    def remove_database(self):
        pass

    def add_table(self, table_name, attributes):
        cursor = self.DATABASE.cursor()
        cursor.execute(self.REQUESTER.get_add_table_requests(table_name, attributes))
        self.DATABASE.commit()
        print(f"Table '{table_name}' créée avec les attributs : {attributes}")

    def modify_table(self):
        pass

    def remove_table(self):
        pass

    def get_data(self, table_name, attributes):
        cursor = self.DATABASE.cursor()
        cursor.execute(self.REQUESTER.get_select_data_request(table_name, attributes))
        return cursor.fetchall()

    def add_data(self, table_name, attributes, values):
        cursor = self.DATABASE.cursor()
        cursor.execute(self.REQUESTER.get_insert_data_request(table_name, attributes), values)
        self.DATABASE.commit()
        print(f"Données dans '{table_name}' ajoutées avec les attributs : {attributes}")

    def modify_data(self):
        pass

    # Ex: table_name="user", attributes=(name, age), conditions=("John", 30)
    def remove_data(self, table_name, attributes, conditions):
        cursor = self.DATABASE.cursor()
        cursor.execute(self.REQUESTER.get_delete_data_request(table_name, attributes), conditions)
        self.DATABASE.commit()
        print(f"Données dans '{table_name}' supprimées pour les attributs : {attributes}")

    def close_program(self):
        print(f"Fermeture de '{self.name}'...")
        self.DATABASE.close()
        sys.exit()


if __name__ == "__main__":
    main = DataGenerator()

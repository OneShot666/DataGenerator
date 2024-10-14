import math
import os.path
import sys
from math import *
from random import *
from time import *
from requests import DataRequestsGiver
from pathlib import Path
import sqlite3

# ! Refine some functions (messages display to user or some case study)
# ! Fill empty functions (or search if useless)
# ! Test all functions in test.py (use test directory)


# [v0.0.1] Structure of the project
# [v0.0.2] Make basics functions
# ... [v0.0.3] Create real database and test all functions
# [v0.0.4] Add class to manage requests
# ... [v0.0.5] Add menu to use functions (ask user)
# ! [v0.0.6] Make table a class (params as attributes) ?
# ! [v0.0.7] Make menu a class ?
# ! [v0.0.8] Add graphics interface for menu (use tkinter ?)
# ! [v0.0.9] Add parameters
# ! [v1.0.0] Final tasks to complete project
class DataGenerator:
    def __init__(self):
        # Project data
        self.name = "DataGenerator"
        self.creator = "One Shot"
        self.version = "v0.0.4"
        self.birthday = "12/10/12024"
        # Path data
        self.local_path = Path(__file__).parent.parent                          # Current program path
        self.Directories = ["src", "db", "test"]
        self.code_dirname = "src"
        self.db_dirname = "db"
        # Menu data
        self.Menus = ["Menu", "Base de données", "Tables", "Données", "Quitter"]
        self.SubMenus = ["Sous-menu", "Ajouter", "Modifier", "Supprimer", "Retour"]
        self.menu_location = self.Menus[0]
        # Database data
        self.DATABASE = None
        self.db_name = "Étres vivants"                                          # ! Later : change to None
        self.db_filename = "etres_vivants.db"                                   # ! Later : change to None
        self.DbTables = ["Végétaux", "Animaux", "Champignons", "Microorganismes"]   # ! Later : change to []
        # Rules data
        self.date_format = "%d%m%Y"
        self.number_min = 0
        self.number_max = math.inf
        # Requests data
        self.REQUESTER = DataRequestsGiver()
        # Parameters data
        self.param_autosave = True                                              # ! Use later
        self.param_collect_cookies = True                                       # Can't be modified
        # Main functions
        self.create_directories()
        self.run()

    def create_directories(self):
        for directory in self.Directories:
            if not os.path.exists(f"{self.local_path}/{directory}"):
                os.makedirs(f"{self.local_path}/{directory}")

    def run(self):                                                              # Main function
        print(f"Lancement de '{self.name}'...")
        self.create_database()
        self.display_database()
        self.close_program()

    def menu(self):                                                             # ! Later : Choices for user
        current_menu = None
        if self.menu_location == self.Menus[0]:
            current_menu = self.Menus
        elif self.menu_location == self.SubMenus[0]:
            current_menu = self.SubMenus

        print(current_menu[0])
        for i, m in enumerate(current_menu[0::]):
            print(f"{i} - {m}")

    def change_current_database(self):                                          # Connect to another database
        self.db_name = input("Entrer le nom de la base de données actuelle : ")
        self.db_filename = input("Entrer le nom du fichier de la base (format db) : ")
        self.db_filename += ".db" if not self.db_filename.endswith(".db") else ""
        self.create_database()

    def display_database(self):                                                 # Display db on console (tkinter later)
        Tables = self.get_all_tables()
        Attributes = []
        for table in Tables:
            Attributes.append(self.get_all_attributes(table))
        print(f"{self.db_name} : ")
        for i, table in enumerate(Tables):
            print(f"- {table} : {Attributes[i]}")

    def check_data_correct(self):                                               # Browses database + check if data correct
        pass

    def create_database(self):                                                  # Connect to a database
        print(f"Création de la base de données '{self.db_name}'...")
        path = f"{self.local_path}/{self.db_dirname}/{self.db_filename}"
        self.DATABASE = sqlite3.connect(path)                                   # Create if doesn't exist

    def modify_database(self):
        pass

    def remove_database(self):                                                  # Delete a database
        pass

    def get_all_attributes(self, table_name):                                   # Return attributes from a tables
        cursor = self.DATABASE.cursor()
        cursor.execute(self.REQUESTER.get_all_attributes_request(table_name))
        Columns = cursor.fetchall()
        return [col[1] for col in Columns]

    def get_all_tables(self):                                                   # Return tables from a current db
        cursor = self.DATABASE.cursor()
        cursor.execute(self.REQUESTER.get_all_tables_request())
        Tables = cursor.fetchall()
        return [table[0] for table in Tables]

    def add_table(self, table_name, attributes):                                # Add a table in the current db
        cursor = self.DATABASE.cursor()
        cursor.execute(self.REQUESTER.get_add_table_requests(table_name, attributes))
        self.DATABASE.commit()
        print(f"Table '{table_name}' créée avec les attributs : {attributes}")

    def modify_table(self):
        pass

    def remove_table(self):                                                     # Delete a table from the current db
        pass

    # ! Add condition ("*" or true by default)
    def get_data(self, table_name, attributes):                                 # Return data from a given table
        cursor = self.DATABASE.cursor()
        cursor.execute(self.REQUESTER.get_select_data_request(table_name, attributes))
        return cursor.fetchall()

    def add_data(self, table_name, attributes, values):                         # Add data in a given table
        cursor = self.DATABASE.cursor()
        cursor.execute(self.REQUESTER.get_insert_data_request(table_name, attributes), values)
        self.DATABASE.commit()
        print(f"Données dans '{table_name}' ajoutées avec les attributs : {attributes}")

    def modify_data(self):
        pass

    # Ex: table_name="user", attributes=(name, age), conditions=("John", 30)
    def remove_data(self, table_name, attributes, conditions):                  # Delete data from a given table
        cursor = self.DATABASE.cursor()
        cursor.execute(self.REQUESTER.get_delete_data_request(table_name, attributes), conditions)
        self.DATABASE.commit()
        print(f"Données dans '{table_name}' supprimées pour les attributs : {attributes}")

    def close_program(self):                                                    # Exit the program
        print(f"Fermeture de '{self.name}'...")
        self.DATABASE.close()
        sys.exit()


if __name__ == "__main__":
    main = DataGenerator()

import sqlite3

conn = sqlite3.connect('trameDSI_info.db')

cursor = conn.cursor()


# cursor.execute("""CREATE TABLE Writers (Info text, Writer_Name text, File_Extension text)""")

# reader_info: list =[
# ("Oceans11Datacard loads in metadata describing a dataset to be stored in the oceans11 DSI data server (oceans11.lanl.gov). Input format is YAML","Oceans11Datacard",".yaml"),
# ("DublinCoreDatacard loads in a dataset's metadata which conforms to Dublin Core. Input format is XML","DublinCoreDatacard",".xml"),
# ("SchemaOrgDatacard loads in a dataset's metadata which conforms to schema.org. Input format is JSON","SchemaOrgDatacard",".json"),
# ("Schema loads in a complex JSON schema that describes tables relations for a structured relational database like Sqlite and DuckDB.","Schema",),
# ("Bueno captures performance data from Bueno (github.com/lanl/bueno). Input format is a dictionary in a text file ending in .data","Bueno",".data"),
# ("Csv loads in data from CSV files that can only be for one table in each separate call","Csv",".csv"),
# ("YAML1 loads in data from YAML files of a particular structure","YAML1",".yaml"),
# ("TOML1 loads in data from TOML files of a particular structure","TOML1",".toml"),
# ("Ensemble loads in data from a CSV file and generates a simulation table alongside it. Each row of data should be a separate simulation run","Ensemble",".csv"),
# ("JSON loads in data from JSON files that can only be for one table in each separate call","JSON",".json")
# ]       



# cursor.execute("""INSERT INTO Readers VALUES ("Oceans11Datacard loads in metadata describing a dataset to be stored in the oceans11 DSI data server (oceans11.lanl.gov). Input format is YAML","Oceans11Datacard",".yaml"),
# ("DublinCoreDatacard loads in a dataset's metadata which conforms to Dublin Core. Input format is XML","DublinCoreDatacard",".xml"),
# ("SchemaOrgDatacard loads in a dataset's metadata which conforms to schema.org. Input format is JSON","SchemaOrgDatacard",".json"),
# ("Schema loads in a complex JSON schema that describes tables relations for a structured relational database like Sqlite and DuckDB.","Schema",".json"),
# ("Bueno captures performance data from Bueno (github.com/lanl/bueno). Input format is a dictionary in a text file ending in .data","Bueno",".data"),
# ("Csv loads in data from CSV files that can only be for one table in each separate call","Csv",".csv"),
# ("YAML1 loads in data from YAML files of a particular structure","YAML1",".yaml"),
# ("TOML1 loads in data from TOML files of a particular structure","TOML1",".toml"),
# ("Ensemble loads in data from a CSV file and generates a simulation table alongside it. Each row of data should be a separate simulation run","Ensemble",".csv"),
# ("JSON loads in data from JSON files that can only be for one table in each separate call","JSON",".json")
               
               
#                """)         

conn.commit()

#cursor.execute("""DROP TABLE Info_for_Writers
    #           """)


#conn.commit()

#cursor.execute("""ALTER TABLE Info_for_Readers ADD Reader_Name text""")

#conn.commit()

#cursor.execute("""INSERT INTO Info_for_Writers VALUES 
   #("ER_Diagram creates an image of an ER Diagram based on data stored in DSI."),
   #("Table_Plot generates a plot of a specified table's numerical data that is stored in DSI."),
   #("Csv_Writer creates a CSV of a specified table whose data is stored in DSI.") 
 #  """) 
 
#cursor.execute("""INSERT INTO Info_for_Readers (Reader_Name) VALUES
                
    #    ("Oceans11Datacard"),
     #   ("DublinCoreDatacard"),
      #  ("SchemaOrgDatacard"),
        #("Schema"),
       # ("Bueno"),
        #("Csv"),
        #("YAML1"),
        #("TOML1"),
        #("Ensemble"),
        #("JSON")
                
         #       """)





cursor.execute("""INSERT INTO Writers VALUES

("ER_Diagram creates an image of an ER Diagram based on data stored in DSI.","ER_Diagram",".png, .pdf, .jpg, .jpeg"),
("Table_Plot generates a plot of a specified table's numerical data that is stored in DSI.", "Table_Plot", ".png, .jpg, .jpeg"),
("Csv_Writer creates a CSV of a specified table whose data is stored in DSI.", "Csv_Writer",".csv")
""")

conn.commit()

conn.close()

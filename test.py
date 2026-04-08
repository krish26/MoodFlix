import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=moodflix1.database.windows.net,1433;"
    "DATABASE=free-sql-db-1196900;"
    "UID=agasya;"
    "PWD=Koumudi@26;"
    "Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=60;"
)
print("Connected!")
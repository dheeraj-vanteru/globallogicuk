import json
import mysql.connector

db_connection = mysql.connector.connect(
  host="mysql_container",
  user="dev",
  passwd="123456",
  database="devopstt"
)
db_cursor = db_connection.cursor(dictionary=True)

def test_version():
    db_cursor.execute("SELECT max(version) as version FROM versionTable;")
    resultVersion = db_cursor.fetchone()
    f = open('test/expecteddbstate/versionTable.json')
    version = json.load(f)
    assert resultVersion == version

def test_appTable():
    db_cursor.execute(f"SELECT * FROM appTable;")
    result = db_cursor.fetchone()
    print(result)
    fileoutput = open("test/expecteddbstate/appTable.json")
    test = json.load(fileoutput)
    assert result == test

def test_someTable():
    db_cursor.execute(f"SELECT * FROM someTable;")
    result = db_cursor.fetchone()
    print(result)
    fileoutput = open("test/expecteddbstate/someTable.json")
    test = json.load(fileoutput)
    assert result == test
    
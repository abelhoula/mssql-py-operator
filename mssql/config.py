import pyodbc
import typer

from mssql import ERRORS
def mmsqlconx(server: str, database: str, username: str, password: str = None, port: int = None, lock: bool = True):

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
    try:
        dsn = 'tcp:'+server+','+str(port)
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+dsn+';DATABASE='+database+';UID='+username+';PWD='+ password)
    except pyodbc.Error as ex:
        typer.echo(f"{ERRORS[1]}")
        raise typer.Exit()
    
    return cnxn

def disablelogin(login,cnxn):
    """disable a given login"""    
    cursor = cnxn.cursor()
    cursor.execute("Alter Login "+ login +" disable;")
    cnxn.commit()
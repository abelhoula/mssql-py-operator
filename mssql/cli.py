"""This module provides the mssql To-Do CLI."""
# mssql/cli.py

from typing import Optional
import pyodbc 
import csv
import typer

from mssql import __app_name__, __version__

app = typer.Typer()

@app.command()
def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.command()
def check(server: str = None, database: str = None, username: str = None, password:str = None, port: int = None):
    """Show all logins where the password was changed within 364 days and set to never expire"""
    print("tcp:"+server+"1433")
    test = mssqlCheck(server,database,username,password,port)


def mssqlCheck(server: str, database: str, username: str, password: str = None, port: int = None):
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
    header = ['name', 'is_expiration_checked']
    dsn = 'tcp:'+server+','+str(port)
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+dsn+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    #-- Show all logins where the password was changed within the last day (for testing purpose)
    cursor.execute("SELECT name, is_expiration_checked FROM sys.sql_logins WHERE LOGINPROPERTY([name], 'PasswordLastSetTime') > DATEADD(dd, -1, GETDATE()) and is_expiration_checked = 0;") 
    row = cursor.fetchone()
    #report
    f = open('report.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    while row:
        print(row[0])
        writer.writerow(row)
        row = cursor.fetchone()

        
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    app()
    return

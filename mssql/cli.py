"""This module provides the mssql To-Do CLI."""
# mssql/cli.py

from typing import Optional
import csv
from csv import DictReader
import typer

from mssql import __app_name__, __version__, config

app = typer.Typer()

@app.command()
def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.command()
def check(server: str = None, database: str = None, username: str = None, password:str = None, port: int = None, lock: bool = None):
    """Show all logins where the password was changed within 364 days and set to never expire"""

    header = ['name', 'is_expiration_checked']
    #get db conex
    cursor = config.mmsqlconx(server,database,username,password,port).cursor()

    #-- Show all logins where the password was changed within the last day (for testing purpose)
    cursor.execute("SELECT name, is_expiration_checked FROM sys.sql_logins WHERE LOGINPROPERTY([name], 'PasswordLastSetTime') > DATEADD(dd, -12, GETDATE()) and is_expiration_checked = 0 and is_disabled = 0;") 
    logins = cursor.fetchone()

    #report
    f = open('report.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    while logins:
        print(logins[0])
        writer.writerow(logins)
        logins = cursor.fetchone()
    f.close()
    cursor.close()

    if lock:
        with open('report.csv', 'r') as sql_logins:
            csv_dict_reader = DictReader(sql_logins)
            for row in csv_dict_reader:
                print("locked ===> "+row['name'])
                config.disablelogin(row["name"], config.mmsqlconx(server,database,username,password,port))
        
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

"""Top-level package for mssql To-Do."""
# mssql/__init__.py

__app_name__ = "mssql operator"
__version__ = "0.1.0"

(
    SUCCESS,
    DB_CONECT_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

ERRORS = {
    DB_CONECT_ERROR: "conection to sql server error ",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    ID_ERROR: "to-do id error",
}
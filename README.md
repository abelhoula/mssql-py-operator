# Dev env setup

1) Setup Python vituall enviroment
    ```bash
      cd mssql-py/
      python3 -m venv ./venv
      source venv/bin/activate
    ```

 2) Install deps
 
    ```bash
     python -m pip install -r requirements.txt
    ```
 3) Run tests
    ```bash
       pytest
    ```

 # Setup Local sql server 2019 with docker
 pwd: mssql-pass1
port: 1433

1) Prepare sql server 2019 instance with docker

    ```bash
    docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=mssql-pass1" -p 1433:1433 --name mssql -d mcr.microsoft.com/mssql/server:2019-CU14-ubuntu-20.04
    ```
2) Connect to sql server

   ```bash
   docker exec -it mssql /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P mssql-pass1
   ```
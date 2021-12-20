CREATE LOGIN test1 WITH PASSWORD = 'Pass+pass!pass'
CREATE LOGIN test2 WITH PASSWORD = 'Pass+pass!pass'
CREATE LOGIN test3 WITH PASSWORD = 'Pass+pass!pass'
CREATE LOGIN test4 WITH PASSWORD = 'Pass+pass!pass'
GO

SELECT LOGINPROPERTY('sa', 'PasswordLastSetTime');
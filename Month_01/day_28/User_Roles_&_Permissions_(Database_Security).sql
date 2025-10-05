use SalesDB
go

-- Create a New Login

Create Login test_user with password = 'Test@1234';

-- Create Database User from Login

Create user Test_user For Login test_user;

-- Grant Read Access (db_datareader)

Alter role db_datareader Add Member Test_user;

-- Grant Write Access (db_datawriter)

Alter role db_datawriter Add member Test_user;

-- Revoke Permissions

REVOKE SELECT ON dbo.sale TO Test_user;

-- Deny Specific Permission

DENY DELETE ON dbo.sale TO Test_user;

-- Check Current Permissions

EXECUTE AS USER = 'Test_user';
SELECT * FROM fn_my_permissions('dbo.Sale', 'OBJECT');
REVERT;

EXEC sp_helpuser 'Test_user';




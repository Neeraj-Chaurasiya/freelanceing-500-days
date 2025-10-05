
# 📘 Day 28 – SQL User Roles & Permissions (Detailed Notes)

---

## 🧾 Step 1: Use Database

```sql
use SalesDB
go
```
👉 Selects the database `SalesDB` where users and permissions will be managed.

---

## 🏗️ Step 2: Create a New Login

```sql
Create Login test_user with password = 'Test@1234';
```
- `Login` → SQL Server level account.  
- Password is required to authenticate.  
- This login allows connection to SQL Server, but not access to specific database yet.

---

## 🏗️ Step 3: Create Database User from Login

```sql
Create user Test_user For Login test_user;
```
- Maps server login `test_user` to a **database user** inside `SalesDB`.  
- This user can now access the database subject to permissions.

---

## 🏗️ Step 4: Grant Read Access (db_datareader)

```sql
Alter role db_datareader Add Member Test_user;
```
- `db_datareader` → Predefined role that allows **SELECT** on all tables in the database.  
- `Add Member` → Assign `Test_user` to this role.  

---

## 🏗️ Step 5: Grant Write Access (db_datawriter)

```sql
Alter role db_datawriter Add member Test_user;
```
- `db_datawriter` → Predefined role that allows **INSERT, UPDATE, DELETE** on all tables.  
- Assigns write access to `Test_user`.

---

## 🏗️ Step 6: Revoke Permissions

```sql
REVOKE SELECT ON dbo.sale TO Test_user;
```
- Revokes previously granted SELECT permission **specifically on `sale` table**.  
- Overrides any broader role permissions if needed.

---

## 🏗️ Step 7: Deny Specific Permission

```sql
DENY DELETE ON dbo.sale TO Test_user;
```
- Deny takes priority over grant.  
- Prevents `Test_user` from deleting rows in `sale` table, even if `db_datawriter` role allows it.

---

## 🧪 Step 8: Check Current Permissions

```sql
EXECUTE AS USER = 'Test_user';
SELECT * FROM fn_my_permissions('dbo.Sale', 'OBJECT');
REVERT;
```
- `EXECUTE AS USER` → Temporarily switch context to check permissions.  
- `fn_my_permissions` → Shows effective permissions on the object `dbo.Sale`.  
- `REVERT` → Return to original user context.

---

## 🧪 Step 9: List Database User Info

```sql
EXEC sp_helpuser 'Test_user';
```
- Displays info about `Test_user`, including roles and permissions in the database.

---

## ✅ Summary Table

| Command | Purpose |
|---------|---------|
| CREATE LOGIN | Server-level authentication account |
| CREATE USER | Map login to database user |
| ALTER ROLE ADD MEMBER | Assign role-based permissions (read/write) |
| REVOKE | Remove granted permission |
| DENY | Explicitly deny a permission |
| EXECUTE AS | Test permissions as another user |
| sp_helpuser | List user and role information |

💡 **Key Points**
- Roles simplify permission management (readers/writers).  
- DENY overrides any granted permission.  
- Always test user permissions before deployment.

---

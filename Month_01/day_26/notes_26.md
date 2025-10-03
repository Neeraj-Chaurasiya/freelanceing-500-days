# Day 26 – SQL Transactions & ACID Properties (Detailed Notes)

---

## 1️⃣ Transactions Basics

```sql
use SalesDB
go

-- Start a Transaction
Begin Transaction;
 Insert into customers (Name,City) Values ('Ravi','Delhi');
 Insert into sale (Product, Category,Price, Quantity, CustomerId) Values
 ('Laptop','Electronics',55000, 1, 5);

 Commit;
```

### Explanation:
- `Begin Transaction;` → Ek nayi transaction shuru hoti hai.
- `Insert into customers...` → Customer add kiya gaya hai.
- `Insert into sale...` → Us customer ki ek sale record add kiya gaya hai.
- `Commit;` → Dono operations **permanently database me save** ho gaye.  
👉 Agar beech me error hota to rollback use kar sakte the.

---

## 2️⃣ Rollback Example

```sql
 Begin Transaction;

 Update sale
 Set Price = Price * 0.5
 Where Product = 'Laptop';

 Rollback;
```

### Explanation:
- Transaction start hua.
- `Update` se Laptop ka price 50% kam kiya.
- `Rollback;` → Changes undo ho gaye. Database apne purane state pe wapas aa gaya.

---

## 3️⃣ Savepoint Example

```sql
 Begin transaction;

 Insert into customers (Name,City) values ('Priya','Mumbai')
 Save Transaction SavePoint1;
 
 Insert into customers (Name,City) values ('Amit','Kolkata');

 RollBack Transaction Savepoint1;
 Commit;
```

### Explanation:
- `Save Transaction SavePoint1;` → Ek checkpoint create kiya.
- Uske baad Amit add hua tha.
- `Rollback Transaction SavePoint1;` → Wapas savepoint tak rollback ho gaya → Priya add hui rahegi, Amit ka insert undo ho gaya.
- `Commit;` → Jo changes bache the (Priya ka insert) permanently save ho gaye.

---

## 4️⃣ Isolation Example

```sql
 Set Transaction Isolation Level Read Committed;
 Begin Transaction;
 Select * From sale Where  Product = 'Laptop';

 select * from sale
```

### Explanation:
- `Set Transaction Isolation Level Read Committed;` → Ye level ensure karta hai ki ek transaction dusre ke **uncommitted (dirty) data** ko read nahi karega.
- Matlab sirf wahi data read hoga jo commit ho chuka hai.
- Ye concurrency control ke liye use hota hai.

---

## 🔑 ACID Properties Recap

- **Atomicity** → Transaction ya to fully complete hogi ya fully fail hogi (Rollback support karta hai).
- **Consistency** → Database hamesha valid state me rahega.
- **Isolation** → Parallel transactions ek dusre ke beech interfere nahi karenge.
- **Durability** → Commit ke baad data permanent save ho jata hai, crash hone par bhi.

---

## ✅ Summary

- **Transaction control commands**: `BEGIN`, `COMMIT`, `ROLLBACK`, `SAVEPOINT`
- **Rollback** → Changes ko undo karta hai.
- **Savepoint** → Partial rollback ke liye checkpoints.
- **Isolation Levels** → Concurrency ke liye safety rules.
- **ACID Properties** → Reliable transactions ke 4 main rules.

---

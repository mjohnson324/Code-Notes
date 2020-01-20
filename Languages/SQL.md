# SQL

"Normalize until it hurts, denormalize until it works"
~ A very wise person

**Transaction**- A distinct unit of work against a database treated in a reliable way

Data Operations:

1. Create (Insert)
INSERT INTO _table_
VALUES _values_
1. Read (Select) - Core Structure:
SELECT _columns_ (expressions) DISTINCT *DISTINCT and expressions applied after HAVING clause
FROM _table_ AS _alias_
(RIGHT/LEFT) (INNER/OUTER) JOIN _table_ AS _alias_ ON _foreign_key_
WHERE (rows matching condition)
GROUP BY _column_ *aggregation
HAVING (rows matching condition)
ORDER BY _column_
OFFSET _number_from_top_
LIMIT _number_
3. Update
UPADTE _table_
SET _column_x_, _column_y_, VALUES = x, y
WHERE (rows matching conditions)
4. Delete

Other keywords: Avg, Between, In, Like, Count, etc.

* Null is not like False as it does not equal itself. Use IS NULL or IS NOT NULL for null checks

* Database indices improve read performance but slow other types of transactions. Use sensibly.

* Correlated Subquery- Subqueries reference column/table names from outer queries
* Relational Database- Database that tracks the relationships between data
* Schema- A description of a database's tables and their respective columns
* Foreign Key- ID in a table pointing to a row in another table
* Join Table- ID table for establishing many-to-many relationships between entities
* Pivot Table- Summarizes data from another table
* SQL Injection- When an extra query is added to retrieve unintended data. A hacker exploit

## Useful PSQL Commands

* `\l` to list databases
* `\dt` to list tables
* `\d` _table_ to list columns and types
* `\dg` to list roles

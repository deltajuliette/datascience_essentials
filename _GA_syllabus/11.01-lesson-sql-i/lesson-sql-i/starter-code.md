# SQL I

## `SELECT` and `FROM`

SQL we read data from a database. The two primary clauses that must be present in every query are `SELECT` and `FROM`.

- What columns do you want (`SELECT`)?
- and `FROM` which table?

```SQL
-- Returns all columns (*) from a table called "users"
SELECT *
FROM users;
```

We will use the `ncaa_basketball` data within Google's [BigQuery](https://cloud.google.com/bigquery/).

Challenges:

- Return all the columns from the `mascots` table.

We can also get a subset of the columns from a table.

```SQL
-- Returns ONLY the name and age columns from the users table
SELECT name, age
FROM users;
```

Challenges:

- Return the `market` and `mascot_name` columns from the `mascots` table.
- Give me the colors of all the teams

## Namespacing & Aliasing

Namespacing is when you prepend the table name to the column name in your `SELECT` clause. This is overkill when you’re querying one table, but is crucial when querying from multiple tables.

```SQL
SELECT users.name, users.salary
FROM users;
```

You can also namespace the wildcard.

```SQL
SELECT users.*
FROM users;
```

Namespacing the full table name can get cumbersome. Thankfully, we can alias our table names similar to Python imports (e.g. `import pandas as pd`).

Aliasing in SQL looks like this:

```SQL
SELECT u.name, u.salary
FROM users AS u;
```

Challenges (play around with namespacing and aliasing):

- Return the `market` and `mascot_name` columns from the `mascots` table
- Give me every column from the `mascots` table
- Query the `season` and `status` columns from the `mbb_games_sr` table

You can also alias column names. Similar to aliasing tables, this won't permanently change the column name. Aliasing only affects your views.

```SQL
-- Returns the name column (aliased as "user") from users table.
SELECT u.name AS user
FROM users AS u;
```

Challenges:

- Show me the `scheduled_date` (temporarily renamed to `date`) from the `mbb_games_sr` table
- Give me all the mascot names, alias the `mascot_name` column as `name`

## `DISTINCT`

`DISTINCT` returns a list of **unique** values from a given column:

```SQL
-- Returns the only the unique university names (i.e. no duplicates)
SELECT DISTINCT u.university
FROM users u;
```

Challenges:

- Show me the unique seasons (renamed to `year`) from the `mbb_games_sr` table.
- From the `mbb_teams` table, query the unique values from the `market` column

## `ORDER BY`

Sometimes it makes sense to order your query on a certain column. For example, we might want to get a list of users sorted alphabetically:

```SQL
SELECT users.name
FROM users
ORDER BY users.name ASC;
```

Challenges:

- Show me the `name` (temporarily renamed to `team`) and `venue_capacity` columns from the `mbb_teams` table, ordered from highest capacity to least
- Give me all the `names` in alphabetical order.
- Retrieve all the columns from `mascots` in reverse alphabetical order by mascot name

You can order on multiple columns. Priority is given from left to right in your `ORDER BY` clause.

```SQL
-- Returns users from oldest to youngest. If they're the same age, then sort alphabetically
SELECT u.name, u.age
FROM users u
ORDER BY u.age DESC, u.name ASC
```

Challenges:

- Give me the `last_name` (renamed to `name`), `height` and `jersey_number` from `mbb_players_games_sr`. Order first by `height` from biggest to smallest, then by `jersey_number` from smallest to biggest

## `LIMIT`

Rather than returning everything from a given table, you can request a specific number of rows. This is done with `LIMIT`.

```SQL
-- Returns the top ten highest paid users
SELECT users.name, users.salary
FROM users
ORDER BY users.salary DESC
LIMIT 10
```

Challenges:

- Give me the first and last names of the 10 tallest players from the `mbb_players_games_sr` table.
- What is the last player by `last_name` alphabetically (limit to 1 result)

## Query Order

Your SQL clauses have to be in a specific order, otherwise you'll throw an exception.

1. `SELECT`
2. `FROM`
3. `WHERE`
4. `GROUP BY`
5. `HAVING`
6. `ORDER BY`
7. `LIMIT`

Mnemonic: "Smelly Feet Will Give Horrible Odors, Lingeringly"

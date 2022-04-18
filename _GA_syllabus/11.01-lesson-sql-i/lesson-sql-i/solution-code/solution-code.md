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

Challenges:_(share in thread or try directly on bigquery)_

- Return all the columns from the `mascots` table.

```SQL
SELECT *
FROM `bigquery-public-data.ncaa_basketball.mascots`;
```

We can also get a subset of the columns from a table.

```SQL
-- Returns ONLY the name and age columns from the users table
SELECT name, age
FROM users;
```

Challenges:_(share in thread or try directly on bigquery)_

- Return the `market` and `mascot_name` columns from the `mascots` table.

```SQL
SELECT market, mascot_name
FROM `bigquery-public-data.ncaa_basketball.mascots`;
```

- Give me the colors of all the teams

```SQL
SELECT color
FROM `bigquery-public-data.ncaa_basketball.team_colors`;
```

## Namespacing & Aliasing

Namespacing is when you prepend the table name to the column name in your `SELECT` clause. This is overkill when you’re querying one table, but is crucial when querying from multiple tables.

```SQL
SELECT users.name, users.salary
FROM users;
```

You can also namespace the wildcard to select all columns from the table.

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

Challenges (play around with namespacing and aliasing):_(share in thread or try directly on bigquery)_

- Return the `market` and `mascot_name` columns from the `mascots` table

```SQL
SELECT m.market, m.name
FROM `bigquery-public-data.ncaa_basketball.mascots` AS m;
```

- Give me every column from the `mascots` table

```SQL
SELECT m.*
FROM `bigquery-public-data.ncaa_basketball.mascots` AS m;
```

- Query the `season` and `status` columns from the `mbb_games_sr` table

```SQL
SELECT g.season, g.status
FROM `bigquery-public-data.ncaa_basketball.mbb_games_sr` AS g;
```

You can also alias column names. Similar to aliasing tables, this won't permanently change the column name. Aliasing only affects your views.

```SQL
-- Returns the name column (aliased as "user") from users table.
SELECT u.name AS user
FROM users AS u;
```

Challenges: _(share in thread or try directly on bigquery)_

- Show me the `scheduled_date` (temporarily renamed to `date`) from the `mbb_games_sr` table

```SQL
SELECT g.scheduled_date as date
FROM `bigquery-public-data.ncaa_basketball.mbb_games_sr` AS g;
```

- Give me all the mascot names, alias the `mascot_name` column as `name`

```SQL
SELECT m.mascot_name as name
FROM `bigquery-public-data.ncaa_basketball.mascots` AS m;
```

## `DISTINCT`

`DISTINCT` returns a list of **unique** values from a given column:

```SQL
-- Returns only the unique university names (i.e. no duplicates)
SELECT DISTINCT u.university
FROM users u;
```

Challenges:_(share in thread or try directly on bigquery)_

- Show me the unique seasons (renamed to `year`) from the `mbb_games_sr` table.

```SQL
SELECT DISTINCT season as year
FROM `bigquery-public-data.ncaa_basketball.mbb_games_sr`;
```

- From the `mbb_teams` table, query the unique values from the `market` column

```SQL
SELECT DISTINCT market
FROM `bigquery-public-data.ncaa_basketball.mbb_teams`;
```

## `ORDER BY`

Sometimes it makes sense to order your query on a certain column. For example, we might want to get a list of users sorted alphabetically:

```SQL
SELECT users.name
FROM users
ORDER BY users.name ASC;
```

Challenges:_(share in thread or try directly on bigquery)_

- Show me the `name` (temporarily renamed to `team`) and `venue_capacity` columns from the `mbb_teams` table, ordered from highest capacity to least

```SQL
SELECT name as team, venue_capacity
FROM `bigquery-public-data.ncaa_basketball.mbb_teams`
ORDER BY venue_capacity DESC;
```

- Same table: Retreive all the columns sorted by `name` in alphabetical order.

```SQL
SELECT *
FROM `bigquery-public-data.ncaa_basketball.mbb_teams`
ORDER BY name
```

- Retrieve all the columns from `mascots` in reverse alphabetical order by mascot name

```SQL
SELECT *
FROM `bigquery-public-data.ncaa_basketball.mascots`
ORDER BY mascot_name DESC
```

You can order on multiple columns. Priority is given from left to right in your `ORDER BY` clause.

```SQL
-- Returns users from oldest to youngest. If they're the same age, then sort alphabetically
SELECT u.name, u.age
FROM users u
ORDER BY u.age DESC, u.name ASC
```

Challenges:_(share in thread or try directly on bigquery)_

- Give me the `last_name` (renamed to `name`), `height` and `jersey_number` from `mbb_players_games_sr`. Order first by `height` from biggest to smallest, then by `jersey_number` from smallest to biggest

```SQL
SELECT last_name as name, height, jersey_number
FROM `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
ORDER BY height DESC, jersey_number 
```

## `LIMIT`

Rather than returning everything from a given table, you can request a specific number of rows. This is done with `LIMIT`.

```SQL
-- Returns the top ten highest paid users
SELECT users.name, users.salary
FROM users
ORDER BY users.salary DESC
LIMIT 10
```

Challenges:_(share in thread or try directly on bigquery)_

- Give me the first and last names of the 10 tallest players from the `mbb_players_games_sr` table.

```SQL
SELECT DISTINCT first_name, last_name, height
FROM `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
ORDER BY height DESC
LIMIT 10;
```

- What is the last player by `last_name` alphabetically (limit to 1 result)

```SQL
SELECT DISTINCT first_name, last_name, height
FROM `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
ORDER BY last_name DESC
LIMIT 1;
```

## Query Order

Your SQL clauses have to be in a specific order, otherwise you'll throw an exception.

1. `SELECT`
2. `FROM`
3. `WHERE` # filter:yet to cover
4. `GROUP BY` # aggregating:yet to cover
5. `HAVING` # filter post aggregating:yet to cover
6. `ORDER BY`
7. `LIMIT`

Mnemonic: "Smelly Feet Will Give Horrible Odors, Lingeringly"

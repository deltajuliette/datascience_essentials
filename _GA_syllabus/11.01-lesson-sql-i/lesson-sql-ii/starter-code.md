# SQL II

## `WHERE`

One of the more important skills in SQL is the ability to filter your queries based a certain condition. This is accomplished with the `WHERE` command.

```SQL
-- Returns all users who make less than $30k
SELECT users.*
FROM users
WHERE users.salary < 30000
```

Numerical filters are similar to python:

- Greater than: `>`
- Greater than or equal to: `>=`
- Less than: `<`
- Less than or equal to: `<=`
- Equal to: `=`

### Challenges

- Give me the `name` and `points_game` of `mbb_historical_teams_games` with more than 163 points. Order your results by points; largest to smallest

## `AND`/`OR`

Multiple `WHERE` clauses can be chained together with `AND` and `OR`, similar to chaining multiple boolean expressions in Python.

```SQL
-- Returns all users under the age of 30 who earn more than $100k
SELECT users.*
FROM users
WHERE users.age < 30
AND users.salary > 100000
```

### Challenges

- Give me all `name` and `win` of `mbb_historical_teams_games` where `points_game` was over 150 points or having _at least_ 77,612 in `attendance`.
- Same table (`mbb_historical_teams_games`). Give me the `opp_name` and `opp_points_game` of the Bulldogs (`opp_code` = 813) with 90 or more `opp_points_game`. Sort your results by `opp_points_game` (ASC).**

## Filtering on String Values

When filtering on a string value, use single quotes:

```SQL
SELECT users.*
FROM users
WHERE users.role = 'admin'
```

### Challenges

- Find Petey from the `mascots` table.

## Wildcards

We can use `LIKE` and wildcards (%) to broaden our string filters:

```SQL
-- Returns all users whose name begins with a capital "R"
SELECT users.*
FROM users
WHERE users.name LIKE 'R%'
```

```SQL
-- Returns all users whose name ends with a capital "R"
SELECT users.*
FROM users
WHERE users.name LIKE '%R'
```

```SQL
-- Returns all users with a capital "R" somewhere in the name
SELECT users.*
FROM users
WHERE users.name LIKE '%R%'
```

Notes:

- `ILIKE` is a case insensitive `LIKE`. (Note: available in PostgreSQL, not in others)
- You can negate a `LIKE` with `NOT LIKE`.

### Challenges

- Find all the mascot names that start with the letter `P`.

## Null values

Databases can have null values. You can filter them like so:

```SQL
-- Returns all users with no name
SELECT users.*
FROM users
WHERE users.name IS NULL
```

```SQL
-- Returns all users with a value for their name
SELECT users.*
FROM users
WHERE users.name IS NOT NULL
```

### Challenges

- Give me everything from the mascots table with null values in the `mascot_common_name` column.

## Joining Tables

It's very common to want to combine information from multiple tables into one query.

For example, we might want to find the user's name for a given blog post. We can do this by joining.

```SQL
-- Returns all blog posts with the associated user name.
-- A user has many posts, and a post belongs to a user. Therefore the foreign key (user_id)
-- is on the child table: posts.
SELECT posts.*, users.name
FROM posts
INNER JOIN users ON users.id = posts.user_id
```

There are several types of joins:

- Inner join. This is the most common type of join.
- Left/Right join
- Left/Right outer join
- Unions

### Challenges

- Give me the color from `team_colors` with their associated mascot.
- Repeat the query from above, except this time change which table is your `FROM`.
- Give me the `player_id` from `mbb_players_games_sr` and `attendance` from `mbb_games_sr` for each game that had more than 1,000 people in `attendance`. NOTE: They share the same `game_id`.
- Give me the mascot name and `scheduled_date` of all games (`mbb_games_sr`) in the `Colorado` market (in the `mascots` table) that had over 1000 people in attendance. NOTE: `mbb_games_sr` has an id for the home team (`h_id`).
- Give me everything from the `mbb_games_sr` and `mascot` tables in Arizona. Use the `h_id` from `mbb_games_sr`.
- Give me the game ID of every game (`mbb_games_sr` table) associated with a mascot whose name starts with the letter 'B'. NOTE: Link the `h_id` from `mbb_games_sr` with the `id` from `mascots`.
- Give me players' first names, mascot, and venue capacity of the top ten most attended games. You're linking three tables: `mbb_players_games_sr`, `mbb_games_sr` and `mascots`. Limit your results to 10.


## Aggregating

Sometimes we might want to reduce our query to a single value. For example, we may want to know how many users our in our database:

```SQL
SELECT COUNT(users.id)
FROM users
```

The `COUNT` in the previous query is an aggregate function. The most common aggregate functions are:

- `COUNT`
- `AVG`
- `MIN`
- `MAX`
- `SUM`

### Challenges

- What is the total number of items in the `mascots` table?

## `GROUP BY`

Often we’ll want to group our data into buckets and then run some sort of aggregate function.

```SQL
-- Returns how much each user spends on average
SELECT users.id, AVG(payments.amount)
FROM users
INNER JOIN payments ON payments.user_id = user.id
GROUP BY users.id;
```

NOTE: Every column you're returning that isn't an aggregation needs to be in the `GROUP BY` clause:

```SQL
-- Returns how much each user spends on average
SELECT users.id, users.name, AVG(payments.amount)
FROM users
INNER JOIN payments ON payments.user_id = user.id
GROUP BY users.id, users.name
```

### Challenges

- From `mbb_games_sr`, return the average attendance for each `season`, sorted by the season.
- Same table: `mbb_games_sr`. Give me the average attendance by mascot. Sort your results alphabetically.


## `HAVING`

Sometimes you might want to use the result of an aggregate function as a filter. We can do this with `HAVING`, which is similar to `WHERE` but for aggregates:

```SQL
-- Returns the users who average more than $1,000 per purchase
SELECT users.id, users.name, AVG(payments.amount)
FROM users
INNER JOIN payments ON payments.user_id = users.id
GROUP BY users.id, users.name
HAVING AVG(payments.amount) > 1000;
```

### Challenges

- Give me the average attendance by mascot for `mascots` that have at least 5000 people in attendance on average. Sort your results alphabetically.
- What mascots average less than 35 home rebounds (`h_rebounds`)? Order your results from most home rebounds to least.
# `data`

Store data here for local usage only, everything except this README file should be ignored.

## Database Information

The data being pulled from `Resolute.AI` is very relational, this is why things are separated into individual tables. There are a couple of tables that will always be included in the database:

1. `base`: this is the "base" table that everything else is based off of. It's not of much use so it can mostly be ignored.
2. `products`: this has jnj product names and categories with the associated company. This may be useful when performing queries.
3. `requests`: this is a record of all requests that were made in order to create the database.

The naming convension of all other tables goes like this:

* (endpoint)_(nested / relational data)

So for example, the `search/news/` endpoint has a nested column with company topic information. Therefore, the resulting table is named `search_news_company_topics`.

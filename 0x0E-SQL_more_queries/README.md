# 0x0E. SQL - More queries

### Tasks
* **0. My privileges!:**
A script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
    * [ Script Here ](./0-privileges.sql)

* **1-create_user.sql:**
A script that creates the MySQL server user user_0d_1.
    * user_0d_1 would have all privileges on your MySQL server
    * The user_0d_1 password would be set to user_0d_1_pwd
    * If the user user_0d_1 already exists, the script would not fail
[ Script Here ](./1-create_user.sql)

* **2.Read user:**
A script that creates the database hbtn_0d_2 and the user user_0d_2.
    * user_0d_2 would have only SELECT privilege in the database hbtn_0d_2
    * The user_0d_2 password would be set to user_0d_2_pwd
    * If the database hbtn_0d_2 already exists, the script would not fail
    * If the user user_0d_2 already exists, script would not fail

[ Script Here ](./2-create_read_user.sql)

* **3. Always a name:**
A script that creates the table force_name on your MySQL server.
    * force_name description:
        * id INT
        * name VARCHAR(256) can’t be null
    * The database name should be passed as an argument of the mysql command
    * If the table force_name already exists, the script would not fail

[ Script Here ](./3-force_name.sql)

* **4. ID can't be null:**
A script that creates the table id_not_null on your MySQL server.
    * id_not_null description:
        * id INT with the default value 1
        * name VARCHAR(256)
    * The database name Should be passed as an argument of the mysql command
    * If the table id_not_null already exists, the script would not fail

[ Script Here ](./4-never_empty.sql)

* **5. Unique ID:**
A  script that creates the table unique_id on your MySQL server.
    * unique_id description:
        * id INT with the default value 1 and must be unique
        * name VARCHAR(256)
    * The database name should be passed as an argument of the mysql command
    * If the table unique_id already exists, the script would not fail

[ Script Here ](./5-unique_id.sql)

* **6. States table:**
A script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
    * states description:
        * id INT unique, auto generated, can’t be null and is a primary key
        * name VARCHAR(256) can’t be null
    * If the database hbtn_0d_usa already exists, the script would not fail
    * If the table states already exists, the script would not fail

[ Script Here ](./6-states.sql)

* **7. Cities table:**
A script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
    * cities description:
        * id INT unique, auto generated, can’t be null and is a primary key
        * state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
        * name VARCHAR(256) can’t be null
    * If the database hbtn_0d_usa already exists, the script would not fail
    * If the table cities already exists, the script would not fail
[ Script Here ](./7-cities.sql)

* **8. Cities of California:**
A script that lists all the cities of California that can be found in the database hbtn_0d_usa.
    * The states table contains only one record where name = California (but the id can be different, as per the example)
    * Results will be sorted in ascending order by cities.id
    * The JOIN keyword not used
    * The database name should be passed as an argument of the mysql command

[ Script Here ](./8-cities_of_california_subquery.sql)

* **9. Cities by States:**
A script that lists all cities contained in the database hbtn_0d_usa.
    * Each record would display: cities.id - cities.name - states.name
    * Results would be sorted in ascending order by cities.id
    * Only one SELECT statement is used.
    * The database name should be passed as an argument of the mysql command

[ Script Here ](./9-cities_by_state_join.sql)

* **10. Genre ID by show:**
The hbtn_0d_tvshows database [here](./https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
    * Each record would display: tv_shows.title - tv_show_genres.genre_id
    * Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
    * Only one SELECT statement is used
    * The database name should be passed as an argument of the mysql command

[ Script Here ](./10-genre_id_by_show.sql)

* **11. Genre ID for all shows:**
A script that lists all shows contained in the database hbtn_0d_tvshows.
    * Each record displays: tv_shows.title - tv_show_genres.genre_id
    * Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
    * If a show doesn’t have a genre, it displays NULL
    * Only one SELECT statement is used
    * The database name should be passed as an argument of the mysql command

[ Script Here ](./11-genre_id_all_shows.sql)

* **12. No genre:**
A script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
    * Each record displays: tv_shows.title - tv_show_genres.genre_id
    * Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
    * Only one SELECT statement is used
    * The database name should be passed as an argument of the mysql command

[ Script Here ](./12-no_genre.sql)

* **13. Number of shows by genre:**
A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
    * Each record displays: <TV Show genre> - <Number of shows linked to this genre>
    * First column is called genre
    * Second column is called number_of_shows
    * A genre that doesn’t have any shows linked is not displayed
    * Results are sorted in descending order by the number of shows linked
    * Only one SELECT statement is used
    * The database name should be passed as an argument of the mysql command

[ Script Here ](./13-count_shows_by_genre.sql)

* **14. My genres:**
A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
    * The tv_shows table contains only one record where title = Dexter (but the id can be different)
    * Each record displays: tv_genres.name
    * Results are sorted in ascending order by the genre name
    * Only one SELECT statement can be used.
    * The database name should be passed as an argument of the mysql command

[ Script Here ](./14-my_genres.sql)

* **15. Only Comedy:**
A script that lists all Comedy shows in the database hbtn_0d_tvshows.
    * The tv_genres table contains only one record where name = Comedy (but the id can be different)
    * Each record displays: tv_shows.title
    * Results are sorted in ascending order by the show title
    * Only one SELECT statement is used
    * The database name should be passed as an argument of the mysql command

[ Script Here ](./15-comedy_only.sql)

* **16. List shows and genres:**
A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
    * If a show doesn’t have a genre, NULL is displayed in the genre column
    * Each record displays: tv_shows.title - tv_genres.name
    * Results are sorted in ascending order by the show title and genre name
    * Only one SELECT statement
    * The database name should be passed as an argument of the mysql command

[ Script Here ](./16-shows_by_genre.sql)

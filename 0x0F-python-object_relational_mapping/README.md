# 0x0F. Python - Object-relational mapping
In this project, I'll learn how to use the MySQLdb module to connect to a MySQL database and execute SQL queries. I'll also practice how to use the module SQLAlchemy, an Objet Relational Mapper(ORM)

## Tasks
* [ 0-select_states.py ](./0-select_states.py): A script that lists all states from the database hbtn_0e_0_usa using the module MySQLdb.
    * Results are displayed in ascending order by states.id

* [ 1-filter_states.py ](./1-filter_states.py): A script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa using the MySQLdb module.
    * Results are sorted in ascending order by states.id

* [ 2-my_filter_states.py ](./2-my_filter_states.py): A  script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument passed into the script using the MySQLdb module.
    * Results are sorted in ascending order by states.id

* [ 3-my_safe_filter_states.py ](./3-my_safe_filter_states.py): A script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, it is safe from MySQL injections using the MySQLdb module!
    * Results are sorted in ascending order by states.id

* [ 4-cities_by_state.py ](./4-cities_by_state.py): A script that lists all cities from the database hbtn_0e_4_usa using the MySQLdb module.
    * Results are sorted in ascending order by cities.id

* [ 5-filter_cities.py ](./5-filter_cities.py): A script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa using the MySQLdb module.
    * Results are sorted in ascending order by cities.id

* [ model_state.py ](./model_state.py) - A python file that contains the class definition of a State and an instance Base = declarative_base():
    * State class:
        * inherits from Base
        * links to the MySQL table states
        * class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
        * class attribute name that represents a column of a string with maximum 128 characters and can’t be null
    * It uses the SQLAlchemy module

* [ 7-model_state_fetch_all.py ](./7-model_state_fetch_all.py): This script that lists all State objects from the database hbtn_0e_6_usa using the SQLAlchemy module.
    * Results are sorted in ascending order by states.id

* [ 8-model_state_fetch_first.py ](./8-model_state_fetch_first.py): A script that prints the first State object from the database hbtn_0e_6_usa using theSQLAlchemy module.
    * State and Base from model_state - from model_state import Base, State is imported.
    * Results are sorted in ascending order by states.id

* [ 9-model_state_filter_ ](./9-model_state_filter_): A script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa using the SQLAlchemy module.
    * Results are sorted in ascending order by states.id
    * State and Base from model_state - from model_state import Base, State
    * Code won't run if imported

* [ 10-model_state_my_get.py ](./10-model_state_my_get.py): A script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa using the SQLAlchemy module.
    * State and Base from model_state - from model_state import Base, State is imported
    * Results are sorted in ascending order by states.id
    * Code would not run if imported

* [ 11-model_state_insert.py ](./11-model_state_insert.py): A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa using the SQLAlchemy module.
    * State and Base from model_state - from model_state import Base, State is imported

* [ 12-model_state_update_id_2.py ](./12-model_state_update_id_2.py): A script that changes the name of a State object from the database hbtn_0e_6_usa using the SQLAlchemy module.
    * State and Base from model_state - from model_state import Base, State is imported

* [ 13-model_state_delete_a.py ](./13-model_state_delete_a.py): A script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa using the SQLAlchemy module.
    * State and Base from model_state - from model_state import Base, State is imported

* [ 14-model_city_fetch_by_state.py ](./14-model_city_fetch_by_state.py): A script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa using the SQLAlchemy module.
    * State and Base from model_state - from model_state import Base, State is imported
    * Results are sorted in ascending order by cities.id
    * Results are displayed as they are in the example below (<state name>: (<city id>) <city name>)
    * Code won't run if imported

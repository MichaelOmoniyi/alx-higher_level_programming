-- Lists all records of the table second_table from the database hbtn_0c_0 in your MySQL server.
-- Don't list rows without a name value
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

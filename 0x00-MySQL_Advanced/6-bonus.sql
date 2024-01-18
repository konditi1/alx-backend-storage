--  script that creates a stored procedure AddBonus that adds
-- a new correction for a student.

DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus (
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    INSERT INTO projects (name)
    VALUES (project_name);
    SET @project_id = LAST_INSERT_ID();
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, @project_id, score);
END $$
DELIMITER ;

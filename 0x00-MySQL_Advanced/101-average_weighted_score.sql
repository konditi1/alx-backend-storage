-- Script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;

    -- Declare a cursor to iterate through all users
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    
    -- Declare handler for when no more rows are found
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET user_id = NULL;

    -- Open the cursor
    OPEN user_cursor;

    -- Start iterating through users
    user_loop: LOOP
        -- Fetch the next user_id
        FETCH user_cursor INTO user_id;

        -- Exit the loop if no more users
        IF user_id IS NULL THEN
            LEAVE user_loop;
        END IF;

        -- Calculate total weighted score and total weight for the user
        SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO total_score, total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Compute and update the average weighted score for the user
        IF total_weight > 0 THEN
            UPDATE users
            SET average_score = total_score / total_weight
            WHERE id = user_id;
        END IF;
    END LOOP;

    -- Close the cursor
    CLOSE user_cursor;
END //

DELIMITER ;

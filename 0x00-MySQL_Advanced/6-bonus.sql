-- Creates a stored procedure AddBonus to add a new correction for a student
-- and create a new project if it doesn't exist.

DELIMITER $$

-- Create the AddBonus stored procedure
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    -- Check if the project exists, and if not, create it
    DECLARE project_id INT;
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the correction with the provided values
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END $$
DELIMITER ;

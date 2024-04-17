-- Script That Creates A Stored Procedure ComputeAverageScoreForUser.
-- Computes And Store The Sverage Score For A Student.

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;
    SELECT SUM(score) INTO total_score FROM corrections WHERE user_id = user_id;
    SELECT COUNT(DISTINCT project_id) INTO total_projects FROM corrections WHERE user_id = user_id;
    IF total_projects > 0 THEN
        UPDATE users SET average_score = total_score / total_projects WHERE id = user_id;
    ELSE
        UPDATE users SET average_score = 0 WHERE id = user_id;
    END IF;
END;
//
DELIMITER ;

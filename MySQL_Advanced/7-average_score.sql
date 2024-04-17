-- Script That Creates A Stored Procedure ComputeAverageScoreForUser.
-- Computes And Store The Sverage Score For A Student.
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(score) / COUNT(*) 
        FROM corrections
        WHERE corrections.user_id = user_id
    )
    WHERE id = user_id;
END;
//
DELIMITER ;

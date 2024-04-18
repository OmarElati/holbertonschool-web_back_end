-- Script That Creates A View need_meeting.
-- Lists All Students That have A Score Under 80 (Strict) And No last_meeting Or More Than 1 Month.
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE (score < 80 AND last_meeting IS NULL OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));

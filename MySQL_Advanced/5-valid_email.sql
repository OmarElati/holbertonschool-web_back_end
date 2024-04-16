-- Script That Creates A Trigger That Resets The Attribute valid_email.
-- Only When The Email Has Been Changed.
DELIMITER //
CREATE TRIGGER trg_reset
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;

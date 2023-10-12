-- Creates a function SafeDiv that divides two numbers and returns the result or 0 if the second number is 0.

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT DETERMINISTIC
BEGIN
    RETURN IF(b = 0, 0, a / b);
END $$

DELIMITER ;

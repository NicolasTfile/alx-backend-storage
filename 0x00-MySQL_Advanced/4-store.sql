-- Create the trigger to decrease item quantity
-- after adding an order
DELIMITER //
CREATE TRIGGER DecreaseItemQuantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //
DELIMITER ;

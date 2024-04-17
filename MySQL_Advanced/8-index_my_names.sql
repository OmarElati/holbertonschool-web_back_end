-- Script That Creates An Index idx_name_first.
-- On The Table names And The First Letter of name.
CREATE INDEX idx_name_first ON names (name(1));

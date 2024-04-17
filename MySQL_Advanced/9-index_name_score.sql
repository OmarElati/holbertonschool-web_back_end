-- Script That Creates An Index idx_name_first_score.
-- On The Table names And The First Letter Of name And The score.
CREATE INDEX idx_name_first_score ON names (name(1), score);

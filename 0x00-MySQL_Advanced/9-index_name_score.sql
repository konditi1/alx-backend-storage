--  script that creates an index idx_name_first_score on the
-- table names and the first letter of name and the score

CREATE INDEX idx_name_score ON names(name(1))

-- Create an index on the score column
CREATE INDEX idx_score ON names (score);

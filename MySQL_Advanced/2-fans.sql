-- Create A Table users.
-- Calculate country origins of bands ranked by number of non-unique fans.
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

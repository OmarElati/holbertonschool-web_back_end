-- List all bands with Glam rock as their main style
-- Ranked by longevity
SELECT band_name, IFNULL(split, YEAR(CURDATE())) - formed as lifespan FROM metal_bands WHERE style LIKE '%Glam rock%';

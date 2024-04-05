-- List all bands with Glam rock as their main style, ranked by longevity
SELECT band_name, 
       IFNULL(SUBSTRING_INDEX(split, '-', -1), YEAR(CURDATE())) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC, band_name;

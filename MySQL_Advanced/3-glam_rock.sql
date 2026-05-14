-- Script that lists all bands with Glam rock as their main style
-- Ranked by their longevity (lifespan) up to the year 2024

-- Select band name and calculate lifespan using 2024 for active bands
SELECT band_name, (IFNULL(split, 2024) - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;

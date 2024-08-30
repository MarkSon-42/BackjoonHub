SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (
    (GENOTYPE & 1 > 0)  -- Trait 1 is present
    OR
    (GENOTYPE & 4 > 0)  -- Trait 3 is present
)
AND
(
    (GENOTYPE & 2 = 0)  -- Trait 2 is absent
);

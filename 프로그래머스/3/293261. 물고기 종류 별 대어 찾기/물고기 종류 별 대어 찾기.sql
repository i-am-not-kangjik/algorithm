-- 코드를 작성해주세요
SELECT 
    ID, 
    fni.FISH_NAME, 
    LENGTH 
FROM FISH_INFO fi 
LEFT JOIN FISH_NAME_INFO fni ON fi.FISH_TYPE = fni.FISH_TYPE 
WHERE fi.length = (
    SELECT MAX(f.LENGTH)
    FROM FISH_INFO f 
    WHERE f.FISH_TYPE = fi.FISH_TYPE
);

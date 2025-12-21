-- 코드를 작성해주세요
select CONCAT(FORMAT(MAX(LENGTH),2), 'cm') as MAX_LENGTH
from FISH_INFO
where LENGTH is not null
    
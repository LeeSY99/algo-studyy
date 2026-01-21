-- 코드를 입력하세요
SELECT 
    b.CATEGORY,
    sum(s.sales) as TOTAL_SALES
from BOOK b
join BOOK_SALES s on b.book_id = s.book_id
where s.sales_date >= "2022-01-01" and s.sales_date < "2022-02-01"
group by b.category
order by b.category
-- 코드를 입력하세요
SELECT B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(PRICE * SALES) AS TOTAL_SALES
FROM BOOK AS B
JOIN AUTHOR AS A ON B.AUTHOR_ID = A.AUTHOR_ID 
JOIN BOOK_SALES AS S ON B.BOOK_ID = S.BOOK_ID
WHERE SALES_DATE LIKE '2022-01%'
GROUP BY AUTHOR_ID, B.CATEGORY
ORDER BY AUTHOR_ID ASC, CATEGORY DESC;
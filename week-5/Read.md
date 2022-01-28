SELECT * FROM member;

SELECT * FROM member ORDER BY time;

SELECT * FROM member ORDER BY time LIMIT 1,3;

SELECT * from member WHERE username='test';

SELECT * from member WHERE username='test' and password='test';

UPDATE * from member WHERE username='test' and password='test';

SET SQL_SAFE_UPDATES=0;
UPDATE member SET name='test2' WHERE username='test';
SET SQL_SAFE_UPDATES=1;

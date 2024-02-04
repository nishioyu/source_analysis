-- select_query = """
SELECT
    a.column1 AS alias1,
    b.column2 AS alias2,
    c.column3 AS alias3
FROM
    (SELECT * FROM table1 WHERE column4 = (SELECT column5 FROM table4 WHERE column6 = 'value')) a
    JOIN (SELECT * FROM table2 WHERE column7 = (SELECT column8 FROM table5 WHERE column9 = 'another_value')) b ON a.id = b.id
    JOIN (SELECT * FROM table3 WHERE column10 = (SELECT column11 FROM table6 WHERE column12 = 'yet_another_value')) c ON b.id = c.id;
-- """

-- insert_query = """
# hogehoge  
INSERT INTO               table1 　　　　　　　　　　　　　　　　　　　　　　　　　　　　　(column1, column2, column3)　　　　
VALUES
    ((SELECT column4 FROM table2 WHERE column5 = 'value'),
    (SELECT column6 FROM table3 WHERE column7 = 'another_value'),
    (SELECT column8 FROM table4 WHERE column9 = 'yet_another_value'));
-- """

-- insert_query_2 = """
# このSQLはほげほげ
INSERT INTO          table1
VALUES
    ((SELECT column4 FROM table2 WHERE column5 = 'value'),
    (SELECT column6 FROM table3 WHERE column7 = 'another_value'),
    (SELECT column8 FROM table4 WHERE column9 = 'yet_another_value'));
-- """

-- update_query = """
UPDATE table1
SET
    column1 = (SELECT column2 FROM table2 WHERE column3 = 'value'),
    column4 = (SELECT column5 FROM table3 WHERE column6 = 'another_value'),
    column7 = (SELECT column8 FROM table4 WHERE column9 = 'yet_another_value')
WHERE
    id = (SELECT id FROM table5 WHERE column10 = (SELECT column11 FROM table6 WHERE column12 = 'value'));
-- """

-- delete_query = """
DELETE FROM table1
WHERE
    id IN (SELECT id FROM table2 WHERE column1 = (SELECT column3 FROM table3 WHERE column4 = 'value'))
    AND column2 = (SELECT column3 FROM table4 WHERE column4 = 'another_value')
    AND column5 = (SELECT column6 FROM table5 WHERE column7 = (SELECT column9 FROM table6 WHERE column10 = 'yet_another_value'));
-- """


-- update_sample = """
# 更新処理だよ
UPDATE employees JOIN manager
ON employees.emp_no = manager.emp_no
SET employees.manager_name = ( SELECT manager.manager_name FROM manager
  WHERE employees.emp_no = manager.emp_no ), employees.manager_id = 100
WHERE employees.emp_id = 1;
-- """

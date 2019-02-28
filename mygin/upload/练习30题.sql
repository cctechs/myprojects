#查看mysql数据库中user表的表结构
SHOW TABLES;
DESCRIBE cds;

#查询user表中host（主机IP）,user（用户名）两个字段的值
SELECT USER,HOST
FROM mysql.user;

#创建lianxi库，设置数据库的默认字符集为utf8,使该数据库可以支持中文，输入的字符不区分大小写；
CREATE DATABASE lianxi2 DEFAULT CHARACTER utf8 COLLATE utf8_general_ci:
CREATE DATABASE lianxi2 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE DATABASE lianxi2 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
#"--------default\character\set------collate--uft8_general_ci-------"


#修改数据库lianxi的字符集为gb2312，排序规则为gb2312_chinese_ci,使该数据库可以支持中文，
#输入的sql语句不区分大小写
ALTER DATABASE lianxi2 DEFAULT CHARACTER SET gb2312 COLLATE gb2312_chinese_ci;

#删除数据库lianxi1
DROP DATABASE lianxi2;

#在lianxi库中，创建学生表stu，
#字段名包括：学号sno,数据类型为int,长度为5，姓名sname，数据类型为char,长度为20
CREATE DATABASE lianxi2 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE TABLE lianxi2.stu(sno INT(5),sname CHAR(20));
#"--------未加括号---------"

#在lianxi库中，创建表stu1，字段名包括：
#学号sno,数据类型为int,长度为5，
#姓名sname，数据类型为char,长度为20
#将字段sno设置为主键
CREATE TABLE lianxi2.stu1
(
sno INT(5)PRIMARY KEY,
sname CHAR(20)
);
#"-------未加逗号---------"


#在lianxi库中，创班级表class，字段名包括：班号cno,数据类型为int,长度为6，
#班级名cname，数据类型为char,长度为15，
#将字段cno设置为主键
CREATE TABLE lianxi2.class(
cno INT(6)PRIMARY KEY,
cname CHAR(15)
);

#在lianxi库中，创建表stu2，字段名包括：学号sno,数据类型为int,长度为5，
#姓名sname，数据类型为char,长度为20，
#班号cno,数据类型为int,长度为6；
#将字段sno设置为主键，将字段cno设置为外键
CREATE TABLE lianxi2.stu2(
sno INT(5) PRIMARY KEY,
sname CHAR(20),
cno INT(6),
FOREIGN KEY(cno) REFERENCES lianxi2.`class`(cno));
#"-------注意空格---第45行为什么不需加空格也可执行成功？------"

#查看hrdb库员工表（employees）表的外键有哪些
SHOW KEYS
FROM hrdb.`employees`;

#修改hr库中sales表名称为sale?
CREATE DATABASE hr;
CREATE TABLE hr.sales(
sno INT(5),
sname CHAR(20));
ALTER TABLE hr.`sales`
RENAME TO sale;

#为表sales 增加主键约束sales_customer_no_pk
SHOW KEYS
FROM hr.`sales`;

ALTER TABLE sales ADD(customer_no CHAR(20));

ALTER TABLE hr.`sales`
ADD CONSTRAINT sales_customer_no_pk PRIMARY KEY(customer_no);
#"-----------ADD CONSTRAINT添加约束的前提条件是表里已存在该字段---------"

修改sales表约束，使姓名customer_no不允许为空
ALTER TABLE sales ADD(pro_name CHAR(20));
ALTER TABLE sales ADD(customer_name CHAR(20));
ALTER TABLE hr.`sales`
MODIFY customer_name CHAR(20) NOT NULL;
"-----------指定表的位置--alter table-----------"

修改表sale，将字段`pro_name`名称修改为province_name
ALTER TABLE hr.sale ADD(pro_name CHAR(30));
ALTER TABLE hr.`sale`
CHANGE pro_name province_name CHAR(40);
"-----------指定表的位置--alter table-----------"

表sale添加字段product_name,字段类型为varchar，长度为30（重点）
ALTER TABLE hr.`sale` ADD(product_name2 VARCHAR(30));

ALTER TABLE hr.`sale`
ADD COLUMN product_name3 VARCHAR(30);

修改sale表中字段`province_name`的字段类型为varchar(30)
ALTER TABLE hr.`sale`
MODIFY province_name VARCHAR(30);

删除表sale中的字段product_name （重点）
ALTER TABLE hr.`sale`
ADD(product_name VARCHAR(30));
ALTER TABLE hr.`sale`
DROP product_name;

ALTER TABLE hr.`sale`
DROP COLUMN product_name;

为部门表添加外键，先创建两个表：
-- 在hr库中，创建学生表 student(学生编号sno int(5),该字段定义为主键,
-- 学生名称sname char(30),班级编号classno int（6）)"
ALTER TABLE hr.`studet`
dorp studet;
CREATE TABLE hr.studet2(
sno INT(5) PRIMARY KEY,
sname CHAR(30),
classno INT(6));


创建表班级表class（班号cno INT(6),班级名称 cname CHAR(25),系名depno int（4） ）
CREATE TABLE hr.class(
cno INT(6),
cname CHAR(25),
depno INT(4));

将class表的cno字段修改为主键
ALTER TABLE hr.`class`
ADD CONSTRAINT class_cno_pk PRIMARY KEY(cno);
'---------原表里没有设置类型的状态下，设置主键为"ADD COUSTRAIINT"增加约束
如已有就是修改“modify"---------'

为hr库中表student的字段classno添加外键，该外键字段的数据引用自表class的主键字段cno
ALTER TABLE hr.`studet`
ADD CONSTRAINT studet_classno_fk FOREIGN KEY (classno)
REFERENCES hr.`class`(cno);
'-------数据引用命令+引用路径---------'

删除hr库student表的外键 student_classno_fk
'步骤一：删除外键-----------步骤二：删除外键索引'
ALTER TABLE hr.`student`
DROP FOREIGN KEY student_classno_fk;
DROP INDEX student_classno_fk ON hr.`student`;

删除hr库中的表sale
DROP TABLE hr.`sale`;

往表stu1中插入一条数据，编号为01，姓名为张三
CREATE TABLE hr.stu1(
sno INT(5),
sname CHAR(20),
proname CHAR(30));

INSERT INTO hr.`stu1`(sno,sname) VALUES(03,"zhangsan");
INSERT INTO hr.`stu1`(sno,sname) VALUES(04,"lisi");

修改姓名为李四的人的编号由2修改为3
UPDATE hr.`stu1`
SET son=6
WHERE sname="lisi";
UPDATE hr.`stu1`
SET sno=5
WHERE sname=""lisi"";
'------------未成功-------------------'
删除表stu1中编号为1的数据
DELETE FROM hr.`stu1`
WHERE sno=1;
DELETE FROM hr.`stu1`
WHERE sno=2;

创建一个表，该表的表结构和数据均复制于表employees
CREATE TABLE hr.copy
SELECT * FROM hrdb.`employees`;

删除表emp中的所有数据
DELETE FROM hr.`copy`;
DELETE * FROM hr.`copy`;"错误语法"

删除表emp1中的所有数据
CREATE TABLE hr.emp1
SELECT * FROM hrdb.`employees`;--复制表再删除表
DELETE FROM hr.`emp1`;

查询员工表（employees）中所有人员的所有信息
SELECT *
FROM hrdb.`employees`;(*代表所有)

查询employees表中所有人员的姓、名
SELECT employees.`first_name`,employees.`last_name`
FROM hrdb.`employees`;

员工表中员工编号为101的员工的员工编号、工资
SELECT employees.`department_id`,salary
FROM hrdb.`employees`
WHERE employee_id=101;

查询 工资大于9000的人员的姓名、工资
SELECT last_name,salary
FROM hrdb.`employees`
WHERE salary>9000;

查询工资大于等于9000的人员的工资、姓、部门编号
SELECT last_name,employees.`department_id`
FROM hrdb.`employees`
WHERE salary>=9000;

查询工资不等于9000的人员的工资、姓、部门编号(方法一)
"不等于！="

查询工资不等于9000的人员的工资、姓、部门编号(方法二
"不等于<>"

查询工资不等于9000的人员的工资、姓、部门编号(方法三）
"不等于not salary"

查询工资大于9000，部门编号小于102的人员的员工编号、入职日期、工资、部门编号
SELECT employee_id,hire_date,salary,department_id
FROM hrdb.`employees`
WHERE salary>9000 AND department_id<102;

查询员工表中部门编号分别为60 和90 的人员的工资、部门编号、员工编号
SELECT salary,department_id,employee_id
FROM hrdb.`employees`
WHERE department_id=60 OR department_id=90;

"and连接两个查询
or连接两个条件，符合任何一个
in连接多个条件，符合其中一个
beteween...and...在值一与值二之间"
查询工资分别为9000、10000、11000、12000的员工编号、工资
SELECT employee_id,salary
FROM hrdb.`employees`
WHERE salary IN(9000,10000,11000,12000);

查询工资在3000-6000之间的人员的工资、员工编号、职位编号
SELECT salary,employee_id,department_id
FROM hrdb.`employees`
WHERE salary BETWEEN 3000 AND 6000;

查询部门表中经理编号为空的部门的编号、部门名称、经理编号
SELECT department_id,department_name,manager_id
FROM hrdb.`departments`
WHERE manager_id IS NULL;

查询部门表中经理编号不为空的部门的编号、部门名称、经理编号
SELECT department_id,manager_id,department_name
FROM hrdb.`departments`
WHERE department_id IS NOT NULL;

查询员工表中的最高工资、最低工资、平均工资、工资总和
SELECT MAX(salary),MIN(salary),AVG(salary),SUM(salary)
FROM hrdb.`employees`

查询员工表中的所有人员的工资之和以及人员的数量
SELECT SUM(salary),SUM(employee_id)
FROM hrdb.`employees`

往表stu1中插入一条数据，编号为01，姓名为张三
DELETE FROM hr.`stu1`
WHERE sname=zhangsan;（删除表里"指定"内容)

DELETE FROM hr.`stu1`;(删除表里所有内容)

INSERT INTO hr.`stu1`(sno,sname) VALUES(03,"zhangsan");
-------插入的values内容，注意一定要使用"引号"---------

查询员工表中每个部门人员的平均工资，查询结果显示部门编号、平均工资
SELECT AVG(salary),department_id
FROM hrdb.`employees`
GROUP BY department_id;

查询部门编号为70的部门的人员的平均工资
SELECT AVG(salary)
FROM hrdb.`employees`
WHERE department_id=70;

查询不同部门中，不同职位的人员的平均工资,查询结果显示部门编号、
职位编号、平均工资
SELECT AVG(salary),department_id,job_id
FROM hrdb.`employees`
GROUP BY department_id,job_id;

查询部门表中不同部门人员的平均工资，查询结果要求
只显示:平均工资高于12000的部门编号、平均工资
SELECT AVG(salary),department_id
FROM hrdb.`employees`
GROUP BY department_id
HAVING AVG(salary)>12000;

查询部门表中不同部门人员的平均工资，查询结果要求
只显示：部门编号低于60的部门编号、平均工资
SELECT AVG(salary),department_id
FROM hrdb.`employees`
GROUP BY department_id
HAVING department_id<60;

查询员工表中所有人员的工资，查询结果按工资高低升序排列，结果显示员工编号、工资
SELECT salary,employee_id
FROM hrdb.`employees`
GROUP BY salary;
"------升序：ASC(默认顺序) ， 降序：desc------------"

查询不同部门的平均工资，查询结果按平均工资高低进行降序排列，
查询结果显示部门编号、平均工资
SELECT AVG(salary),department_id
FROM hrdb.`employees`
GROUP BY department_id
ORDER BY AVG(salary) DESC
"-----------排序时不可使用having(过滤)，用的是ordey by-------
group by 指定去哪个分组里进行查询
having	对通过group by分组后的数据过滤(可跟字段名、函数名)
limit 4	取前四条数据（限制提取）
order by 指定关键字进行（ASC,DESC）排序"

查询员工表中所有人员的工资，查询结果按工资高低降序排列，
结果显示工资前四高的员工编号、工资
SELECT employee_id,salary
FROM hrdb.`employees`
GROUP BY salary
ORDER BY salary DESC
LIMIT 4;

查询不同部门的平均工资，查询结果按平均工资高低进行降序排列，
查询结果显示前4条数据的部门编号、平均工资
SELECT AVG(salary),department_id
FROM hrdb.`employees`
GROUP BY department_id
ORDER BY AVG(salary) DESC
LIMIT 4;

查询不同部门的平均工资，查询结果按平均工资高低进行降序排列，
查询结果显示平均工资高于7000的数据，只显示前4条数据的部门编号、平均工资
SELECT department_id,AVG(salary)
FROM hrdb.`employees`
GROUP BY department_id
HAVING AVG(salary)>7000
ORDER BY AVG(salary) DESC
LIMIT 4;
"---------注意having后面不带bay---------"

查询员工表中员工编号第二位为2的员工的编号、姓名
SELECT employee_id,last_name,first_name
FROM hrdb.`employees`
WHERE employee_id LIKE"_2%";

"指定条件查询"where......like“”（将关键内容输入引号）
"%2:最后一位为二
2%最前面一位为二
%2%包含2的所有数据
-代表个位数值，比如10086，要查找第四位为8的数值，模糊概念可以用_ _ _ 8%来代替"

查询员工表中员工编号第三位为2的员工的编号、姓名
SELECT employee_id,last_name,first_name
FROM hrdb.`employees`
WHERE employee_id LIKE"__2%";

查询员工表中员工编号最后一位为2的员工的编号、姓名
SELECT employee_id,last_name,first_name
FROM employees
WHERE employee_id LIKE "%2";

查询员工表中职位编号第一位为A的职位编号、姓名
SELECT job_id,last_name,first_name
FROM employees
WHERE job_id LIKE"A%";

查询员工表中first_name编号第一位为a，第三位为i的员工编号、姓名
SELECT employee_id,last_name,first_name
FROM employees
WHERE first_name LIKE"a%" AND first_name LIKE"__i%";
"---用and就表示同时满足，用or只要满足其一就可----------"

查询员工表中有哪些职位分类
SELECT DISTINCT job_id
FROM hrdb.`employees`;

查询员工中不同职位的个数
SELECT COUNT(DISTINCT job_id)
FROM hrdb.`employees`;

distinct相关错误写法：查询员工表中不同职位，查询结果显示部门编号、职位编号
SELECT department_id,DISTINCT job_id
FROM hrdb.`employees`;

统计部门表中有多少个部门
SELECT COUNT(DISTINCT department_id)
FROM hrdb.`departments`;

SELECT COUNT(*)
FROM hrdb.`departments`;

统计部门表中有多少个部门，不统计字段值为null的相关记录
SELECT COUNT(manager_id)
FROM hrdb.`departments`;
"(前提需知道哪些字段下为空值才能指定计算）"

查询员工表中不同员工的薪资，查询结果先按部门编号降序排列，再按薪资高低降序排列
SELECT department_id,salary
FROM hrdb.`employees`
ORDER BY department_id DESC,salary DESC;

查询员工表中last_name为Fay的员工所在的部门的名称
SELECT e.last_name,d.department_name
FROM hrdb.`departments` d,hrdb.`employees` e
WHERE e.department_id=d.department_id
AND e.last_name="fay";

查询在城市Seattle中工作的人员有哪些(跨三个表查询数据)
SELECT e.employee_id,l.city
FROM hrdb.`locations` l,hrdb.`departments` d,hrdb.`employees` e
WHERE l.location_id=d.location_id
AND d.department_id=e.department_id
AND l.city="Seattle";
"----------select显示太多结果输入太导会导致查询失败---------"

查询在United States of America工作的员工有哪些人
SELECT c.country_name,e.employee_id
FROM hrdb.`countries` c,hrdb.`departments` d,hrdb.`employees` e,hrdb.`locations` l
WHERE c.country_id=l.country_id AND l.location_id=d.location_id
AND d.department_id=e.department_id AND c.country_name="United States of America";

查询职位名称为Marketing Manager的职位，有哪些员工,查询结果显示员工编号、职位名称
SELECT j.job_title,e.employee_id
FROM hrdb.`employees` e,hrdb.`jobs` j
WHERE j.job_id=e.job_id AND j.job_title="Marketing Manager";

查看员工表中，员工编号为100的员工所在的部门的部门名称
SELECT e.employee_id,d.department_name
FROM hrdb.`departments` d,hrdb.`employees` e
WHERE e.department_id=d.department_id AND e.employee_id="100";






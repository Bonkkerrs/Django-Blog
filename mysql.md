## MySQL基本语句
### 基本DDL操作
*数据定义语言*
#### 创建数据库
```mysql
create database db; -- 创建数据库
use db; -- 使用db数据库
```
#### 创建数据表
```mysql
create table student(
	id int(10) primary key auto_increment,
	name VARCHAR(50),
	age int(4),
	address VARCHAR(200),
	phone char(11)
);
        /*
        约束语句：
            主键约束: primary key auto_increment
            非空约束: not null
            默认值约束: default 值
            唯一性约束: unique
        */
```
#### 删除数据表
```mysql
drop table student;
```
#### 修改表结构
```mysql
alter table student add 字段 类型 约束;
alter table student drop column 字段;
alter table student modify 字段 类型 约束;
```
### DML语句
数据管理语句 
#### 增加数据
```mysql
-- 添加数据
insert into 表(字段1, 字段2, ...) values(值1, 值2, ...) -- 字符串要加单引号！
-- 一次性多条数据添加
insert into 表(字段1, 字段2, ...) values(值1, 值2, ...),
            表(字段1, 字段2, ...) values(值1, 值2, ...),
            表(字段1, 字段2, ...) values(值1, 值2, ...);
```

#### 修改数据
```mysql
update student set address='Taipei', phone='886' where id=1; -- 要添加限定条件！！否则全表修改
```
#### 删除数据
```mysql
delete from student where id=1; 
```

### 查询数据
#### 基本的查询语句
```mysql
-- 查询所有的数据
select * from student;
-- 查询名字和电话号
select name, phone from student;
-- 指定列名
select name as '名字', phone as '电话' from student;
-- 根据电话号查询个人信息
select * from person where phone = '17612345678';
-- 查询年龄大于20岁的人
select * from person where age >= 20;
-- 查询大于18，小于25岁的人
select * from person where age between 18 and 25;
-- 查询所有姓朱的人(模糊搜索)
select * from person where name like '朱%'       -- %:任意 _:一个字符
-- 查询名字中带有詹字的人
select * from person where name like '%詹%'
-- 查询名字可能是(David, Jason)
select * from person where name in ('David','Jason')
-- 判空操作 is null / is not null
select * from person where name is not null;
```
#### 聚合函数
```mysql
-- max()
select max(age) from person;
-- min()
select min(age) from person;
-- avg() 平均值
select avg(age) from person;
-- count()
select count(*) from person;      -- 避免为空
-- sum()
select sum(age) from person;
```
一般聚合函数配合着group by语句进行使用
```mysql
-- 计算每个班级的平均年龄，查询的其他内容必须卸载group by后面
select cls, avg(age) from person group by cls;
-- having 语句 在分组查询之后和聚合函数计算之后的结果后进行的筛选
-- where 在原始数据的基础上进行筛选
select cls, count(*) from person group by cls;
-- 查询人数超过两人的班级
select cls, count(*) from person group by cls having count(*) > 2;
-- 用()来创建临时表
delete from tt where id not in (select min(id) as id from tt group by name,age);
```

#### order by
```mysql
-- 在sql语句的结尾，添加order by语句，asc(升序),desc(降序)
select * from student order by age asc;
```
#### 多表查询   子查询

#### 多表查询   关联查询
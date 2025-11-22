**Q1.**

mysql> create table Department

    -> (dept\_id int,

    -> dept\_name varchar(20),

    -> manager\_id int,

    -> location\_id int,

    -> primary key(dept\_id, manager\_id));
Query OK, 0 rows affected (0.05 sec)


mysql> create table Employees

    -> (eid int primary key,

    -> first\_name varchar(20),

    -> last\_name varchar(20),

    -> email varchar(20),

    -> phone\_no bigint,

    -> hire\_date date,

    -> job\_id int,

    -> salary decimal(7,2),

    -> commission int,

    -> manager\_id int,

    -> dept\_id int,

    -> foreign key(dept\_id, manager\_id)

    -> references Department(dept\_id, manager\_id));

Query OK, 0 rows affected (0.14 sec)


mysql> table Employees;
+-----+------------+-----------+----------------------+------------+------------+----------+----------+------------+------------+---------+

| eid | first\_name | last\_name | email                | phone\_no   | hire\_date  | job\_id   | salary   | commission | manager\_id | dept\_id |

+-----+------------+-----------+----------------------+------------+------------+----------+----------+------------+------------+---------+

| 100 | Sakshi     | Shirke    | sakshi3@gmail.com    | 8596452145 | 2025-09-13 | ad\_press | 24000.00 |       0.00 |        200 |      10 |

| 101 | Sumit      | Yewale    | sumit06@gmail.com    | 8745120023 | 2025-12-30 | ad\_vp    | 17000.00 |       0.00 |        200 |      10 |

| 102 | Meena      | Shedage   | meena26@gmail.com    | 9654785412 | 2024-05-14 | ad\_vp    | 17000.00 |       0.00 |        200 |      10 |

| 103 | Prachi     | Rajpure   | prachi14@gmail.com   | 7741200899 | 2025-06-14 | it\_prog  |  9000.00 |       0.00 |        103 |      60 |

| 104 | Shravani   | Pawar     | shravani25@gmail.com | 8854520125 | 2011-04-01 | it\_prog  |  6000.00 |       0.00 |        103 |      60 |

| 105 | Tanvi      | Dhiwar    | tanvi06@gmail.com    | 7774369852 | 2020-12-12 | it\_prog  |  4800.00 |       0.00 |        103 |      60 |

| 106 | Anuj       | Jamdade   | anuj44@gmail.com     | 8541200032 | 2015-12-15 | it\_prog  |  4800.00 |       0.00 |        103 |      60 |

| 107 | Suraj      | Shelar    | suraj87@gmail.com    | 7823569874 | 2014-02-28 | it\_prog  |  4200.00 |       0.00 |        114 |      30 |

| 108 | Sakshi     | Dhude     | sakshi45@gmail.com   | 9965214001 | 2022-01-08 | sa\_man   | 12000.00 |       0.00 |        145 |      80 |

| 109 | Ankita     | Landage   | ankita65gmail.com    | 7387596547 | 2011-09-14 | sa\_man   |  9000.00 |       0.00 |        145 |      80 |

+-----+------------+-----------+----------------------+------------+------------+----------+----------+------------+------------+---------+

mysql> table Department;
+---------+------------------+------------+-------------+

| dept\_id | dept\_name        | manager\_id | location\_id |

+---------+------------------+------------+-------------+

|      10 | Administration   |        200 |        1700 |

|      20 | Marketing        |        201 |        1800 |

|      30 | Purchasing       |        114 |        1700 |

|      40 | Human Resources  |        203 |        2400 |

|      50 | Shipping         |        121 |        1500 |

|      60 | IT               |        103 |        1400 |

|      70 | Public Relations |        204 |        2700 |

|      80 | Sales            |        145 |        2500 |

+---------+------------------+------------+-------------+

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\

**Q2.**

mysql> insert into stud values(1,'Sakshi Shirke','Pune','Female'),

    -> (2,'Sumit Yewale','Satara','Male'),

    -> (3,'Meena Shedage','Mumbai','Female');

Query OK, 3 rows affected (0.07 sec)

Records: 3  Duplicates: 0  Warnings: 0

mysql> table stud;

+----+---------------+---------+--------+

| id | name          | address | gender |

+----+---------------+---------+--------+

|  1 | Sakshi Shirke | Pune    | Female |

|  2 | Sumit Yewale  | Satara  | Male   |

|  3 | Meena Shedage | Mumbai  | Female |

+----+---------------+---------+--------+
3 rows in set (0.00 sec)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\

**Q3.**

mysql> create table job

    -> (job\_id varchar(20) primary key unique,

    -> job\_title varchar(30),

    -> min\_salary int,

    -> max\_salary int);

Query OK, 0 rows affected (0.13 sec)


mysql> desc job;
+------------+-------------+------+-----+---------+-------+

| Field      | Type        | Null | Key | Default | Extra |

+------------+-------------+------+-----+---------+-------+

| job\_id     | varchar(20) | NO   | PRI | NULL    |       |

| job\_title  | varchar(30) | YES  |     | NULL    |       |

| min\_salary | int         | YES  |     | NULL    |       |

| max\_salary | int         | YES  |     | NULL    |       |

+------------+-------------+------+-----+---------+-------+
4 rows in set (0.00 sec)


mysql> table job;
+------------+-------------------------------+------------+------------+

| job\_id     | job\_title                     | min\_salary | max\_salary |

+------------+-------------------------------+------------+------------+

| ac\_account | Public Accountant             |       4200 |       9000 |

| ac\_mgr     | Accounting Manager            |       8200 |      16000 |

| ad\_asst    | Administartion Assistant      |       3000 |       6000 |

| ad\_pres    | President                     |      20000 |      40000 |

| ad\_vp      | Administration Vice President |      15000 |      30000 |

| fi\_account | Accounting                    |       4200 |       9000 |

| fi\_mgr     | Finance Manager               |       8200 |      16000 |

| sa\_man     | Sales Manager                 |      10000 |      20000 |

+------------+-------------------------------+------------+------------+

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\

**Q4.**

mysql> update job set

    -> min\_salary = min\_salary \* 1.10,

    -> max\_salary = max\_salary \* 1.10;

Query OK, 8 rows affected (0.07 sec)

Rows matched: 8  Changed: 8  Warnings: 0


mysql> table job;
+------------+-------------------------------+------------+------------+

| job\_id     | job\_title                     | min\_salary | max\_salary |

+------------+-------------------------------+------------+------------+

| ac\_account | Public Accountant             |       4620 |       9900 |

| ac\_mgr     | Accounting Manager            |       9020 |      17600 |

| ad\_asst    | Administartion Assistant      |       3300 |       6600 |

| ad\_pres    | President                     |      22000 |      44000 |

| ad\_vp      | Administration Vice President |      16500 |      33000 |

| fi\_account | Accounting                    |       4620 |       9900 |

| fi\_mgr     | Finance Manager               |       9020 |      17600 |

| sa\_man     | Sales Manager                 |      11000 |      22000 |

+------------+-------------------------------+------------+------------+

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\

**Q5.**

mysql> update Employees

    -> set email = 'Not Avaliable'

    -> where dept\_id = 80

    -> and commission < 0.20;

Query OK, 2 rows affected (0.07 sec)

Rows matched: 2  Changed: 2  Warnings: 0


mysql> table Employees;
+-----+------------+-----------+----------------------+------------+------------+----------+----------+------------+------------+---------+

| eid | first\_name | last\_name | email                | phone\_no   | hire\_date  | job\_id   | salary   | commission | manager\_id | dept\_id |

+-----+------------+-----------+----------------------+------------+------------+----------+----------+------------+------------+---------+

| 100 | Sakshi     | Shirke    | sakshi3@gmail.com    | 8596452145 | 2025-09-13 | ad\_press | 24000.00 |       0.10 |        200 |      10 |

| 101 | Sumit      | Yewale    | sumit06@gmail.com    | 8745120023 | 2025-12-30 | ad\_vp    | 17000.00 |       0.15 |        200 |      10 |

| 102 | Meena      | Shedage   | meena26@gmail.com    | 9654785412 | 2024-05-14 | ad\_vp    | 17000.00 |       0.05 |        200 |      10 |

| 103 | Prachi     | Rajpure   | prachi14@gmail.com   | 7741200899 | 2025-06-14 | it\_prog  |  9000.00 |       0.18 |        103 |      60 |

| 104 | Shravani   | Pawar     | shravani25@gmail.com | 8854520125 | 2011-04-01 | it\_prog  |  6000.00 |       0.12 |        103 |      60 |

| 105 | Tanvi      | Dhiwar    | tanvi06@gmail.com    |  774369852 | 2020-12-12 | it\_prog  |  4800.00 |       0.20 |        103 |      60 |

| 106 | Anuj       | Jamdade   | anuj44@gmail.com     | 8541200032 | 2015-12-15 | it\_prog  |  4800.00 |       0.07 |        103 |      60 |

| 107 | Suraj      | Shelar    | suraj87gmail.com     | 7823569874 | 2014-02-28 | it\_prog  |  4200.00 |       0.09 |        114 |      30 |

| 108 | Sakshi     | Dhude     | Not Avaliable        | 9965214001 | 2022-01-08 | sa\_man   | 12000.00 |       0.16 |        145 |      80 |

| 109 | Ankita     | Landage   | Not Avaliable        | 7387596547 | 2011-09-14 | sa\_man   |  9000.00 |       0.11 |        145 |      80 |

+-----+------------+-----------+----------------------+------------+------------+----------+----------+------------+------------+---------+
10 rows in set (0.00 sec)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\

**Q6.**

mysql> update Employees

    -> set email = 'Not Avaliable'

    -> where dept\_id = 30;

Query OK, 2 rows affected (0.08 sec)

Rows matched: 2  Changed: 2  Warnings: 0

**TWO METHODS ARE USE:**

mysql> UPDATE Employees

    -> SET email = 'anita45@gmail.com'

    -> WHERE dept\_id = (

    -> SELECT dept\_id

    -> FROM Department

    -> WHERE dept\_name = 'Purchasing');
    

mysql> table Employees;
+-----+------------+-----------+----------------------+------------+------------+----------+----------+------------+------------+---------+

| eid | first\_name | last\_name | email                | phone\_no   | hire\_date  | job\_id   | salary   | commission | manager\_id | dept\_id |

+-----+------------+-----------+----------------------+------------+------------+----------+----------+------------+------------+---------+

| 100 | Sakshi     | Shirke    | sakshi3@gmail.com    | 8596452145 | 2025-09-13 | ad\_press | 24000.00 |       0.10 |        200 |      10 |

| 101 | Sumit      | Yewale    | sumit06@gmail.com    | 8745120023 | 2025-12-30 | ad\_vp    | 17000.00 |       0.15 |        200 |      10 |

| 102 | Meena      | Shedage   | meena26@gmail.com    | 9654785412 | 2024-05-14 | ad\_vp    | 17000.00 |       0.05 |        200 |      10 |

| 103 | Prachi     | Rajpure   | prachi14@gmail.com   | 7741200899 | 2025-06-14 | it\_prog  |  9000.00 |       0.18 |        103 |      60 |

| 104 | Shravani   | Pawar     | shravani25@gmail.com | 8854520125 | 2011-04-01 | it\_prog  |  6000.00 |       0.12 |        103 |      60 |

| 105 | Tanvi      | Dhiwar    | tanvi06@gmail.com    |  774369852 | 2020-12-12 | it\_prog  |  4800.00 |       0.20 |        103 |      60 |

| 106 | Anuj       | Jamdade   | anuj44@gmail.com     | 8541200032 | 2015-12-15 | it\_prog  |  4800.00 |       0.07 |        103 |      60 |

| 107 | Suraj      | Shelar    | Not Avaliable        | 7823569874 | 2014-02-28 | it\_prog  |  4200.00 |       0.09 |        114 |      30 |

| 108 | Sakshi     | Dhude     | Not Avaliable        | 9965214001 | 2022-01-08 | sa\_man   | 12000.00 |       0.16 |        145 |      80 |

| 109 | Ankita     | Landage   | Not Avaliable        | 7387596547 | 2011-09-14 | sa\_man   |  9000.00 |       0.11 |        145 |      80 |

| 110 | Anita      | Shelar    | Not Avaliable        | 8987895412 | 2020-05-01 | ad\_press | 50000.00 |       0.15 |        114 |      30 |

+-----+------------+-----------+----------------------+------------+------------+----------+----------+------------+------------+---------+
11 rows in set (0.00 sec)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\

**Q7.**

mysql> update Employees

    -> set email = 'Not Avaliable',

    -> commission = 0.10;

Query OK, 11 rows affected (0.07 sec)

Rows matched: 11  Changed: 11  Warnings: 0


mysql> table Employees;
+-----+------------+-----------+---------------+------------+------------+----------+----------+------------+------------+---------+

| eid | first\_name | last\_name | email         | phone\_no   | hire\_date  | job\_id   | salary   | commission | manager\_id | dept\_id |

+-----+------------+-----------+---------------+------------+------------+----------+----------+------------+------------+---------+

| 100 | Sakshi     | Shirke    | Not Avaliable | 8596452145 | 2025-09-13 | ad\_press | 24000.00 |       0.10 |        200 |      10 |

| 101 | Sumit      | Yewale    | Not Avaliable | 8745120023 | 2025-12-30 | ad\_vp    | 17000.00 |       0.10 |        200 |      10 |

| 102 | Meena      | Shedage   | Not Avaliable | 9654785412 | 2024-05-14 | ad\_vp    | 17000.00 |       0.10 |        200 |      10 |

| 103 | Prachi     | Rajpure   | Not Avaliable | 7741200899 | 2025-06-14 | it\_prog  |  9000.00 |       0.10 |        103 |      60 |

| 104 | Shravani   | Pawar     | Not Avaliable | 8854520125 | 2011-04-01 | it\_prog  |  6000.00 |       0.10 |        103 |      60 |

| 105 | Tanvi      | Dhiwar    | Not Avaliable |  774369852 | 2020-12-12 | it\_prog  |  4800.00 |       0.10 |        103 |      60 |

| 106 | Anuj       | Jamdade   | Not Avaliable | 8541200032 | 2015-12-15 | it\_prog  |  4800.00 |       0.10 |        103 |      60 |

| 107 | Suraj      | Shelar    | Not Avaliable | 7823569874 | 2014-02-28 | it\_prog  |  4200.00 |       0.10 |        114 |      30 |

| 108 | Sakshi     | Dhude     | Not Avaliable | 9965214001 | 2022-01-08 | sa\_man   | 12000.00 |       0.10 |        145 |      80 |

| 109 | Ankita     | Landage   | Not Avaliable | 7387596547 | 2011-09-14 | sa\_man   |  9000.00 |       0.10 |        145 |      80 |

| 110 | Anita      | Shelar    | Not Avaliable | 8987895412 | 2020-05-01 | ad\_press | 50000.00 |       0.10 |        114 |      30 |

+-----+------------+-----------+---------------+------------+------------+----------+----------+------------+------------+---------+



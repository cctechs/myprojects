
create table t_product
(
    pid int(11) PRIMARY KEY,
    pname VARCHAR(100) not NULL,
    pcode VARCHAR(100),
    premark VARCHAR(100),
    pnum int,
    pcreateTime DATETIME
);


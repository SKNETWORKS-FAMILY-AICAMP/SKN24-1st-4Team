create database if not exists traffic;

use traffic;

-- 테이블이 있을 시 삭제 
drop table if exists tbl_road;
drop table if exists tbl_registed_car;
drop table if exists tbl_speed_limit;
drop table if exists tbl_congestion;


 create table if not exists tbl_registed_car(
    registed_region    varchar(15) not null comment '권역구분',
    registed_month    varchar(30) not null comment'등록 월',
    registed_car_num    int comment '등록 차량 수',
    primary key (registed_region, registed_month)
) engine=INNODB comment '구별차량현황';

create table if not exists tbl_road(
		road_id int unsigned not null auto_increment comment '도로코드',
        registed_region varchar(15) not null comment '권역구분(FK)',
        road_name varchar(20) not null comment '도로명', 
		start_point varchar(20) not null comment '시점',
        end_point varchar(20) not null comment '종점',
        derection varchar(3) not null comment '방향',
        primary key(road_id),
        foreign key(registed_region) references tbl_registed_car(registed_region)
) engine=INNODB comment '도로';

create table if not exists tbl_speed_limit(
		road_code int unsigned not null comment '도로코드(FK)',
		road_type varchar(10) not null comment '도로유형구분',
        speen_limit tinyint unsigned not null comment '제한속도',
        foreign key (road_code) references tbl_road(road_id)
)engine=INNODB comment '제한속도';

create table if not exists tbl_congestion(
		road_code int unsigned not null comment '도로코드(FK)',
		date_id int not null comment '날짜',
        average_speed  decimal(5,2) not null comment '평균속도',
        primary key(road_code),
        foreign key (road_code) references tbl_road(road_id)
) engine=INNODB comment '혼잡도';


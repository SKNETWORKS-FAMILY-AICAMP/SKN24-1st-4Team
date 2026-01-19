drop database traffic;
create database if not exists traffic; # db 생성

use traffic;

-- 테이블이 있을 시 삭제 
drop table if exists tbl_road;
drop table if exists tbl_registed_car;
drop table if exists tbl_speed_limit;
drop table if exists tbl_congestion;
drop table if exists faq;


 create table if not exists tbl_registed_car(
    registed_region    varchar(15) not null comment '권역구분',
    registed_month    varchar(30) not null comment'등록 월',
    registed_car_num    int comment '등록 차량 수',
    primary key (registed_region, registed_month)
) engine=INNODB comment '구별차량현황';

create table if not exists tbl_road(
		road_id bigint unsigned not null comment '링크아이디(도로코드)',
        registed_region varchar(15) not null comment '권역구분(FK)',
        road_name varchar(20) not null comment '도로명', 
        road_distance int unsigned not null comment '거리',
		start_point varchar(20) not null comment '시점',
        end_point varchar(20) not null comment '종점',
        derection varchar(3) not null comment '방향',
        primary key(road_id)
) engine=INNODB comment '도로';

create table if not exists tbl_speed_limit(
		road_code bigint unsigned not null comment '도로코드(FK)',
		road_type varchar(10) not null comment '도로유형구분',
        speed_limit tinyint unsigned not null comment '제한속도',
        foreign key (road_code) references tbl_road(road_id)
)engine=INNODB comment '제한속도';

create table if not exists tbl_congestion(
		road_code bigint unsigned not null comment '도로코드(FK)',
		date_id int not null comment '날짜',
        average_speed  decimal(5,2) not null comment '평균속도',
        primary key(road_code, date_id),
        foreign key (road_code) references tbl_road(road_id)
) engine=INNODB comment '혼잡도';

CREATE TABLE IF NOT EXISTS tbl_faq(
    faq_id INT AUTO_INCREMENT COMMENT 'faq 번호',
    faq_title VARCHAR(600) NOT NULL COMMENT 'faq 제목',
    faq_contents TEXT NOT NULL COMMENT 'faq 내용',
    faq_section VARCHAR(20) NOT NULL COMMENT 'faq 구분',
    PRIMARY KEY (faq_id)
) ENGINE=INNODB COMMENT '자주 묻는 질문';

--================================
--|  Скрипт для создания таблиц  |
--================================

-- 1. Спортивное сооружение
CREATE TABLE sports_facility (
    facility_id   NUMBER PRIMARY KEY,
    facility_name VARCHAR2(100) NOT NULL,
    facility_type VARCHAR2(30)  NOT NULL,
    CONSTRAINT CK_facility_type CHECK (
        facility_type IN ('Hall', 'Arena', 'Stadium')
    )
);

-- 2. Спортсмены
CREATE TABLE athlete (
    athlete_id   NUMBER PRIMARY KEY,
    first_name   VARCHAR2(50) NOT NULL,
    last_name    VARCHAR2(50) NOT NULL,
    date_of_birth DATE
);

-- 3. Соревнования
CREATE TABLE competition_result (
    result_id      NUMBER PRIMARY KEY,
    athlete_id     NUMBER NOT NULL,
    facility_id    NUMBER,
    competition_name VARCHAR2(150) NOT NULL,
    sport_name     VARCHAR2(80),
    competition_date DATE,
    place          NUMBER,
    CONSTRAINT CK_place CHECK (place > 0 AND place < 1000),
    CONSTRAINT FK_comp_res_athlete FOREIGN KEY (athlete_id)
        REFERENCES athlete(athlete_id),
    CONSTRAINT FK_comp_res_facility FOREIGN KEY (facility_id)
        REFERENCES sports_facility(facility_id)
);

SELECT 'Tables have been created successfully' AS Massege FROM DUAL;
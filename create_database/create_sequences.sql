--=============================================
--|  Скрипт для создания последовательностей  |
--=============================================

CREATE SEQUENCE SEQ_facility_id START WITH 1 INCREMENT BY 1;

CREATE SEQUENCE SEQ_athlete_id START WITH 1 INCREMENT BY 1;

CREATE SEQUENCE SEQ_competition_result_id START WITH 1 INCREMENT BY 1;

SELECT 'Sequences have been created successfully' AS Massege FROM DUAL;
--===================================
--|  Скрипт для создания триггеров  |
--===================================

CREATE OR REPLACE TRIGGER TRG_sports_facility_id
BEFORE INSERT ON sports_facility
FOR EACH ROW
BEGIN
  SELECT SEQ_facility_id.NEXTVAL INTO :NEW.facility_id FROM DUAL;
END;
/

CREATE OR REPLACE TRIGGER TRG_athlete_id
BEFORE INSERT ON athlete
FOR EACH ROW
BEGIN
  SELECT SEQ_athlete_id.NEXTVAL INTO :NEW.athlete_id FROM DUAL;
END;
/

CREATE OR REPLACE TRIGGER TRG_competition_result_id
BEFORE INSERT ON competition_result
FOR EACH ROW
BEGIN
  SELECT SEQ_competition_result_id.NEXTVAL INTO :NEW.result_id FROM DUAL;
END;
/

SELECT 'Triggers have been created successfully' AS Massege FROM DUAL;
--=============================================
--|  Скрипт для удаления последовательностей  |
--=============================================

BEGIN
  EXECUTE IMMEDIATE 'DROP SEQUENCE SEQ_facility_id';
  EXCEPTION
    WHEN OTHERS THEN
      IF SQLCODE != -2289 THEN 
        RAISE;
      END IF;
END;
/

BEGIN
  EXECUTE IMMEDIATE 'DROP SEQUENCE SEQ_athlete_id';
  EXCEPTION
    WHEN OTHERS THEN
      IF SQLCODE != -2289 THEN
        RAISE;
      END IF;
END;
/

BEGIN
  EXECUTE IMMEDIATE 'DROP SEQUENCE SEQ_competition_result_id';
  EXCEPTION
    WHEN OTHERS THEN
      IF SQLCODE != -2289 THEN
        RAISE;
      END IF;
END;
/

SELECT 'Sequences have been successfully deleted' AS Massege FROM DUAL;
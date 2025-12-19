--===================================
--|  Скрипт для удаления триггеров  |
--===================================

BEGIN
  EXECUTE IMMEDIATE 'DROP TRIGGER TRG_sports_facility_id';
  EXCEPTION
    WHEN OTHERS THEN
      IF SQLCODE != -4080 THEN
        RAISE;
      END IF;
END;
/

BEGIN
  EXECUTE IMMEDIATE 'DROP TRIGGER TRG_athlete_id';
  EXCEPTION
    WHEN OTHERS THEN
      IF SQLCODE != -4080 THEN
        RAISE;
      END IF;
END;
/

BEGIN
  EXECUTE IMMEDIATE 'DROP TRIGGER TRG_competition_result_id';
  EXCEPTION
    WHEN OTHERS THEN
      IF SQLCODE != -4080 THEN
        RAISE;
      END IF;
END;
/

SELECT 'Triggers have been successfully deleted' AS Massege FROM DUAL;
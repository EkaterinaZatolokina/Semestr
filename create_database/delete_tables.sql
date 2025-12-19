--================================
--|  Скрипт для удаления таблиц  |
--================================

BEGIN
  EXECUTE IMMEDIATE 'DROP TABLE competition_result CASCADE CONSTRAINTS';
  EXCEPTION
    WHEN OTHERS THEN
      IF SQLCODE != -942 THEN
        RAISE;
      END IF;
END;
/

BEGIN
  EXECUTE IMMEDIATE 'DROP TABLE athlete CASCADE CONSTRAINTS';
  EXCEPTION
    WHEN OTHERS THEN
      IF SQLCODE != -942 THEN
        RAISE;
      END IF;
END;
/

BEGIN
  EXECUTE IMMEDIATE 'DROP TABLE sports_facility CASCADE CONSTRAINTS';
  EXCEPTION
    WHEN OTHERS THEN
      IF SQLCODE != -942 THEN
        RAISE;
      END IF;
END;
/

SELECT 'Tables have been deleted successfully' AS Massege FROM DUAL;
--===================================
--|    Триггеры для логирования     |
--===================================

BEGIN
  EXECUTE IMMEDIATE 'DROP TRIGGER sports_facility_audit_trg';
EXCEPTION WHEN OTHERS THEN NULL; END;
/

BEGIN
  EXECUTE IMMEDIATE 'DROP TRIGGER athlete_audit_trg';
EXCEPTION WHEN OTHERS THEN NULL; END;
/

BEGIN
  EXECUTE IMMEDIATE 'DROP TRIGGER competition_result_audit_trg';
EXCEPTION WHEN OTHERS THEN NULL; END;
/

CREATE OR REPLACE TRIGGER sports_facility_audit_trg
    AFTER INSERT OR UPDATE OR DELETE ON sports_facility
    FOR EACH ROW
DECLARE
    v_operation VARCHAR2(10);
    v_old_data VARCHAR2(200);
    v_new_data VARCHAR2(200);
BEGIN
    IF INSERTING THEN
        v_operation := 'INSERT';
        v_new_data := 'facility_id=' || :NEW.facility_id || 
                     ',facility_name=' || :NEW.facility_name || 
                     ',facility_type=' || :NEW.facility_type;
    ELSIF UPDATING THEN
        v_operation := 'UPDATE';
        v_old_data := 'facility_id=' || :OLD.facility_id || 
                     ',facility_name=' || :OLD.facility_name || 
                     ',facility_type=' || :OLD.facility_type;
        v_new_data := 'facility_id=' || :NEW.facility_id || 
                     ',facility_name=' || :NEW.facility_name || 
                     ',facility_type=' || :NEW.facility_type;
    ELSIF DELETING THEN
        v_operation := 'DELETE';
        v_old_data := 'facility_id=' || :OLD.facility_id || 
                     ',facility_name=' || :OLD.facility_name || 
                     ',facility_type=' || :OLD.facility_type;
    END IF;
    
    INSERT INTO audit_log (log_id, table_name, operation_type, old_data, new_data)
    VALUES (audit_log_seq.NEXTVAL, 'SPORTS_FACILITY', v_operation, v_old_data, v_new_data);
END;
/

CREATE OR REPLACE TRIGGER athlete_audit_trg
    AFTER INSERT OR UPDATE OR DELETE ON athlete
    FOR EACH ROW
DECLARE
    v_operation VARCHAR2(10);
    v_old_data VARCHAR2(400);
    v_new_data VARCHAR2(400);
BEGIN
    IF INSERTING THEN
        v_operation := 'INSERT';
        v_new_data := 'athlete_id=' || :NEW.athlete_id || 
                     ',first_name=' || :NEW.first_name || 
                     ',last_name=' || :NEW.last_name || 
                     ',date_of_birth=' || TO_CHAR(:NEW.date_of_birth, 'YYYY-MM-DD');
    ELSIF UPDATING THEN
        v_operation := 'UPDATE';
        v_old_data := 'athlete_id=' || :OLD.athlete_id || 
                     ',first_name=' || :OLD.first_name || 
                     ',last_name=' || :OLD.last_name || 
                     ',date_of_birth=' || TO_CHAR(:OLD.date_of_birth, 'YYYY-MM-DD');
        v_new_data := 'athlete_id=' || :NEW.athlete_id || 
                     ',first_name=' || :NEW.first_name || 
                     ',last_name=' || :NEW.last_name || 
                     ',date_of_birth=' || TO_CHAR(:NEW.date_of_birth, 'YYYY-MM-DD');
    ELSIF DELETING THEN
        v_operation := 'DELETE';
        v_old_data := 'athlete_id=' || :OLD.athlete_id || 
                     ',first_name=' || :OLD.first_name || 
                     ',last_name=' || :OLD.last_name || 
                     ',date_of_birth=' || TO_CHAR(:OLD.date_of_birth, 'YYYY-MM-DD');
    END IF;
    
    INSERT INTO audit_log (log_id, table_name, operation_type, old_data, new_data)
    VALUES (audit_log_seq.NEXTVAL, 'ATHLETE', v_operation, v_old_data, v_new_data);
END;
/

CREATE OR REPLACE TRIGGER competition_result_audit_trg
    AFTER INSERT OR UPDATE OR DELETE ON competition_result
    FOR EACH ROW
DECLARE
    v_operation VARCHAR2(10);
    v_old_data VARCHAR2(400);
    v_new_data VARCHAR2(400);
BEGIN
    IF INSERTING THEN
        v_operation := 'INSERT';
        v_new_data := 'result_id=' || :NEW.result_id || 
                     ',athlete_id=' || :NEW.athlete_id || 
                     ',facility_id=' || NVL(:NEW.facility_id, 'NULL') || 
                     ',competition_name=' || :NEW.competition_name || 
                     ',sport_name=' || NVL(:NEW.sport_name, 'NULL') || 
                     ',competition_date=' || TO_CHAR(:NEW.competition_date, 'YYYY-MM-DD') || 
                     ',place=' || :NEW.place;
    ELSIF UPDATING THEN
        v_operation := 'UPDATE';
        v_old_data := 'result_id=' || :OLD.result_id || 
                     ',athlete_id=' || :OLD.athlete_id || 
                     ',facility_id=' || NVL(:OLD.facility_id, 'NULL') || 
                     ',competition_name=' || :OLD.competition_name || 
                     ',sport_name=' || NVL(:OLD.sport_name, 'NULL') || 
                     ',competition_date=' || TO_CHAR(:OLD.competition_date, 'YYYY-MM-DD') || 
                     ',place=' || :OLD.place;
        v_new_data := 'result_id=' || :NEW.result_id || 
                     ',athlete_id=' || :NEW.athlete_id || 
                     ',facility_id=' || NVL(:NEW.facility_id, 'NULL') || 
                     ',competition_name=' || :NEW.competition_name || 
                     ',sport_name=' || NVL(:NEW.sport_name, 'NULL') || 
                     ',competition_date=' || TO_CHAR(:NEW.competition_date, 'YYYY-MM-DD') || 
                     ',place=' || :NEW.place;
    ELSIF DELETING THEN
        v_operation := 'DELETE';
        v_old_data := 'result_id=' || :OLD.result_id || 
                     ',athlete_id=' || :OLD.athlete_id || 
                     ',facility_id=' || NVL(:OLD.facility_id, 'NULL') || 
                     ',competition_name=' || :OLD.competition_name || 
                     ',sport_name=' || NVL(:OLD.sport_name, 'NULL') || 
                     ',competition_date=' || TO_CHAR(:OLD.competition_date, 'YYYY-MM-DD') || 
                     ',place=' || :OLD.place;
    END IF;
    
    INSERT INTO audit_log (log_id, table_name, operation_type, old_data, new_data)
    VALUES (audit_log_seq.NEXTVAL, 'COMPETITION_RESULT', v_operation, v_old_data, v_new_data);
END;
/


--==================================
--|  Скрипт для заполнения таблиц  |
--==================================

-- Спортивные сооружения
INSERT INTO sports_facility (facility_name, facility_type) VALUES ('Central Stadium', 'Stadium');
INSERT INTO sports_facility (facility_name, facility_type) VALUES ('Ice Palace "Kristallix"', 'Arena');
INSERT INTO sports_facility (facility_name, facility_type) VALUES ('Dynamo Sports Hall', 'Hall');
INSERT INTO sports_facility (facility_name, facility_type) VALUES ('Elite Tennis Court', 'Hall');
INSERT INTO sports_facility (facility_name, facility_type) VALUES ('Olymp Basketball court', 'Hall');
INSERT INTO sports_facility (facility_name, facility_type) VALUES ('Yunost football field', 'Stadium');
INSERT INTO sports_facility (facility_name, facility_type) VALUES ('Iskra volleyball court', 'Hall');

-- Спортсмены
INSERT INTO athlete (first_name, last_name, date_of_birth) VALUES ('Andrey', 'Smirnov', DATE '1995-03-10');
INSERT INTO athlete (first_name, last_name, date_of_birth) VALUES ('Alexander', 'Dutchev', DATE '1998-07-22');
INSERT INTO athlete (first_name, last_name, date_of_birth) VALUES ('Maxim', 'Strugatsky', DATE '1992-11-15');
INSERT INTO athlete (first_name, last_name, date_of_birth) VALUES ('Ilya', 'Pikul', DATE '1997-05-01');
INSERT INTO athlete (first_name, last_name, date_of_birth) VALUES ('Egor', 'Novikov', DATE '2000-09-28');
INSERT INTO athlete (first_name, last_name, date_of_birth) VALUES ('Roman', 'Babechev', DATE '1999-02-18');
INSERT INTO athlete (first_name, last_name, date_of_birth) VALUES ('Artyom', 'Messi', DATE '1996-04-05');
INSERT INTO athlete (first_name, last_name, date_of_birth) VALUES ('Nikita', 'Zazin', DATE '1994-08-12');
INSERT INTO athlete (first_name, last_name, date_of_birth) VALUES ('Kirill', 'Ronaldo', DATE '1993-06-08');
INSERT INTO athlete (first_name, last_name, date_of_birth) VALUES ('Denis', 'Valera', DATE '2001-10-20');

-- Соревнования

INSERT INTO competition_result (athlete_id, facility_id, competition_name, sport_name, competition_date, place)
VALUES (1, 1, 'Football City Championship', 'Football', DATE '2024-05-20', 1);
INSERT INTO competition_result (athlete_id, facility_id, competition_name, sport_name, competition_date, place)
VALUES (2, 1, 'Football City Championship', 'Football', DATE '2024-05-20', 2);
INSERT INTO competition_result (athlete_id, facility_id, competition_name, sport_name, competition_date, place)
VALUES (3, 2, 'Cup Hockey Tournament', 'Hockey', DATE '2024-11-10', 1);
INSERT INTO competition_result (athlete_id, facility_id, competition_name, sport_name, competition_date, place)
VALUES (4, 2, 'Cup Hockey Tournament', 'Hockey', DATE '2024-11-10', 2);
INSERT INTO competition_result (athlete_id, facility_id, competition_name, sport_name, competition_date, place)
VALUES (5, 3, 'City Basketball Championship', 'Basketball', DATE '2024-09-20', 1);
INSERT INTO competition_result (athlete_id, facility_id, competition_name, sport_name, competition_date, place)
VALUES (6, 3, 'City Basketball Championship', 'Basketball', DATE '2024-09-20', 2);
INSERT INTO competition_result (athlete_id, facility_id, competition_name, sport_name, competition_date, place)
VALUES (7, 4, 'Open Tennis tournament', 'Tennis', DATE '2024-06-12', 1);
INSERT INTO competition_result (athlete_id, facility_id, competition_name, sport_name, competition_date, place)
VALUES (8, 4, 'Open Tennis tournament', 'Tennis', DATE '2024-06-12', 2);
INSERT INTO competition_result (athlete_id, facility_id, competition_name, sport_name, competition_date, place)
VALUES (9, 5, 'Iskra Volleyball Tournament', 'Volleyball', DATE '2024-07-05', 1);
INSERT INTO competition_result (athlete_id, facility_id, competition_name, sport_name, competition_date, place)
VALUES (10, 5, 'Iskra Volleyball Tournament', 'Volleyball', DATE '2024-07-05', 2);


SELECT 'Data has been added successfully' AS Message FROM DUAL;

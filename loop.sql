CREATE TABLE Results_copy AS SELECT * FROM Results;
DELETE FROM Results_copy

DO $$
 BEGIN
 	FOR counter IN 1..20
		LOOP
			INSERT INTO Results_copy
			 VALUES (random() * 100, random() * 20 + 1, random() * 2 + 1, random() * 5 + 1);
		END LOOP;
 END;
 $$
 
SELECT * FROM Results_copy;
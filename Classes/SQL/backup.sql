
--Backup
-- mysqldump utility to be used for backup
mysqldump -u root -p datascience > datascience_backup.sql

-- Restore
mysql -u root -p datascience > datascience_backup.sql
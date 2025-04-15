-- It commits the change only if everything works fine
-- Else it will get rollback
Start Transaction or Begin
 update film set title = 'bha'
 where film_id between 1 to 1000

commit ;

Rollback;
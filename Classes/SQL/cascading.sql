Create table employee(
    Id INT Primary,
    Child_id Int,
    Foreign key (Child_id)
    References parenttable(parent_id)
    on delete cascade
    on update cascade
)

-- cascade --> deletes the entries in child table
-- set null --> foreign key is set to null
-- set default --> sets foreign key with some default value
-- restrict ---> it prevents the actions if it releated to child tables 
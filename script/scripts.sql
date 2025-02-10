alter table transactions add column modified_by text;

alter table transactions add column modified_at timestamp;

alter table transactions add column change_info jsonb;

create or replace function record_change_columns()
returns trigger as $$
declare
change_details jsonb;
begin
change_details := '{}'::JSONB; --empty json object
if new.amount is distinct from old.amount then
change_details := jsonb_insert(change_details, '{amount}', jsonb_build_object('old', old.amount, 'new', new.amount));
end if;
--adding the user and timestamp
change_details := change_details || jsonb_build_object('modified_by', current_user, 'modified_at', now());
--update change info column
new.change_info := change_details;
new.modified_by := current_user;
new.modified_at := current_timestamp;
return new;
end; 
$$ language plpgsql;

create trigger trigger_record_change_info 
before update on transactions
for each row execute function record_change_columns();
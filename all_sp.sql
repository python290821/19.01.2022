CREATE or replace function sp_get_max3(_x integer, _y integer, _z integer)
 returns integer
 language plpgsql AS
     $$
         BEGIN
             if _x >_y and _x > _z then
                 return _x;
             elseif _y > _z then
                 return _y;
             else
                 return _z;
             end if;
         end;
     $$;


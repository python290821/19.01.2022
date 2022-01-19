
## sample code

# ------------------------------------- Create/update sp
# first way -- write the sp hard coded
local_session.execute(f'''CREATE or replace function sp_get_max3(_x integer, _y integer, _z integer)
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
     $$;''')
local_session.commit()

# second way -- read the sp code from the sql file and run
# read content of file
# run execute on all sp


# ------------------------------------- Execute sp
result = local_session.execute('select * from sp_get_max3(2, 7, 9);')
print('result')
#1
results = [res1 for res1 in result][0][0]
print(results)
#2
#for field in result:
#    print(field[0])

stmt = text('select * from sp_get_max3(:x, :y, :z)').bindparams(x=8, y=10, z=2)
result = local_session.execute(stmt)
results = [res1 for res1 in result][0][0]
print(results)
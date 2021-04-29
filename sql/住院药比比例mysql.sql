select
 department_dict.dept_name as dept_name,
 sum(total_cost) as total_cost,
 CONCAT(FORMAT(sum(xy)/sum(total_cost)*100,2),'%') as xy,
 CONCAT(FORMAT(sum(zcy)/sum(total_cost)*100,2),'%') as zcy,
 CONCAT(FORMAT(sum(ptzj)/sum(total_cost)*100,2),'%') as ptzj,
--  CONCAT(FORMAT(sum(gf)/sum(total_cost)*100,2),'%') as gf,
CONCAT(FORMAT(sum(ctyp)/sum(total_cost)*100,2),'%') as ctyp,
 CONCAT(FORMAT(sum(jzyp)/sum(total_cost)*100,2),'%') as jzyp,
 CONCAT(FORMAT(sum(cw)/sum(total_cost)*100,2),'%') as cw,
--  sum(krt) as krt,
--  sum(xl) as xl,
--  sum(sj) as sj,
 CONCAT(FORMAT(sum(otherDrug)/sum(total_cost)*100,2),'%') as otherDrug
from zyyb,department_dict
where create_date>='{startdate}'
  and create_date<='{enddate}'
  and department_dict.dept_code = zyyb.dept_code
group by zyyb.dept_code,department_dict.dept_name
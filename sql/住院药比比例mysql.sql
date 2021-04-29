select
 department_dict.dept_name as dept_name,
 sum(total_cost) as total_cost, sum(xy)/sum(total_cost) as xy, sum(zcy) as zcy, sum(ptzj) as ptzj, sum(gf) as gf, sum(ctyp) as ctyp, sum(jzyp) as jzyp, sum(cw) as cw, sum(krt) as krt,
        sum(xl) as xl, sum(sj) as sj, sum(otherDrug) as otherDrug from zyyb,department_dict
where create_date>='{startdate}'
  and create_date<='{enddate}'
  and department_dict.dept_code = zyyb.dept_code
group by zyyb.dept_code,department_dict.dept_name
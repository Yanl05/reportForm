select
      to_date('{startdate}', 'YYYY-MM-DD') create_date,
      r.SICK_IN_DEPT dept_code,
       --(select dept_name from department_dict d where d.DEPT_code = r.SICK_IN_DEPT) 科室名称,
       sum(r.cost) total_cost,
  /*     t.ypbl /100 ypbl,   --西成药控
      t.zyzjbl /100 zyzjbl,  --制剂药控
      t.zyypbl /100 zyypbl, --饮片药控*/
    --  nvl(sum(case when r.item_code in('0202025','0201911','0201913','0201918','0201953','0201954','0201966','0201967','0201984','0201994','0201995','0202030','0201684','0201888','0201827','0202003','0201860','0201758','0201885','0201826','0100405','0201802','0200975','0201984','0201680','0200776','0201803','0200944','0201909','0201994','0200800','0201997','0201990','0201918','0202030','0202056','0201995','0201802','0201911') then cost end),0) 靶向药, --靶向药
             SUM(DECODE((select b1.ypzd_jxfl
                    from physic_dict_table b1
                   where b1.physic_code = r.item_code
                     and (r.item_class  like 'A%'
                     or r.item_class  like 'B%'
                     or r.item_class  like 'C%')),
                  'X01',
                  COST,
                  0)) xy,   --西药
       SUM(DECODE((select b1.ypzd_jxfl
                    from physic_dict_table b1
                   where b1.physic_code = r.item_code
                     and (r.item_class  like 'A%'
                     or r.item_class  like 'B%'
                     or r.item_class  like 'C%')),
                  'X02',
                  COST,
                  0)) zcy,   --中成药
             SUM(DECODE((select b1.ypzd_jxfl
                    from physic_dict_table b1
                   where b1.physic_code = r.item_code
                     and (r.item_class  like 'A%'
                     or r.item_class  like 'B%'
                     or r.item_class  like 'C%')),
                  'Y01',
                  COST,
                  0)) ptzj,   --普通制剂

              SUM(DECODE((select b1.ypzd_jxfl
                    from physic_dict_table b1
                   where b1.physic_code = r.item_code
                     and (r.item_class  like 'A%'
                     or r.item_class  like 'B%'
                     or r.item_class  like 'C%')),
                  'Y02',
                  COST,
                  0)) gf,   --膏方制剂
              SUM(DECODE((select b1.ypzd_jxfl
                    from physic_dict_table b1
                   where b1.physic_code = r.item_code
                     and (r.item_class  like 'A%'
                     or r.item_class  like 'B%'
                     or r.item_class  like 'C%')),
                  'Z01',
                  COST,
                  0)) ctyp,   --中药传统饮片
              SUM(DECODE((select b1.ypzd_jxfl
                    from physic_dict_table b1
                   where b1.physic_code = r.item_code
                     and (r.item_class  like 'A%'
                     or r.item_class  like 'B%'
                     or r.item_class  like 'C%')),
                  'Z02',
                  COST,
                  0)) jzyp,   --中药精制饮片
              SUM(DECODE((select b1.ypzd_jxfl
                    from physic_dict_table b1
                   where b1.physic_code = r.item_code
                     and (r.item_class  like 'A%'
                     or r.item_class  like 'B%'
                     or r.item_class  like 'C%')),
                  'Z0301',
                  COST,
                  0)) cw,   --超微
               SUM(DECODE((select b1.ypzd_jxfl
                    from physic_dict_table b1
                   where b1.physic_code = r.item_code
                     and (r.item_class  like 'A%'
                     or r.item_class  like 'B%'
                     or r.item_class  like 'C%')),
                  'Z0302',
                  COST,
                  0)) krt,   --康仁堂
                SUM(DECODE((select b1.ypzd_jxfl
                    from physic_dict_table b1
                   where b1.physic_code = r.item_code
                     and (r.item_class  like 'A%'
                     or r.item_class  like 'B%'
                     or r.item_class  like 'C%')),
                  'Z0303',
                  COST,
                  0)) xl,   --新绿
                SUM(DECODE((select b1.ypzd_jxfl
                    from physic_dict_table b1
                   where b1.physic_code = r.item_code
                     and (r.item_class  like 'A%'
                     or r.item_class  like 'B%'
                     or r.item_class  like 'C%')),
                  'Z0304',
                  COST,
                  0)) sj,   --三九
                SUM(DECODE((select nvl(b1.ypzd_jxfl,'G1')
                    from physic_dict_table b1
                   where b1.physic_code = r.item_code
                     and (r.item_class  like 'A%'
                     or r.item_class  like 'B%'
                     or r.item_class  like 'C%')),
                  'G1',
                  COST,
                  0)) otherDrug  --未分类药品
from residence_sick_price_item r --left join temp_rep_kshdypbl@jlhis t on r.SICK_IN_DEPT=t.dept_code
where r.item_name <> '医保返还'
and r.archive is null
and 1=1
and r.apply_no is not null
 and
 (operation_time>=to_date('{startdate}', 'YYYY-MM-DD') )  and
 (operation_time <to_date('{enddate}', 'YYYY-MM-DD'))
group by r.SICK_IN_DEPT --,t.ypbl, t.zyzjbl, t.zyypbl
order by (select SEQUENCE from  DEPARTMENT_DICT d where d.dept_code=r.SICK_IN_DEPT)
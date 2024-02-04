INSERT INTO
  ootaka_sandbox_db.public.region
SELECT
  r_regionkey,
  r_name,
  r_comment
FROM
  snowflake_sample_data.tpch_sf1.region
;

INSERT INTO
  ootaka_sandbox_db.public.region_and_nation
SELECT
  r_regionkey,
  r_name,
  r_comment,
  n_nationkey,
  n_name,
  n_comment
FROM
  ootaka_sandbox_db.public.region
INNER JOIN snowflake_sample_data.tpch_sf1.nation ON
  region.r_regionkey = nation.n_regionkey
;
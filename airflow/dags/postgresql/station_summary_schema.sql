CREATE TABLE IF NOT EXISTS station_summary (
  ID double precision DEFAULT NULL,
  flow_99 double precision DEFAULT NULL,
  flow_max double precision DEFAULT NULL,
  flow_median double precision DEFAULT NULL,
  flow_total double precision DEFAULT NULL,
  n_obs double precision DEFAULT NULL
)
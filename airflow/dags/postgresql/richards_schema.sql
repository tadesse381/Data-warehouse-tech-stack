CREATE TABLE IF NOT EXISTS richards (
  timestamp text,
  flow1 DOUBLE PRECISION DEFAULT NULL,
  occupancy1 DOUBLE PRECISION DEFAULT NULL,
  flow2 DOUBLE PRECISION DEFAULT NULL,
  occupancy2 DOUBLE PRECISION DEFAULT NULL,
  flow3 DOUBLE PRECISION DEFAULT NULL,
  occupancy3 DOUBLE PRECISION DEFAULT NULL,
  totalflow DOUBLE PRECISION DEFAULT NULL,
  weekday DOUBLE PRECISION DEFAULT NULL,
  hour DOUBLE PRECISION DEFAULT NULL,
  minute DOUBLE PRECISION DEFAULT NULL,
  second DOUBLE PRECISION DEFAULT NULL
)
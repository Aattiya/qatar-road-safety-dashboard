# Data source: Qatar Open Data Portal - data.gov.qa
# Columns dropped (>75% null): WEATHER, ROAD_STATUS, ACCIDENT_REASON, ACCIDENT_NATURE
# Usable columns: ACCIDENT_YEAR, ACCIDENT_TIME, CITY, ZONE, ACCIDENT_SEVERITY,
#                 ACCIDENT_CLASSIFICATION, DEATH_COUNT, NATIONALITY_GROUP
# IMPORTANT: Use SUM(TOTAL) to count accidents, never COUNT(*)
# 2025 excluded from trend analysis (partial year)
# 2020 flagged as COVID anomaly

import duckdb

con = duckdb.connect("C:/Users/ahmed/OneDrive/Desktop/AI Directory/Accidents Dashboard/accidents.db")

con.execute("""
    CREATE TABLE IF NOT EXISTS accidents AS
    SELECT * FROM read_csv_auto(
        'C:/Users/ahmed/OneDrive/Desktop/AI Directory/Accidents Dashboard/accident.csv',
        delim=';'
    )
""")

print(f"Loaded {con.execute('SELECT COUNT(*) FROM accidents').fetchone()[0]:,} rows")
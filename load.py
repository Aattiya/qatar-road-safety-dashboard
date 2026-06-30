import duckdb

con = duckdb.connect("C:/Users/ahmed/OneDrive/Desktop/AI Directory/Accidents Dashboard/accidents.db")

result = con.execute("""
    SELECT
        COUNT(*) as row_count,
        SUM(TOTAL) as actual_accidents
    FROM accidents
""").fetchdf()

print(result.to_string())


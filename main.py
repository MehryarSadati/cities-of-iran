import polars as pl

cities = pl.read_csv("csv/shahr.csv")
provinces = pl.read_csv("csv/ostan.csv")

city = input()
result = cities.filter(pl.col("name") == city)
province_code = result["ostan"].item() if result.height > 0 else None

province_name = provinces.filter(pl.col("id") == province_code)
final_answer = province_name["name"].to_list

if province_code:
    print(final_answer)

else:
    print(f"sorry we don't have the city of {city} in our dataset")
import pandas as pd

air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)

print(air_quality.head())

air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

print(air_quality.head())

air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "Antwerp",
        "station_london": "London",
        "station_paris": "Paris",
    }
)

print(air_quality_renamed.head())

air_quality_renamed.plot()
1==1
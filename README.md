# UTMB_index_precision
this repo is try to evaluate the precision of UTMB index given to all runner, to do so i scrape data of UTMB race from UTMB official website

## SCRAPED RACES : 53

is interesting to notice how UTMB index is still a good number to evaluate an athlete, in this code you can see however how in a lot of race there's about 10 to 20 % of outliers that don't match the prediction

I set a threshold of 2 stnd deviation to define an outliers 

## I share my data in this repo because UTMB give it for free at the public 

the data are on data_races in json format

enjoy the charts :D 

```bash
streamlit run frontend.py
```
to run the code and see the results ( in the ) ScrapingUTMB folder

### All the data are in json format in the ScrapingUTMB/data_races folder

![Screenshot from 2024-11-28 14-04-28](https://github.com/user-attachments/assets/35c6eec5-d0f2-48e4-940b-1bec0cbdad61)

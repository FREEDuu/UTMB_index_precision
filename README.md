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
to run the code and see the results 

![Screenshot from 2024-11-15 15-31-28](https://github.com/user-attachments/assets/f68d4482-83be-4fc1-bc22-89a2041c4180)

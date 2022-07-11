# Visualize Covid-19 cases in Shanghai from2022-03-01

update ended in 4th July 2022

## Acquire the reported Covid-19 cases in SH

1. Scrap data from [上海本地宝](http://m.sh.bendibao.com/)
    - local_url="http://m.sh.bendibao.com/mip/233243.html"
    - data provide in a [table](http://m.sh.bendibao.com/mip/233243.html)
      ![table_data](https://cdn.jsdelivr.net/gh/zlmturnout/MyGithubIMG/BlogImg/SHCovide19-datatable0517.jpg)
2. scrap all items from table

```python
# acquire html
html_resp = download(local_url)
assert html_resp, '数据获取错误'
html_soup = BeautifulSoup(html_resp, 'html.parser')
tr = html_soup.find('table').find_all('tr')  # 查找表格内所有内容
table_info = tr[0].find_all('td')[0].text.replace('\t', '').replace('\n', '').split('\r')
```

3. data structure  
   SH_COVID19_DATA structure

   note: no death data in the table [table_url](http://m.sh.bendibao.com/mip/233243.html)

| date       | NewInfection | NewAsymptomatic | AllInfection | AllAsymptomatic | Death |
|------------|--------------|-----------------|--------------|-----------------|-------|
| 2022-05-12 | 227          | 1869            | 56754        | 581422          | 0     |
| 2022-05-11 | 144          | 1305            | 56527        | 579553          | 0     |
| ...        | ...          | ...             | ...          | ...             | ...   |

## Transform and save data

1. dict data form:  
   **SH_COVID19_DATA:**

> {"Date":list[date], "NewInfection": list[int], "NewAsymptomatic": list[int],
"AllInfection": list[int], "AllAsymptomatic": list[int], "Death": list[int] }

2. transform to pandas dataframe

3. save pandas dataframe data to sqltable,csv,xlsx,json

## plot data

via plotnine

1. line-plot
2. Calendar plot

results:
![area_fill_covid19-SH2022](/save/area_fillCOVID_SH2022.png)
![calendar_mao_covid19-SH2022](/save/calendar_mapCOVID_SH2022.png)
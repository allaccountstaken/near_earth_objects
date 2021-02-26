# Expected Noticable Close Approaches of Near-Earth Objects in 2021
The project uses data from two different data sources and it seemed warranted to start with in-depth visual exploratory data analysis and, also, merge the data to better understand what objects could be visiable this year. 

## Overview
Specifically, it was hypothesized that albedo, relative brightness, and estimated diameter, could help determine what potentially hazardous asteroids could be visible in the nearest future. 
![](https://github.com/allaccountstaken/near_earth_objects/blob/main/imgs/pha_scplt.png)

### Albedo
Relative brightness feature seems to be concentrated around 0.07-0.3 range with only a few rare outliers above 0.5. Objects with value about 0.3 should be considered exceptionally bright.
![](https://github.com/allaccountstaken/near_earth_objects/blob/main/imgs/albedo_bxplt.png)

### Diameter
Size feature as measured by estimated diameter has more outliers, starting from values of around 0.5. Therefore, objects larger than 0.5 could also be considered relatively noticeable.
![](https://github.com/allaccountstaken/near_earth_objects/blob/main/imgs/diameter_bxplt.png)

### Distance
For close approaches the situation is different as the sample already contains potentially hazardous objects that come close by definition. It seems that the cut of point was set at 0.5 and no outliers were included. Approaches with distance smaller than 0.2 should be considered as very close.  
![](https://github.com/allaccountstaken/near_earth_objects/blob/main/imgs/dist_bxplt.png)

### Speed
In order to get an idea of what should be generally expected from approach speed, distribution of relative velocity feature was analyzed. Normal speeds of approach should be around 10-20, although the dataset contains a lot of outliers. 
![](https://github.com/allaccountstaken/near_earth_objects/blob/main/imgs/speed_bxplt.png)

### Expected this year
Finally, close approaches dataset was sorted for 2021 expected dates and joined with objects dataset on unique identifiers associated with potentially hazardous objects. This resulted in `exp_pha_df` table with 56 objects that may be visible during the year. Noteworthy is the object pdes=523664, with medium size of 0.346 and outstanding brightness of 0.536, for example. Apparently, it is approaching every 3 years and is expected to come back as close as 0.10 again on 2021-Jul-25 22:09.
![](https://github.com/allaccountstaken/near_earth_objects/blob/main/imgs/exp_pha_bbplt.png)

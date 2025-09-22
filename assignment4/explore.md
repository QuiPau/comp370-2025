
-	How big is the dataset?

There are 36860 words in the data set and the size the data set is 4870970.
I have used this 2 commands: 
- wc -l clean_dialog.csv
- stat -c %s clean_dialog.csv

-	What’s the structure of the data?

"title","writer","pony","dialog" are the fields of the data

-	How many episodes does it cover?
197
I used this command: 

sort | cut -d ',' -f1 clean_dialog.csv | uniq | wc -l

-	During the exploration phase, find at least one aspect of the dataset that is unexpected – meaning that it seems like it could create issues for later analysis.

The Pony field display multiple Pony which will be a problem to know which pony is talking.

To get the total line_count for each pony, I wrote the following grep command:
cut -d ',' -f3 clean_dialog.csv | grep -Eow 'Twilight Sparkle|Rarity|Pinkie Pie|Rainbow Dash|Fluttershy' | sort | uniq -c
Giving me: 
   2045 Fluttershy
   2691 Pinkie Pie
   2848 Rainbow Dash
   2433 Rarity

Then to count the number of total lines I simply executed the following command:
wc -l clean_dialog.csv

Finally I had to generate the Line_percentage.csv, to do I created a short python script with the previous grep output.

csv_generator.py:


import pandas as pd

total_lines = 36860

data = {
    'pony_name' : ['Twilight Sparkle', 'Rarity', 'Pinkie Pie', 'Rainbow Dash', 'Fluttershy'],
    'total_line_count' : ['2045', '2691', '2848', '2433', '4381'],
    'percent_all_lines' : [f'{round((2045/total_lines)*100, 4)}%', f'{round((2691/total_lines)*100,4)}%', f'{round((2848/total_lines)*100, 4)}%', f'{round((2433/total_lines)*100,4)}%', f'{round((4381/total_lines)*100,4)}%']
}

df = pd.DataFrame(data)
df.to_csv('Line_percentages.csv', index=False)


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

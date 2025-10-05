## Task 1

Version 1: Are the noise issues tend to stem from different causes across the year.
Version 2: Do the causes of noise complaints (Commercial, helicopter, etc ...) vary by month across the year?
Version 3: Using the Complaint Type "Noise" and Descriptor fields, do the frequencies of specific noise complaint types vary across months in 2024?
Version 4: What is the monthly distribution of each Noise complaint descriptor.

Noise - Commercial
Noise - Helicopter
Noise - House of Worship (église)
Noise - Park
Noise - Residential
Noise - Street/Sidewalk
Noise - Vehicle

Banging/Pounding (Coup de poing/coup de pied)
Car/Truck Horn
Car/Truck Music
Double Parked Blocking Vehicle
Engine Idling
In Public
Loud Music/Party
Loud Talking
Loud Television
News Gathering

## Task 2

Version 1: Where in the city rats and mice are most likely to create sanitation issues
Version 2: For complaints classified as 'Rodent', which Location Types are reported most frequently?
Version 3: Across complaints involving either 'Rodent' or 'Dead Animal', which Location Types are most commonly reported?


grep -E "Dead Animal|Rodent" 311_2024.csv | cut -d "," -f7 | sort | uniq -c | sort -nr

25191 Rat Sighting
6885 Condition Attracting Rodents
5604 Signs of Rodents
4124 Cat
4028 Rodents/Insects/Garbage
2047 Mouse Sighting
1963 Rodent Sighting
1347 Rat or Mouse
1057 Raccoon
774 Opossum
726 Dead Animal
720 Bird
701 Squirrel
587 Other
521 Dog
290 Rodents/Mice
149 Deer

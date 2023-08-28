# pythiwlgen
<h2>Python Word List Generator</h2>

Combination of bash and python to add extra flavours to passwords for password cracking.
Only use this tool for legal penetration activities.

I built this tool because I wanted to create a personal flavour of Hashcat rules, but this was just easier to do for me. Plus it was good to get into Python again fo a bit.

Current shell script will call 3 functionalities:
- obfuscate chars so that the character 'a' will turn into @ and 4, 'e' into a 3, etc
- add birth years to all the combinations. Starting with the year that you can insert as parameter.
- adding exclamation marks to all possible passwords

This script doesn't really tae into account wrong user input.

<b>Usage:</b>
sh ./createDictionary.sh {/path/to/input/file} {year}
for example: sh ./createDictionary.sh ~/Downloads/file 1950

<b>Example of an input file:</n>

test
Amsterdam

<b>output (when parameter 2021 is passed):</b>
4mst3rd4m
4mst3rd4m!
4mst3rd4m2021
4mst3rd4m2021!
4mst3rd4m2022
4mst3rd4m2022!
4mst3rd4m2023
4mst3rd4m2023!
4mst3rdam
4mst3rdam!
4mst3rdam2021
4mst3rdam2021!
4mst3rdam2022
4mst3rdam2022!
4mst3rdam2023
4mst3rdam2023!
4mst3rd@m
4mst3rd@m!
4mst3rd@m2021
4mst3rd@m2021!
4mst3rd@m2022
4mst3rd@m2022!
4mst3rd@m2023
4mst3rd@m2023!
4msterd4m
4msterd4m!
4msterd4m2021
4msterd4m2021!
4msterd4m2022
4msterd4m2022!
4msterd4m2023
4msterd4m2023!
4msterdam
4msterdam!
4msterdam2021
4msterdam2021!
4msterdam2022
4msterdam2022!
4msterdam2023
4msterdam2023!
4msterd@m
4msterd@m!
4msterd@m2021
4msterd@m2021!
4msterd@m2022
4msterd@m2022!
4msterd@m2023
4msterd@m2023!
Amst3rd4m
Amst3rd4m!
Amst3rd4m2021
Amst3rd4m2021!
Amst3rd4m2022
Amst3rd4m2022!
Amst3rd4m2023
Amst3rd4m2023!
Amst3rdam
Amst3rdam!
Amst3rdam2021
Amst3rdam2021!
Amst3rdam2022
Amst3rdam2022!
Amst3rdam2023
Amst3rdam2023!
Amst3rd@m
Amst3rd@m!
Amst3rd@m2021
Amst3rd@m2021!
Amst3rd@m2022
Amst3rd@m2022!
Amst3rd@m2023
Amst3rd@m2023!
Amsterd4m
Amsterd4m!
Amsterd4m2021
Amsterd4m2021!
Amsterd4m2022
Amsterd4m2022!
Amsterd4m2023
Amsterd4m2023!
Amsterdam
Amsterdam!
Amsterdam2021
Amsterdam2021!
Amsterdam2022
Amsterdam2022!
Amsterdam2023
Amsterdam2023!
Amsterd@m
Amsterd@m!
Amsterd@m2021
Amsterd@m2021!
Amsterd@m2022
Amsterd@m2022!
Amsterd@m2023
Amsterd@m2023!
@mst3rd4m
@mst3rd4m!
@mst3rd4m2021
@mst3rd4m2021!
@mst3rd4m2022
@mst3rd4m2022!
@mst3rd4m2023
@mst3rd4m2023!
@mst3rdam
@mst3rdam!
@mst3rdam2021
@mst3rdam2021!
@mst3rdam2022
@mst3rdam2022!
@mst3rdam2023
@mst3rdam2023!
@mst3rd@m
@mst3rd@m!
@mst3rd@m2021
@mst3rd@m2021!
@mst3rd@m2022
@mst3rd@m2022!
@mst3rd@m2023
@mst3rd@m2023!
@msterd4m
@msterd4m!
@msterd4m2021
@msterd4m2021!
@msterd4m2022
@msterd4m2022!
@msterd4m2023
@msterd4m2023!
@msterdam
@msterdam!
@msterdam2021
@msterdam2021!
@msterdam2022
@msterdam2022!
@msterdam2023
@msterdam2023!
@msterd@m
@msterd@m!
@msterd@m2021
@msterd@m2021!
@msterd@m2022
@msterd@m2022!
@msterd@m2023
@msterd@m2023!
t3st
t3st!
t3st2021
t3st2021!
t3st2022
t3st2022!
t3st2023
t3st2023!
test
test!
test2021
test2021!
test2022
test2022!
test2023
test2023!

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

test<br>
Amsterdam

<b>output (when parameter 2021 is passed):</b>

4mst3rd4m<br>
4mst3rd4m!<br>
4mst3rd4m2021<br>
4mst3rd4m2021!<br>
4mst3rd4m2022<br>
4mst3rd4m2022!<br>
4mst3rd4m2023<br>
4mst3rd4m2023!<br>
4mst3rdam<br>
4mst3rdam!<br>
4mst3rdam2021<br>
4mst3rdam2021!<br>
4mst3rdam2022<br>
4mst3rdam2022!<br>
4mst3rdam2023<br>
4mst3rdam2023!<br>
4mst3rd@m<br>
4mst3rd@m!<br>
4mst3rd@m2021<br>
4mst3rd@m2021!<br>
4mst3rd@m2022<br>
4mst3rd@m2022!<br>
4mst3rd@m2023<br>
4mst3rd@m2023!<br>
4msterd4m<br>
4msterd4m!<br>
4msterd4m2021<br>
4msterd4m2021!<br>
4msterd4m2022<br>
4msterd4m2022!<br>
4msterd4m2023<br>
4msterd4m2023!<br>
4msterdam<br>
4msterdam!<br>
4msterdam2021<br>
4msterdam2021!<br>
4msterdam2022<br>
4msterdam2022!<br>
4msterdam2023<br>
4msterdam2023!<br>
4msterd@m<br>
4msterd@m!<br>
4msterd@m2021<br>
4msterd@m2021!<br>
4msterd@m2022<br>
4msterd@m2022!<br>
4msterd@m2023<br>
4msterd@m2023!<br>
Amst3rd4m<br>
Amst3rd4m!<br>
Amst3rd4m2021<br>
Amst3rd4m2021!<br>
Amst3rd4m2022<br>
Amst3rd4m2022!<br>
Amst3rd4m2023<br>
Amst3rd4m2023!<br>
Amst3rdam<br>
Amst3rdam!<br>
Amst3rdam2021<br>
Amst3rdam2021!<br>
Amst3rdam2022<br>
Amst3rdam2022!<br>
Amst3rdam2023<br>
Amst3rdam2023!<br>
Amst3rd@m<br>
Amst3rd@m!<br>
Amst3rd@m2021<br>
Amst3rd@m2021!<br>
Amst3rd@m2022<br>
Amst3rd@m2022!<br>
Amst3rd@m2023<br>
Amst3rd@m2023!<br>
Amsterd4m<br>
Amsterd4m!<br>
Amsterd4m2021<br>
Amsterd4m2021!<br>
Amsterd4m2022<br>
Amsterd4m2022!<br>
Amsterd4m2023<br>
Amsterd4m2023!<br>
Amsterdam<br>
Amsterdam!<br>
Amsterdam2021<br>
Amsterdam2021!<br>
Amsterdam2022<br>
Amsterdam2022!<br>
Amsterdam202<br>
Amsterdam2023!<br>
Amsterd@m<br>
Amsterd@m!<br>
Amsterd@m2021<br>
Amsterd@m2021!<br>
Amsterd@m2022<br>
Amsterd@m2022!<br>
Amsterd@m2023<br>
Amsterd@m2023!<br>
@mst3rd4m<br>
@mst3rd4m!<br>
@mst3rd4m2021<br>
@mst3rd4m2021!<br>
@mst3rd4m2022<br>
@mst3rd4m2022!<br>
@mst3rd4m2023<br>
@mst3rd4m2023!<br>
@mst3rdam<br>
@mst3rdam!<br>
@mst3rdam2021<br>
@mst3rdam2021!<br>
@mst3rdam2022<br>
@mst3rdam2022!<br>
@mst3rdam2023<br>
@mst3rda2023!<br>
@mst3rd@m<br>
@mst3rd@m!<br>
@mst3rd@m2021<br>
@mst3rd@m2021!<br>
@mst3rd@m2022<br>
@mst3rd@m2022!<br>
@mst3rd@m2023<br>
@mst3rd@m2023!<br>
@msterd4m<br>
@msterd4m!<br>
@msterd4m2021<br>
@msterd4m2021!<br>
@msterd4m2022<br>
@msterd4m2022!<br>
@msterd4m2023<br>
@msterd4m2023!<br>
@msterdam<br>
@msterdam!<br>
@msterdam2021<br>
@msterdam2021!<br>
@msterdam2022<br>
@msterdam2022!<br>
@msterdam2023<br>
@msterdam2023!<br>
@msterd@m<br>
@msterd@m!<br>
@msterd@m2021<br>
@msterd@m2021!<br>
@msterd@m2022<br>
@msterd@m2022!<br>
@msterd@m2023<br>
@msterd@m2023!<br>
t3st<br>
t3st!<br>
t3st2021<br>
t3st2021!<br>
t3st2022<br>
t3st2022!<br>
t3st2023<br>
t3st2023!<br>
test<br>
test!<br>
test2021<br>
test2021!<br>
test2022<br>
test2022!<br>
test2023<br>
test2023!<br>
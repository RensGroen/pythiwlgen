mkdir ./tmp
python3 ./obfuscatechars.py input=$1 output=./tmp/result_char_obfuscation.txt
python3 ./addYears.py fromYear=$2 input=./tmp/result_char_obfuscation.txt output=./tmp/result_addYears.txt
python3 ./addExclamationMark.py input=./tmp/result_addYears.txt output=./tmp/result_exclamation_mark.txt
python3 ./addExclamationMark.py input=./tmp/result_char_obfuscation.txt output=./tmp/result_chars_obfuscation_and_exlamation_mark.txt
cat ./tmp/result_char_obfuscation.txt ./tmp/result_addYears.txt ./tmp/result_exclamation_mark.txt ./tmp/result_chars_obfuscation_and_exlamation_mark.txt | sort -u > result.txt
rm -r ./tmp
echo 'finished!'
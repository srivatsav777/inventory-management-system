grep -i -A 16 "Op rate" tem.json > temp.json
cat temp.json > tem.json
rm temp.json
sed -i 's/^/"/' tem.json
sed -i 's/$/"/' tem.json
sed -i 's/:/":"/1' tem.json
sed -i 's/ //g' tem.json
sed -i ' s/$/,/' tem.json
sed -i '1 s/^/{/' tem.json
sed -i '$ s/,//' tem.json
sed -i '$ s/$/}/' tem.json


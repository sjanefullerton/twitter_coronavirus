# file will loop over each file in dataset and run the map.py command
for file in '/data/Twitter dataset/'geoTwitter20*; do
    ./src/map.py --input_path="$file" &
done

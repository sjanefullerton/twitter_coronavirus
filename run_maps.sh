# file will loop over each file in dataset and run the map.py command
#!/bin/sh
for file in /data/Twitter dataset/geoTwitter20-*.zip; do
	echo "Running map.py on $file"
    ./src/map.py --input_path="$file" &
done

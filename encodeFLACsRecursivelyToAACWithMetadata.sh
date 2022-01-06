ffmpeg -i "${1}" -f caf - 2>/dev/null| fdkaac -b160 - -o "${1%.flac}".m4a 2>/dev/null
ffmpeg -i "${1}" tmp.png 2>/dev/null
mp4art --add tmp.png "${1%.flac}".m4a
rm tmp.png

iphone 照片 HEIC 文件转jpg 方便训练

mkdir -p jpg_output
for file in *.HEIC; do
    sips -s format jpeg "$file" --out "jpg_output/${file%.*}.jpg"
done

HERE=`pwd`

docker run -v $HERE:/usr/vol --rm --name boto3_instance \
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    akrieger/boto3 python /usr/src/upload_files.py --bucket $TARGET_BUCKET --dir ./output
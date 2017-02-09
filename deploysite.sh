HERE=`pwd`

docker run -v $HERE:/usr/vol --rm --name boto3_instance \
    -e AWS_ACCESS_KEY=$AWS_ACCESS_KEY \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    akrieger/boto3 python upload_files.py --bucket $TARGET_BUCKET --dir ./output
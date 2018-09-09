HERE=`pwd`

docker run --rm --name akblog_pelican -it -v $HERE:/usr/src akrieger/pelican

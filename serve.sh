#!/bin/bash
DIR=`pwd`/output

docker run --name akblog_instance -v $DIR:/usr/share/nginx/html:ro -p 8000:80 -d nginx
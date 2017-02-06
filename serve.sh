#!/bin/bash
SERVEPATH=$1
echo $SERVEPATH
(cd $SERVEPATH && python -m SimpleHTTPServer 8000)
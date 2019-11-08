#!/usr/bin/env bash
# cd server
# virtualenv venv3
# virtualenv --no-site-packages -p /usr/local/opt/bin/python3.7 venv3
virtualenv --no-site-packages -p /usr/bin/python3.5 venv3
source venv3/bin/activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tushare
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple lxml
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple bs4
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple grpcio-tools

cd server
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/tushare.proto

python tushare-server2.py
# python tushare-server.py
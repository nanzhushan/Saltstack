参考：
http://www.xiaomastack.com/2014/11/18/salt-api/

开始前也需要安装salt的api
yum install -y salt-api python-cherrypy

证书生成：
useradd -M -s /sbin/nologin saltapi
passwd saltapi
cd /etc/pki/tls/certs/
make testcert
一路回车
cd /etc/pki/tls/private/
openssl rsa -in localhost.key -out localhost_nopass.key


关于salt的配置文件请看目录下的:
master
master.d 

推荐安装：
ipython：

wget https://cloud.github.com/downloads/ipython/ipython/ipython-0.13.tar.gz
tar xzf ...
python setup.py install


测试语句：
curl -k https://192.168.0.197:8888/login -H "Accept: application/x-yaml" -d username='saltapi' -d password='password' -d eauth='pam'
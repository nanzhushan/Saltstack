官方文档：
https://github.com/saltstack/salt-api


在salt-api官方文档中，对python访问API给出了如下的格式要求:


###########################################################
[{
    "client": "local",
    "tgt": "*",
    "fun": "test.fib",
    "arg": ["10"]
},
{
    "client": "runner",
    "fun": "jobs.lookup_jid",
    "jid": "20130603122505459265"
}]

###########################################
以上的JSON代码中，指定了API去执行两个命令，一个模块命令，一个runner命令.

格式转换工具:
http://pro.jsonlint.com/

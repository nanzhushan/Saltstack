参考：
https://docs.saltstack.com/en/latest/ref/clients/


对于salt的访问，可以使用salt的api接口 当然也可以使用
salt.client

>>> import salt.client
>>> client = salt.client.LocalClient()
>>> ret = client.cmd('*','test.ping')
>>> ret
{'192.168.2.92': True}

参考：
https://docs.saltstack.com/en/latest/ref/clients/


对于salt的访问，可以使用salt的api接口 当然也可以使用(非常方便，但是原来是python2.6.6,千万不要升级到python2.7不然，website是用python2.7开发的跑步起来)
salt.client

>>> import salt.client
>>> client = salt.client.LocalClient()
>>> ret = client.cmd('*','test.ping')
>>> ret
{'192.168.2.92': True}

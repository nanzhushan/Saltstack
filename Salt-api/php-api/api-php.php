<?php
/*
@author knight 
 */
function get_token(){
global $token;
$url = 'https://192.168.0.197:8000/login'; //ip是已经配好的api地址如 192.168.0.197
$ch = curl_init($url);
curl_setopt($ch,CURLOPT_POST,TRUE);
curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,2);
curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,False);
curl_setopt($ch,CURLOPT_HTTPHEADER, Array('Accept: application/x-yaml'));
curl_setopt($ch,CURLOPT_POSTFIELDS, 'username=saltapi&password=password&eauth=pam');
curl_setopt($ch,CURLOPT_RETURNTRANSFER,TRUE);
$token = curl_exec($ch);
$token = strstr($token, 'token', false);  //取登录后返回字符串中的token
$token = strstr($token, 'user', true);
$token = explode(" ",$token);
curl_close($ch);
$token = rtrim($token,"\n"); //删掉token字符串最后面的'\n'，不然后面死活登不上去
}
 
//适用于带一个或不带参数的salt exc模块如 salt \* test.ping 或 salt \* test.echo "hello"这样的模块
function exc_salt($tgt, $fun, $arg, $arg_num){
global $token;
global $report;
$url = 'https://192.168.0.197:8000/';
$ch = curl_init($url);
curl_setopt($ch,CURLOPT_POST,TRUE);
curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,2);
curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,False);
curl_setopt($ch,CURLOPT_HTTPHEADER,Array('Accept: application/x-yaml',"X-Auth-Token: $token"));
if ($arg_num)
    curl_setopt($ch,CURLOPT_POSTFIELDS,"client=local&tgt=$tgt&fun=$fun&arg=$arg");
else
    curl_setopt($ch,CURLOPT_POSTFIELDS,"client=local&tgt=$tgt&fun=$fun");
curl_setopt($ch,CURLOPT_RETURNTRANSFER,TRUE);
$report = curl_exec($ch);
curl_close($ch);
return $report;
}
 
//适用于带两个参数的salt exc模块
function exc_salt_2($tgt, $fun, $arg_1, $arg_2){
global $token;
global $report;
$url = 'https://192.168.0.197:8000/';
$ch = curl_init($url);
curl_setopt($ch,CURLOPT_POST,TRUE);
curl_setopt($ch,CURLOPT_SSL_VERIFYHOST,2);
curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,False);
curl_setopt($ch,CURLOPT_HTTPHEADER,Array('Accept: application/x-yaml',"X-Auth-Token: $token"));
curl_setopt($ch,CURLOPT_POSTFIELDS,"client=local&tgt=$tgt&fun=$fun&arg=$arg_1&arg=$arg_2");
curl_setopt($ch,CURLOPT_RETURNTRANSFER,TRUE);
$report = curl_exec($ch);
curl_close($ch);
return $report;
}
 
//以下是测试这个脚本功能的部分，正式上线是得注释掉
get_token();
print exc_salt('HD1', 'test.echo', 'hello', 1); //带一个参数的
print exc_salt('HD1', 'test.ping', '', 0);  //不带参数的
?>
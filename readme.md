
微信公众平台web应用服务器

在官方api文档基础上改写：
https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1472017492_58YV5

用于基于树莓派的共享拍立得项目。内容是用户回复图片码，自动回复名称对应的本地图片；新用户订阅，发送使用指示。

使用说明：
1.授权。
	/authorize/handle.py改token值。运行/authorize/main.py，选择80端口(sudo python /authorize/main.py 80)。
	微信公众号的开发者配置中填写token值、ip等配置，提交，完成token认证。启动开发者模式。
2.运行服务器。
	若要使用临时素材，basic.py中修改appId、appSecret。
	运行/main.py，选择80端口(sudo python main.py 80)。
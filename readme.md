爬虫封装
----
封装request
* 传入URL (需要自己定义url)
* user_agent 
* headers (封装了一个请求头,如有需要覆盖即可)
* data    (Post传参的话 data必不可少,需要注意的是data并没有封装进去,需要自己以字典格式传递参数, 会自动转换成bytes数组)
* urlopen 
* 返回bytes 数组 (封装了urlopen 会返回一个bytes数组)
* get or post (封装了两种方法,需要注意的是使用Post必须穿data)
首先导入`form packaging import get, post`

有两种方法可供调用 
* get
* post 
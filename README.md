# citylist

我们通过量化指标、数据可视化、智能推荐系统、文本分析系统*为不同目的的消费者提供城市选择、租房找工作的解决方案。

解决方案/目标人群：

- 选择城市

1. 毕业后找一个城市发展（考虑职业发展、职业规划、父母地址等）
2. 考虑幼儿成长的城市选择（父母职业发展、孩子的教育等）
3. 老人养老（兴趣、医疗环境、交通、其他家属常居地等）

- 选择公司与住所

1. 有了工作，想要找一个合适的房子（考虑房子的价格、通勤时间、交通方式、时间等）
2. 有房子，想要找一个合适的公司上班（职业、薪资、通勤时间等）
3. 既没有工作也没有房子（职业、工资期望、通勤时间等）





## 技术栈

Django3.0.4+MySQL5.7+Nginx

`ecahrts` `jquery` `boostrap` `baidu map api`

未来：`redis` `mongo` `vue` `高德API` `postgresql` 



## Deploy

```shell
git clone git@github.com:Nickszy/citylist.git
cd citylist
python -m venv venv
source venv/bin/activate #加载虚拟环境Unix
venv/Scripts/activate.bat # 加载虚拟环境 windows
pip install -r requirements.txt
python manage.py runserver 1235  #启动django，端口1235
```

 静态资源找我要，图片和其他的一些数据没放在github里面。


 ## todo

- 用户
   - [ ] 基本情况（职业、家庭住址、学校等）
   - [ ] 每一段经历（城市印象与工资）
   - [ ] 关注、点击
- city
    - [ ] 基于统计局数据分析
    - [ ] 环境分析
    - [ ] 房价分析
    - [ ] 关系链分析
    - [ ] 职业分析
- 投资
    - [ ] 投资地介绍
    - [ ] 政策介绍
    - [ ] 相关数据呈现(房价、交通等)
    - [ ] 资料下载
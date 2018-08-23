##  [图片下载]()

一个超简单的获取淘宝图片的爬虫

## 原理
1:根据关键字搜索获取页面

2:找到商品列表展示图

3:下载

## 用法

- 安装依赖:sudo pip install requests

```
===根据关键字获取淘宝商品列表图片===
根据提示：
1：输入你的关键字 
2：输入你所需页数（每页44个）
3：输入保存路径 
===================================
  输入你的关键字:短裙
  输入你所需页数（每页44个）:1
  输入保存路径:/Users/tem
开始获取关键字为：短裙的商品图片
http://g-search2.alicdn.com/img/bao/uploaded/i4/i2/152/9352.jpg
http://g-search2.alicdn.com/img/bao/uploaded/i4/i2/152/9358.jpg
http://g-search2.alicdn.com/img/bao/uploaded/i4/i2/152/9355.jpg
...
done:共计：44

```



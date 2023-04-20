import random


def Interview():
    Interview1 = 'os 和 sys 模块的作用'
    Interview2 = '谈谈你对面向对象的理解'
    Interview3 = 'Python面向对象中的继承有什么特点'
    Interview4 = '如何生成一个随机数?'
    Interview5 = '简述什么是 FBV和CBV?'
    Interview6 = '常用字符串格式化哪几种?'
    Interview7 = '面向对象中super的作用?'
    Interview8 = '列举Http 请求中常见的请求方式?'
    Interview9 = '列举Http 请求中的状态码?'
    Interview10 = '如何使用 django orm 批量创建数据?'

    data_list = [
        Interview1, Interview2, Interview3, Interview4, Interview5,
        Interview6, Interview7, Interview8, Interview9, Interview10
    ]

    questions = random.sample(data_list, 5)
    return questions

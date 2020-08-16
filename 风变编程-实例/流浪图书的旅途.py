'''
Description: 类的创建和运用 
Version: Demo.0.0
Autor: Kiasher
Date: 2020-07-29 11:27:42
LastEditors: Kiasher
LastEditTime: 2020-08-09 12:46:33
'''

class Book(object):
    def __init__(self, name, author, comment, state = 0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state
    
    def __str__(self):
        if self.state == 0:
            status = '未借出'
        else:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status)

class BookManager(object):
    books = []

    def __init__(self):
        book1 = Book('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。',1)
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)

    def menu(self):
        print("欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n ")
        while True:
            print('\n=============================================================== \n')
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_book()
                # 调用对象方法时self不能忘
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            elif choice == 5:
                print('感谢使用！愿你我成为爱书之人，在茫茫书海里相遇。\n')
                break
            else:
                print('请输入数字（1 - 5）重新选择：\n')
    
    def show_all_book(self):
        for book in self.books:
            print(book)

    def add_book(self):
        while True:
            name = input('请输入书籍名称: \n')
            author = input('请输入书籍作者: \n')
            comment = input('请输入推荐语: \n')
            state = 0
            new_book = Book(name, author, comment)
            self.books.append(new_book)
            decision = int(input('书籍添加成功！是否继续添加？ (0)No (1)Yes: \n'))
            if decision == 0:
                break

    def check_book(self,name):
        for book in self.books:
            if book.name == name:
                 return book   
        else:
            return None

    def lend_book(self):
        name = input('请输入书籍的名称：')
        res = self.check_book(name)
        # 将name作为参数调用check_book方法，并将返回值赋值给变量res
        if res != None:
        # 如果返回值不等于None值，即返回的是实例对象
            if res.state == 1:
            # 如果实例对象的属性state为1，即借阅状态为已租借
                print('你来晚了一步，这本书已经被借走了噢')
            else:
            # 如果state为0
                print('借阅成功，借了不看会变胖噢～')
                res.state = 1
                # 书籍借出后属性state变为1
        else:
        # 如果返回值为None值
            print('这本书暂时没有收录在系统里呢')    

    def return_book(self):
        name = input('请输入归还书籍的名称：')
        res = self.check_book(name)
        if res == None:
            print('没有这本书噢，你恐怕输错了书名～')
        else:
            if res.state == 0:
                print('这本书没有被借走，在等待有缘人的垂青呢！')
            else:
                print('归还成功！')
                res.state = 0

manager = BookManager()
manager.menu()
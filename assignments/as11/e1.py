class 出版物:
    def __init__(self, 标题):
        self.标题 = 标题
    def 获取(self):
        for 属性, 值 in self.__dict__.items():
            print(f"{属性}: {值}") if 值 != "不详" else None
class 书籍(出版物):
    def __init__(self, 标题, 作者, 页数):
        super().__init__(标题)
        self.作者 = 作者
        self.页数 = 页数
class 杂志(出版物):
    def __init__(self, 标题, 编辑, 期数="不详"):
        super().__init__(标题)
        self.编辑 = 编辑
        self.期数 = 期数
if __name__ == "__main__":
    书 = 书籍("Compartment No. 6", "Rosa Liksom", 192)
    杂志 = 杂志("Donald Duck", "Aki Hyyppä")
    书.获取()
    print("-----")
    杂志.获取()
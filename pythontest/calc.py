class Calc:
    def add(self,a:int,b:int) ->int:
        return a+b

    def div(self,a:int,b:int)->int:
        try:
            result = a/b
            return result
        except Exception as E:
            print(E)
        finally:
            print("没有打印e就返回了正确的结果")


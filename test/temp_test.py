class A:
    def __init__(self):
        self.__get__()

    def __get__(self):
        print("called")

if __name__=="__main__":
    temp = A()


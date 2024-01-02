
'''
__init__ : 클래스 인스턴스를 생성할 때 실행되는 초기화 함수
'''

'''
__str__ : class magic method 로, 구현되지 않은 상태에서 인스턴스를 print 하면 object 가 나옴. 
'''

'''
__repr__ : repr() 함수가 호출 될 떄 사용 , 엄격한 타입 표현시에 사용 
'''

'''
__dict__ 
'''

class Smartphone:
    def __init__(self, brand, information):
        self.__brand = brand
        self.__information = information
class Flight:
    class_attr = []
    '''
    # 첫번쨰 파라미터는 self 라는 이름을 관례적으로 사용한다.
    # 호출 시 호출한 객체 자신이 전달되기 때문에 self 라는 이름을 사용하게 된 것이다.
    '''

    # init 메소드만 오버라이딩하여 객체를 초기화 할 떄 이용된다.
    def __init__(self):
        print("초기화 함수")

    def add_class_attr(self, number):
        Flight.class_attr.append(number)

    def add_instance_attr(self, number):
        self.class_attr.append(number)

    def get_instance(self):
        print(self.class_attr)

f = Flight()
f.add_instance_attr(5)
f.get_instance()


#Бралатан Роман, б17д_122-А, варінт №2

class Programe:
    def __init__(self):
        while True:
            try:
                self.x = float(input('введіть число у діапазоні (X<=1.39 , X>=67.117)'))
                break
            except ValueError:
                print('Вказано не коректні дані')

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x < 1.39:
            print('замале число')
            raise Warning
        elif x > 67.117:
            print('завелике число')
            raise Warning
        else:
            self.__x = x

    def equation1(self):
        y = self.x**4*1.554+self.x**3*3.859-self.x**2*2.458+self.x*1.851
        return y
    def equation2(self):
        y = self.x**3*2.498-self.x**2*2.055+self.x*5.72
        return y
    def equation3(self):
        y = self.x**2*1.948+self.x*3.572
        return y
    def equation4(self):
        y = self.x*4.314
        return y

def main():
    while True:
        try:
            something = Programe()
            break
        except Warning:
            print('введіть коректне число')
    while True:
        try:
            variant = input('Оберіть формулу:\na) y=x^4*1.554+x^3*3.859-x^2*2.458+x*1.851\nb) y=x^3*2.498-x^2*2.055+x*5.72\nc) y=x^2*1.948+x*3.572\nd) y=x*4.314\n>>> ')
            if variant == 'a' or 'a)':
                print(something.equation1())
                break
            elif variant == 'b' or 'b)':
                print(something.equation2())
                break
            elif variant == 'c' or 'c)':
                print(something.equation3())
                break
            elif variant == 'd' or 'd)':
                print(something.equation4())
                break
            else:
                print('Ви ввели не коректний вибір рівняння')

        except ValueError:
            print('Введіть заново')

if __name__ == '__main__':
    while True:
        main()
        choice = input('Якщо хочете продовжити натисніть 1, все інше - завершити')
        if choice == '1':
            continue
        else:
            break

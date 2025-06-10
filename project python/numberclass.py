import os
#######################################################################################################################

class number:
    num = []

    @classmethod
    def add_num(cls):
        n = int(input("enter len number: "))
        for i in range(n):
            x = int(input(f"enter number{i+1}: "))
            cls.num.append(x)

    @classmethod
    def addeven_num(cls):
        x = []
        y = []
        for i in range(len(cls.num)):
            if i % 2 == 0:
                x.append(cls.num[i])
            else:
                y.append(cls.num[i])
        print(f"even = {x}\n"
              f"odd = {y}")


    @classmethod
    def maxmain_num(cls):
        maxnum = cls.num[0]
        minnum = cls.num[0]
        for i in cls.num:
            if i > maxnum:
                maxnum = i
            if i < minnum:
                minnum = i
        print(f"max = {maxnum}\n"
              f"min = {minnum}")

    @classmethod
    def bubbleinsertion(cls):

        num = int(input("1.bubble"
                        "2.insertion"
                        "which one: "))
        if num == 1:
            x = cls.num
            n = len(cls.num)
            for i in range(n):
                for j in range(n-1):
                    if x[i] > x[j+1]:
                        x[i], x[j+1] = x[j+1], x[i]
            print(f"bubble sort= {x}")
        if num == 2:
            x = cls.num
            n  = len(cls.num)

            for i in range(1 , n):
                j = i - i
                e = x[i]
                while j >=0 and x[j-1] > e:
                    x[j+1] = x[j]
                    j -= 1
                x[j+1] = e

            print(f"insertion sort= {x}")

    @classmethod
    def primemorakab(cls):
        x = []
        y = []
        for i in range(len(cls.num)):
            is_prime = True
            for j in range(2 , i):
                if cls.num[i] % j == 0:
                    is_prime = False
            if is_prime:
                x.append(cls.num[i])
            else:
                y.append(cls.num[i])

        print(f"prime = {x}\n"
              f"morakab = {y}")


def main():

    while True:
        chosnum = int(input("1.add number\n"
                            "2.add and even\n"
                            "3.max and min number\n"
                            "4.bubble sort and insertion sort\n"
                            "5.prime and morakab\n"
                            "6.exit\n"
                            "chose number: "))

        if chosnum == 1:
            number.add_num()
        elif chosnum == 2:
            if not number.num:
                print("not add number please try again")
                continue
            else:
                number.addeven_num()
        elif chosnum == 3:
            if not number.num:
                print("not add number please try again")
                continue
            else:
                number.maxmain_num()
        elif chosnum == 4:
            if not number.num:
                print("not add number please try again")
                continue
            else:
                number.bubbleinsertion()
        elif chosnum == 5:
            if not number.num:
                print("not add number please try again")
                continue
            else:
                number.primemorakab()
        elif chosnum == 6:
            print("exit")
            break
        else:
            print("invalid input please try again.")
            continue

if __name__ == '__main__':
    main()



#######################################################################################################################
os.system('git add .')
os.system('git commit -m "Auto commit"')
os.system('git push')
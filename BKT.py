class BKT:
    def bkt(self, string):
        count = 0
        lst = [0]
        for i in string:
            if i == '(':
                count += 1
                lst.append(count)
            elif i == ')':
                count -= 1
                lst.append(count)
        return max(lst)


str = "A(B(I)(J))(C(H))(D(E)(F(K))(G))"
str1 =  "1(2(3(4(5(6(7(8(9(10(11(12)))))))))))"
bkt = BKT()
print(bkt.bkt(str))
print(bkt.bkt(str1))
class BKT:
    def bkt(self, str):
        count = 0
        lst = [0]
        for i in str1:
            if i == '(':
                count += 1
                lst.append(count)
            elif i == ')':
                count -= 1
                lst.append(count)
        return max(lst)


str = "A(B(I)(J))(C(H))(D(E)(F(K))(G))"
str1 =  "A(B(E(G)F(LM))C)"
bkt = BKT()
print(bkt.bkt(str))
print(bkt.bkt(str1))
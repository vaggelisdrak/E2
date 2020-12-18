import random
import math

class Lista():
    def __init__(self, length): # δημιουργία λίστας πλήθους length ακεραίων μεταξύ 1, length+10
        self.rlist = []
        while len(self.rlist) < length:
            x = random.randint(1,length+10)
            if x not in self.rlist: self.rlist.append(x)
        self.rlist = sorted(self.rlist)
        print("\n\nΔημιουργήθηκε μια λίστα με το εξής περιεχόμενο:\n", self.rlist)

    def binarysearch(self, key):
        step = 1
        lo, hi = 0, len(self.rlist) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.rlist[mid] < key:
                print('BHMA {}: Έλεγχος θέσης lista[{}]={} < {}, ΔΕΝ ΒΡΕΘΗΚΕ'.format(step, mid, self.rlist[mid], key))
                input()
                step += 1
                lo = mid + 1
            elif key < self.rlist[mid]:
                print('BHMA {}: Έλεγχος θέσης lista[{}]={} > {}, ΔΕΝ ΒΡΕΘΗΚΕ'.format(step, mid, self.rlist[mid], key))
                input()
                step += 1
                hi = mid - 1
            else:
                print('BHMA {}: Έλεγχος θέσης lista[{}]={} == {}, ΒΡΕΘΗΚΕ'.format(step, mid, self.rlist[mid], key))
                return mid
        return None

class Main():
    def __init__(self):
        while True:
            try:
                x = int(input('Πόσους ακέραιους θες να περιέχει η λίστα;'))
                l = Lista(x) # δημιουργία λίστας 30 ακεραίων
                y=x+(20/100)*x
                y=int(x)
                key = random.randint(1,y)
                print('Ο μέγιστος αριθμός αναζητησεων ειναι {}'.format(math.ceil(math.log2(x))))
                print('Αναζητάμε τον ακέραιο {}'.format(key))
                l.binarysearch(key)
                nlista = input('Νέα λίστα(ν/ο);')
                if nlista and nlista[0].lower() in "οo": break
            except:
                print('Λάθος καταχώρηση')

if __name__ == '__main__':
    Main()

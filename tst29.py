en = ("U+0041", "U+007A")
gr = ("U+0386", "U+03CE")

class TextAnalyze():
    def __init__(self, txt):
        self.txt = txt
        self.gr_hist = self.histogram(gr)
        self.en_hist = self.histogram(en)

    def histogram(self,ends):
        char_dict={}
        for char in self.txt:
            if char.isalpha():
                if ord(char)>= int(ends[0][2:],16) and ord(char)<= int(ends[1][2:],16):
                    char_dict[char]=char_dict.get(char, 0)+1
        return char_dict

class Menu():
    def __init__(self):
        while True:
            txt = input("κείμενο για ανάλυση:")
            if not txt:
                break
            t = TextAnalyze(txt)
            self.histPrint("Ελληνικά", t.gr_hist)
            self.histPrint("Αγγλικά", t.en_hist)

    def histPrint(self, title, hist):
        print('Ιστόγραμμα - γλώσσα:',title)
        for i in sorted(hist):
            print(i,hist[i]*'*')

Menu()
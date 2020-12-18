import random
import tkinter as tk

class Box():
    theBoxes = {}
    def __init__(self, canvas, place, number):
        self.canvas = canvas
        self.place = place
        self.number = number
        Box.theBoxes[number] = self
        self.draw()
    def draw(self): # γραφική απεικόνιση στοιχείου
        x = self.place[0]
        y = self.place[1]
        self.box = self.canvas.create_rectangle(x,y, x+25, y+25, \
                                outline='#FCE1AD', fill = 'lightyellow')
        if len(str(self.number)) == 1:  mx = 6
        else: mx = 3
        self.text = self.canvas.create_text(x+mx, y+3, text = str(self.number),
                                font = 'Arial 12', anchor = 'nw')

    def hide(self): # διαγραφή στοιχείου
        x = self.place[0]
        y = self.place[1]
        self.box =self.canvas.create_rectangle(x,y, x+25, y+25, \
                                outline='#FCE1AD', fill = 'lightblue')
        if len(str(self.number)) == 1:  mx = 6
        else: mx = 3
        self.text = self.canvas.create_text(x+mx, y+3, text = str(self.number),
                                font = 'Arial 12', anchor = 'nw')

        self.cross1 = self.canvas.create_line(x,y+25,x+25,y,fill='red')
        self.cross2 = self.canvas.create_line(x,y,x+25,y+25,fill='red')
        
    def highlight(self): # έμφαση στο στοιχείο
        x = self.place[0]
        y = self.place[1]
        self.box =self.canvas.create_rectangle(x,y, x+25, y+25, \
                                outline='red', fill = 'yellow')
        if len(str(self.number)) == 1:  mx = 6
        else: mx = 3
        self.text = self.canvas.create_text(x+mx, y+3, text = str(self.number),
                                font = 'Arial 12', anchor = 'nw')

class GUI():
    def __init__(self, root):
        self.root = root
        self.root.geometry('920x300+100+100')
        self.root.resizable(False, False)
        self.root.title('Binary search')
        self.f1 = tk.Frame(self.root)
        self.f1.pack(side = 'top', fill='x')
        self.b0 = tk.Button(self.f1, command=self.show_info, text='( i )', font='Arial 20')
        self.b0.pack(side='left', fil='x', expand=1)
        self.b2 = tk.Button(self.f1, command=self.reset, text=' νέοι αριθμοί...', font='Arial 20')
        self.b2.pack(side='left', fill='x', expand=1)
        self.value = tk.StringVar()
        self.num = tk.Label(self.f1, textvariable=self.value, font='Arial 20', bg='#E6E6E6')
        self.num.pack(side='left', fill='both', expand=1)
        self.b1 = tk.Button(self.f1, command=self.binary_step, text='  βήμα >>', font='Arial 20')
        self.b1.pack(side='left', fill='x', expand=1)
        self.f2 = tk.Frame(self.root)
        self.f2.pack(side='bottom', fill='x')
        self.canvas = tk.Canvas(self.f2, height=50, width=920)
        self.canvas.pack()
        self.f3 = tk.Frame(self.root)
        self.f3.pack(side = 'bottom', fill='x')
        scrol = tk.Scrollbar(self.f3)
        self.text = tk.Text(self.f3, height=10, font='Arial 16', width=100, bg='lightyellow' )
        scrol.pack(side='right', fill='y')
        self.text.pack(side='left', fill='y')
        scrol.config(command=self.text.yview)
        self.text.config(yscrollcommand=scrol.set)
        self.reset()
        self.step = 1
    def show_info(self):
        displayed_text = '''
\nΕΙΚΟΝΟΠΟΙΗΣΗ ΑΛΓΟΡΙΘΜΟΥ ΔΥΑΔΙΚΗΣ ΑΝΑΖΗΤΗΣΗΣ
Δυαδική αναζήτηση ονομάζεται ένας αναδρομικός αλγόριθμος αναζήτησης ενός στοιχείου (το λεγόμενο στοιχείο-κλειδί)
σε έναν ταξινομημένο μονοδιάστατο πίνακα. Ο αλγόριθμος αυτός χρησιμοποιεί την τεχνική Διαίρει και Βασίλευε.
Η δυαδική αναζήτηση στηρίζεται στο γεγονός ότι ο πίνακας είναι ταξινομημένος, με αποτέλεσμα να απαιτούνται log2(n)
συγκρίσεις, όπου n το πλήθος των στοιχείων του πίνακα.
Πατήστε το πλήκτρο [ βήμα >> ] για το επόμενο βήμα στην αναζήτηση
Πατήστε το πλήκτρο [ νέοι αριθμοί ] για νέο πίνακα και νέα τιμή κλειδιού.'''
        self.text.insert('end', displayed_text)
        self.text.see('end')
    def draw_arrow(self, place):
        x0,y0 = place[0]+15, place[1]
        return self.canvas.create_polygon([x0, y0, x0, y0-20, x0, y0, x0-5, y0-5, x0,y0, x0+5,y0-5],
                                          outline='red', width=5)
    def add_text(self, txt):
        print(txt)
        self.text.insert('end', '\n'+txt)
        self.text.see('end')
    def reset(self):
        self.canvas.delete('all')
        for b in Box.theBoxes.values(): del b
        self.rlist = self.create_list()
        self.step = 1
        self.lo = 0
        self.hi = len(self.rlist) - 1
        x0,y0 = 5,25
        for i in self.rlist:
            Box(self.canvas, (x0,y0), i)
            x0 += 30
        self.b1.config(state="normal")
        self.text.delete(1.0, 'end')
        self.value.set(' αναζήτησε τον αριθμό '+str(random.randint(1, 40)))
        to_display = 'Αναζητάμε τον αριθμό {}'.format(self.value.get().split()[-1])
        self.add_text(to_display)
    def hide_boxes(self, l,h):
        for i in self.rlist[l:h+1]:
            Box.theBoxes[i].hide()
    def binary_step(self):
        value = int(self.value.get().split()[-1])
        found = False
        mid = (self.lo + self.hi) // 2
        self.arrow = self.draw_arrow(Box.theBoxes[self.rlist[mid]].place)
        if self.rlist[mid] < value:
            to_display = '>BHMA {}: ο αριθμός {} απορρίπτεται, όπως και όλοι οι μικρότεροι, είναι μικρότερος του {}'.format(self.step, self.rlist[mid],value)
            self.add_text(to_display)
            self.step += 1
            self.hide_boxes(self.lo, mid)
            self.lo = mid + 1
        elif value < self.rlist[mid]:
            to_display = '>BHMA {}: ο αριθμός {} απορρίπτεται, όπως και όλοι οι μεγαλύτεροι, είναι μεγαλύτερος του {}'.format(self.step,self.rlist[mid],value)
            self.add_text( to_display)
            self.step += 1
            self.hide_boxes(mid, self.hi)
            self.hi = mid - 1
        else:
            self.add_text('>BHMA {}: σωστά, ο αριθμός {} βρέθηκε'.format(self.step, value))
            Box.theBoxes[value].highlight()
            found = True
        if self.lo > self.hi :
            self.add_text('ο αριθμός {} δεν υπάρχει στη λίστα'.format(value))
        if self.lo > self.hi or found:
            self.b1.config(state="disabled")
    def create_list(self): # δημιουργία λίστας 30 αριθμών μεταξύ 1,40
        rlist = []
        while len(rlist) < 30:
            x = random.randint(1,40)
            if x not in rlist: rlist.append(x)
        rlist = sorted(rlist)
        #print(rlist)
        return rlist
    
def main():
    root = tk.Tk()
    GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()


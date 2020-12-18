import turtle as tr
import random


class Point():
    '''
    η κλάση Point δημιουργεί σημεία και
    τυπώνει τα αντικείμενα (μια κουκίδα διαμέτρου 2 πίξελ για κάθε σημείο)
    '''

    def __init__(self, x, y, board):
        self.board = board
        self.x = x
        self.y = y
        self._draw()

    def _draw(self):
        # εδώ θα σχεδιαστεί το σημείο
        self.board.mypencil.penup()
        self.board.mypencil.setpos(self.x, self.y)
        self.board.mypencil.pendown()
        self.board.mypencil.begin_fill()
        self.board.mypencil.color('black')
        self.board.mypencil.circle(1)
        self.board.mypencil.end_fill()
    
class Poly():
    '''
    Η κλάση Line δημιουργεί ένα κλειστό πολύγωνο διαδοχικών σημείων
    Έχει τη μέθοδο add_point() που εισάγει ένα ακόμη σημείο στο πολύγωνο
    και σχεδιάζει μια γραμμή ανάμεσα στο νέο σημείο και το προηγούμενό του.
    Αν ένα σημείο είναι πολύ κοντά στο προηγούμενο (διπλό κλικ) τότε ολοκληρώνεται
    το πολύγωνο και γεμίζει με ένα τυχαίο χρώμα.
    Βοηθητικές μέθοδοι:
        _fill_poly() που γεμίζει το πολύγωνο,
        _check_point() που ελέγχει αν το σημείο ταυτίζεται με το προηγούμενο (διπλό κλικ),
        _draw_line() γράφει μια γραμμή ανάμεσα στα διαδοχικά σημεία ή κλείνει
                     το πολύγωνο αν ο χρήστης έχει κάνει διπλό κλικ.
    Η παράμετρος done γίνεται True όταν ολοκληρωθεί η σχεδίαση του πολυγώνου
    '''

    def __init__(self, board):
        r = lambda : random.randint(100,255) # ανώνυμη συνάρτηση δημιουργίας ακεραίων στο διάστημα 100,255
        self.color = "#{:0X}{:0X}{:0X}".format(r(), r(), r()) # τυχαίο παλ χρώμα
        self.board = board
        self.poly = []
        self.done = False


    def add_point(self, new_point):
        check = self._check_points(new_point)  # check if double click
        if not check:
            self.poly.append(new_point)
            if len(self.poly) > 1: self._draw_line()
        else:
            self._draw_line(last=True)
            self._fill_poly()
            self.done = True  # finish

    def _fill_poly(self):
        self.board.mypencil.begin_fill()
        self.board.mypencil.color(self.color)
        self.board.mypencil.goto(self.poly[0].x, self.poly[0].y)
        for p in self.poly[1:]:
            self.board.mypencil.goto(p.x, p.y)
        self.board.mypencil.end_fill()
    
    def _check_points(self, p):
        for pnt in self.poly:
            if abs(pnt.x - p.x) < 2 and abs(pnt.y - p.y) < 2:
                return pnt
        return False

    def _draw_line(self, last=False):
        if last: # connect last to first point
            start = self.poly[-1]
            end = self.poly[0]
        else: # connect last two points
            start = self.poly[-2]
            end = self.poly[-1]
        self.board.mypencil.penup()
        self.board.mypencil.setpos(start.x, start.y)
        self.board.mypencil.pendown()
        self.board.mypencil.color('black')
        self.board.mypencil.setpos(end.x, end.y)
        self.board.mypencil.penup()

class Board():
    '''
    Η κλάση Board δημιουργεί ένα καμβά 800x800, μια γραφίδα (Turtle)
    και περιμένει κλικ onscreenclick(), κάθε φορά που ο χρήστης κάνει
    κλικ καλείται η μέθοδος _check() που δημιουργεί ένα σημείο στη θέση
    του κλικ και προσθέτει το σημείο στην πολυγωνική γραμμή self.poly.
    '''

    def __init__(self):
        self.screen = tr.Screen()
        tr.setup(800, 800)
        tr.title('Ζωγραφίζω πολύγωνα')
        self.mypencil = tr.Turtle()  # η γραφίδα που θα χρησιμοποιήσουμε
        self.mypencil.speed('fastest')
        self.mypencil.hideturtle()
        self.poly = Poly(self)  # δημιούργησε νέα γραμμή
        tr.onscreenclick(self._check)
        self.screen.mainloop()

    def _check(self, x, y):
        new_point = Point(x, y, self)  # δημιούργησε ένα σημείο στη θέση x,y
        if self.poly.done:
            self.poly = Line(self)  # δημιούργησε νέα γραμμή
        self.poly.add_point(new_point)  # προσθήκη σημείου στη γραμμή


if __name__ == '__main__':
    Board()

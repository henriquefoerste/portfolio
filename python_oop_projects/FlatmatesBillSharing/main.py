from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatemate:
    """
    Creates a flatemate person who lives in the flat and pays a share of the bill.
    """
    def __init__(self, name, days_in_house) -> None:
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        return bill.amount * (self.days_in_house / (self.days_in_house + flatmate.days_in_house))

class PDFReport:
    """
    Creates a PDF file that contains data about the flatmates such as their names, their due amount and the period of the bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

        pdf.cell(w=100, h=40, txt='Period:', border=1)
        pdf.cell(w=100, h=40, txt=bill.period, border=1, ln=1)

        pdf.cell(w=150, h=40, txt=flatmate1.name, border=1, align='C', ln=1)
        pdf.cell(w=150, h=40, txt=str(flatmate1.pays(bill, flatmate2)), border=1, align='C', ln=1)

        pdf.cell(w=150, h=40, txt=flatmate2.name, border=1, align='C', ln=1)
        pdf.cell(w=150, h=40, txt=str(flatmate2.pays(bill, flatmate1)), border=1, align='C', ln=1)

        pdf.output(self.filename)


bill = Bill(amount=120, period="March 2021")
john = Flatemate(name='John', days_in_house=20)
marry = Flatemate(name='Marry', days_in_house=25)

pdf_report = PDFReport(filename='bill_report.pdf')
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=bill)

print(john.pays(bill=bill, flatmate=marry))
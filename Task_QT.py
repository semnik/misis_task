import requests
from PyQt4.QtCore import *
from PyQt4.QtGui import *

url='http://testlodtask20172.azurewebsites.net/task'
r = requests.get(url)
dat = r.json()
male_id_ar = []
female_id_ar = []
male_age_ar = []
female_age_ar = []
for i in range(0,len(dat)):
    if dat[i]['sex']=='male':
        male_id_ar.append(dat[i]['id'])
    if dat[i]['sex']=='female':
        female_id_ar.append(dat[i]['id'])
x = {}
y = {}
for i in range(0,len(male_id_ar)):
    r_id_male = 'http://testlodtask20172.azurewebsites.net/task/' + male_id_ar[i]
    g_id_male = requests.get(r_id_male)
    g_dat = g_id_male.json()
    male_age_ar.append(g_dat['age'])
    x[g_dat['age']] = g_dat['name']


for i in range(0,len(female_id_ar)):
    r_id_female = 'http://testlodtask20172.azurewebsites.net/task/' + female_id_ar[i]
    g_id_female = requests.get(r_id_female)
    g_dat_f = g_id_female.json()
    female_age_ar.append(g_dat_f['age'])
    y[g_dat_f['age']] = g_dat_f['name']


class AppForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.create_main_frame()

    def create_main_frame(self):
        page = QWidget()

        self.button = QPushButton('Вывести самых молодых парня и девушку', page)
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()

        vbox1 = QVBoxLayout()


        vbox1.addWidget(self.button)
        page.setLayout(vbox1)
        self.setCentralWidget(page)

        self.connect(self.button, SIGNAL("clicked()"), self.clicked)

    def clicked(self):
        QMessageBox.about(self, "Результат", "Самый молодой парень - %s, самая молодая девушка - %s" % (
            x[min(male_age_ar)], y[min(female_age_ar)]))



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    app.exec_()
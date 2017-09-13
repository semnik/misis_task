import requests
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

print('Самый молодой парень - '+x[min(male_age_ar)])
for i in range(0,len(female_id_ar)):
    r_id_female = 'http://testlodtask20172.azurewebsites.net/task/' + female_id_ar[i]
    g_id_female = requests.get(r_id_female)
    g_dat_f = g_id_female.json()
    female_age_ar.append(g_dat_f['age'])
    y[g_dat_f['age']] = g_dat_f['name']
print('Самая молодая девушка - '+y[min(female_age_ar)])
from departement import Departement
from etudiant import Etudiant

info_dep = Departement('01', 'Informatique', ['MSID', 'IoT', 'Robotique'])

# Pass the 'dep' argument when creating the Etudiant object
etudiant1 = Etudiant("A01", "Mickel", "mike@gmail.com")

print(etudiant1.info_etudiant())
print(info_dep.info_departement())

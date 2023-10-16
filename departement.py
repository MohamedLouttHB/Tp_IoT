class Departement:
    id: str
    nom: str
    filieres: []

    def __init__(self, id, nom,filieres ):
        self.id = id
        self.nom = nom
        self.filieres = filieres

    def info_departement(self):
        return f'Id : {self.id} \nNom : {self.nom} \nMail :  {self.filieres}'


dep1 = Departement('01', 'Informatique', ['MSID','IoT','Robotique'])

#print(dep1.info_departement())
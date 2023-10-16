class Etudiant:
    id: str
    nom: str
    mail: str

    def __init__(self, id, nom, mail):
        self.id = id
        self.nom = nom
        self.mail = mail

    def info_etudiant(self):
        return f'Id : {self.id} \nNom : {self.nom} \nMail :  {self.mail}'


etud1 = Etudiant('111', 'mohamed', 'med@gmail.com')

print(etud1.info_etudiant())
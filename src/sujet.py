
class Sujet:
    def __init__(self):
        self.observateurs = []

    def ajouter_observateur(self, observateur):
        self.observateurs.append(observateur)

    def supprimer_observateur(self, observateur):
        self.observateurs.remove(observateur)

    def notifier_observateurs(self, stock):
        for observateur in self.observateurs:
            observateur.mettre_a_jour(stock)

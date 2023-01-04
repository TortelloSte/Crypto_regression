# from utilities.model import modello_rete
from utilities.file_opening import datas
from utilities.decision_tree import decisiotree
from utilities.regressione import regress


if __name__ == '__main__':
    filepath = './archive/coin_Bitcoin.csv'
    datas(filepath)
    # print(f"errore rete_neurale: {round(modello_rete(filepath))} $")
    print(f"errore decisiontree: {round(decisiotree(filepath))} $")
    print(f"errore regressione lineare: {round(regress(filepath))} $")
    
# from model import modello_rete
from file_opening import datas
from decision_tree import decisiotree


if __name__ == '__main__':
    filepath = './archive/coin_Bitcoin.csv'
    datas(filepath)
    #modello_rete(filepath)
    decisiotree(filepath)
    
baba   =   [["Kardeş -> Baba"],"Baba"]
anne =     [["Kardeş -> Anne"],"Anne"]
kardes =   [["Anne -> Oğul", "Anne -> Kız", "Baba -> Oğul", "Baba -> Kız"],"Kardeş"]

es =       [["Oğul -> Anne", "Oğul -> Baba", "Kız -> Anne", "Kız -> Baba"],"Eş"]

annebaba = [["Anne -> Baba", "Dayı -> Baba" , "Teyze -> Baba"],"Annebaba"]
anneanne = [["Anne -> Anne"],"Anneanne"]
dayi =     [["Annebaba -> Oğul","Anneanne -> Oğul"],"Dayı"]
teyze =    [["Annebaba -> Kız" ,"Anneanne -> Kız"],"Teyze"]

babababa = [["Baba -> Baba", "Amca -> Baba", "Hala -> Baba"],"Babababa"]
babaanne = [["Baba -> Anne"],"Babaanne"]
hala =     [["Babababa -> Kız" ,"Babaanne -> Kız"],"Hala"]
amca =     [["Babababa -> Oğul" ,"Babaanne -> Oğul"],"Amca"]

torun =    [["Oğul -> Oğul","Oğul -> Kız","Kız -> Oğul","Kız -> Kız"],"Torun"]

sulale = [baba, anne, kardes, es, annebaba, anneanne, dayi, teyze, babababa, babaanne, hala, amca, torun]

def kisalt(bilgi):
    for akraba in sulale:
        for baginti in akraba[0]:
            if baginti in bilgi:
                bilgi = bilgi.replace(baginti,akraba[1])
                return kisalt(bilgi)

    return bilgi

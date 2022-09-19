def sort_list(list_to_sort: list) -> list:
    print("liste initiale: ", list_to_sort)
    listeTemp = []
    for i in range(len(list_to_sort)):
        listeTemp.append(list_to_sort[i])
    print("liste temporaire :", listeTemp)

     
    
    return listeTemp


liste = [5,36,12,86,45,27,2,11,35]

print(sort_list(liste))
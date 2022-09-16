def date_gap(date):
    date_sep = date.split(".")
    date_year = (int(date_sep[1]) * 12)
    month_date = int((date_year + int(date_sep[0])))
    return month_date

def month_year(gap):
    if gap < 12:
        return 0
    else:
        return 1 + month_year(gap - 12)
    

events_qty = int(input())

level_lst = input().split(", ")
date_lst = input().split(", ")
events_lst = input().split(", ")
date_tday = input()

level_lst_c = level_lst.copy()

low = 0
medium = 0
high = 0

time_gap_lst = []


for i in range(events_qty):
    time_gap_lst.append(date_gap(date_tday) - date_gap(date_lst[i]))
    if int(time_gap_lst[i]) >= 54:
        level_lst_c[i] = 7 #changing value
    
    if int(level_lst_c[i]) <= 4:
        low += 1
    elif int(level_lst_c[i]) <= 6:
        medium += 1
    elif int(level_lst_c[i]) > 6:
        high += 1

if (low + medium > 0):
    insec_formula = int(((medium/(low + medium)) * 100))



if high == 0 and insec_formula > 20:
    print("Os cálculos mostram que é possível acessar essa linha do tempo sem que haja muitos danos.")
    print(f"Mas é necessário termos cuidado, a taxa de insegurança é de {insec_formula:}%")
elif high == 0 and insec_formula <= 20:
    print("Os cálculos mostram que é possível acessar essa linha do tempo sem que haja muitos danos.\nA chance de sucesso é muito alta. Mudaremos o mundo mais uma vez, dr. Helena Smith.")
elif high > 0:
    print("Realizar essa operação é um grande erro. A humanidade pode entrar em colapso.")
    print(f"Há {high} acontecimento(s) relevante(s). Se as consequências das suas ações anularem algum desses eventos, teremos sérios problemas.")

print()
print("Aqui estão os dados dos acontecimentos:")
for element in range(events_qty):
    list_gap_e = int(time_gap_lst[element])
    list_gap_e_m = (int(time_gap_lst[element]) % 12)
    print(f"{events_lst[element]} | gap: {month_year(list_gap_e)} anos e {list_gap_e_m} meses | nível de relevância: {level_lst[element]}")




def extraindo_data_e_horas(data_e_horas):
    data = data_e_horas.split('T')[0]
    horas = data_e_horas.split('T')[1]
    return data, horas


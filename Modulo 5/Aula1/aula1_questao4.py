from datetime import datetime

data = datetime.now()
data_em_texto = data.strftime("%d/%m/%Y")
print(f"Data: {data_em_texto}")
hora_em_texto = data.strftime("%H:%M")
print(f"Hora: {hora_em_texto}")
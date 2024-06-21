data = input("Digite sua data de nascimento: ex:(dd/mm/aaaa)")
mes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
x = int(data[3:5])
print(f"{data[:2]} de {mes[x-1]} de {data[6:]}")

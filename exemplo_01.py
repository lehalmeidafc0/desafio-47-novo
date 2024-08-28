import pandas as pd

curso = pd.read_excel("cursinho.xlsx")
display(curso)
Dias da semana	Matérias	Alunos presentes	Alunos com falta
0	Segunda-feira	Português	29	1
1	Terça-feira	Matemática	25	5
2	Quarta-feira	História	28	2
3	Quinta-feira	Geográfia	24	7
4	Sexta-feira	Quimica	22	9
5	Sábado	Inglês	18	13
Total de alunos presentes e ausentes durante a semana

total_presentes = curso["Alunos presentes"].sum()
total_faltas = curso["Alunos com falta"].sum()

print(f"Total de alunos presentes na semana: {total_presentes}")
print(f"Total de faltas na semana: {total_faltas}")
Total de alunos presentes na semana: 146
Total de faltas na semana: 37
Porcentual de faltas e presenças

curso["% Presença"] = round((curso["Alunos presentes"] / (curso["Alunos presentes"] + curso["Alunos com falta"])) * 100, 2)
curso["% Falta"] = round((curso["Alunos com falta"] / (curso["Alunos presentes"] + curso["Alunos com falta"])) * 100, 2)

print(curso)
  Dias da semana    Matérias  Alunos presentes  Alunos com falta  % Presença  \
0  Segunda-feira   Português                29                 1       96.67   
1    Terça-feira  Matemática                25                 5       83.33   
2   Quarta-feira    História                28                 2       93.33   
3   Quinta-feira   Geográfia                24                 7       77.42   
4    Sexta-feira     Quimica                22                 9       70.97   
5         Sábado      Inglês                18                13       58.06   

   % Falta  
0     3.33  
1    16.67  
2     6.67  
3    22.58  
4    29.03  
5    41.94  
Grafico de falta e presenças

import matplotlib.pyplot as plt

curso.plot(x="Matérias", y=["Alunos presentes", "Alunos com falta"], kind="bar", figsize=(10, 6))
plt.title("Comparação de Presença e Falta por Matéria")
plt.ylabel("Número de Alunos")
plt.xlabel("Matérias")
plt.show()


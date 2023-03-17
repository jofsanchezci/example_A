#s_b: salario base
#he: cantidad de horas extras
#b: bonificación 1 si hay bonificación o 0 si no

#Se ingresan los datos
s_b,he,b=input().split()
s_b=float(s_b)
he=int(he)
b=int(b)

#Se hacen las operaciones
vh=s_b/192 #Valor de la hora normal
vhe=vh*1.25 # Valor hora extra
Bon=s_b*0.05 #La bonificación
s_t=(s_b)+(vhe*he)+(Bon*b) #salario total
salario=s_t-((s_t*0.035)+(s_t*0.04)+(s_t*0.01))
#Se impreme el salario
print(round(salario,1))



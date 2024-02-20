'''
Sistema e excutado até digitar "sair" 

Atributos:
string nome_aluno
float percentual_frequencia
float G1
float G2

float media_parcial
float media_final
float exame_final
 
'''

while True:
   nome_auluno = input("Digite o nome do aluno: ")

   percentual_frequencia = float(input("Digite a frequencia do aluno: "))
   nota_g1 = float(input("Digite a nota G1: "))
   nota_g2 = float(input("Digite a nota G2: "))

   media_final = 0

   media_parcial = (nota_g1 + (nota_g2 * 2) ) / 3
   
   if media_parcial <= 6 and percentual_frequencia >=75:
      exame_final = float(input("Digite a nota no exame final: "))

      media_final = (media_parcial + (exame_final * 2) ) / 3

      if media_final >= 6 and percentual_frequencia >= 75:
         print("Aprovado")
   
   elif percentual_frequencia >= 75 and media_parcial >= 6:
        print("Aprovado")

   elif percentual_frequencia <  75 or media_final < 6:
      print("Reprovado")
   
   comando = input("Deseja sair do sistema: ")
   if comando == "sair":
      break;

   

 
      


   

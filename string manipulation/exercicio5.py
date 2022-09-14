string = str(input("digite sua frase: "))
remover_espaço_l = string.lstrip(" ")
remover_espaço_rl = remover_espaço_l.rstrip(" ")

espaços= remover_espaço_rl.count(" ")
tamanho_str = espaços+1


print(f" você digitou {tamanho_str} palavras")

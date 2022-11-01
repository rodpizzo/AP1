from operator import truediv


################################### professor ###########################################


class professor:
    registroFuncional=""
    nome=""
    dataDeNascimento= ""
    sexo=""
    areaDePesquisa=""
    titulação=""
    graduação=""
    email= []
    telefone= []



def listar_elemento_professor(lista_professor):
    if len(lista_professor)==0:
        print("lista vazia")
    else:
        num_registro=input("qual registro deseja listar: ")
        i=buscar_professor(lista_professor,num_registro)
        if i == -1:
            print("Esse registro não existe")
        else:
            imprime_professor(lista_professor[i])
    
def buscar_professor (lista_professores,num_registro):
    existe = False
    saida = - 1
    i=0
    while i<len(lista_professores) and existe == False:
        if lista_professores[i].registroFuncional == num_registro:
            saida = i
            existe=True
        i=i+1
    return saida
    
def inserir_professor(lista_professor):
    p= professor()
    p.registroFuncional=input("Informe o registro funcional: ")
    existe=False
    i=0
    while i<len(lista_professor) and  existe == False:
        while lista_professor[i].registroFuncional == p.registroFuncional:
            print("o codigo ja existe")
            i=0
            p.registroFuncional=input("Informe o registro funcional: ") 
        existe == True  
        i+=1
  
     
    p.nome=input("Informe o nome: ")
    p.dataDeNascimento=input("Informe a data de nascimento: ")
    p.sexo=input("Informe o sexo: ")
    p.areaDePesquisa=input("Informe a area de pesquisa: ")
    p.titulação=input("infomrme o titulo do professor: ")
    p.graduação=input("Informe o tipo de graduação: ")

    p.email=[]
    p.email.append(input("Informe o email: "))
    novo_email = input("deseja informar outro email? (S ou aperte qualquer tecla para continuar)").upper()
    while novo_email=='S': 
        p.email.append(input("digite o email: "))
        novo_email = input("deseja informar outro email? (S ou aperte qualquer tecla para continuar)").upper()
    
    p.telefone=[]
    p.telefone.append(input("Informe o telefone: "))
    novo_tel = input("deseja informar outro telefone? (S ou aperte qualquer tecla para continuar)").upper()
    while novo_tel=='S': 
        p.telefone.append(input("digite o telefone: "))
        novo_tel = input("deseja informar outro telefone? (S ou aperte qualquer tecla para continuar)").upper()

    lista_professor.append(p)
    

def imprime_professor(p):
  print(p.registroFuncional + " | " + p.nome + " | " + p.dataDeNascimento + " | " + p.sexo +" | "+ p.areaDePesquisa+" | "+p.titulação+" | "+ " - ".join(p.email) + " | "+ " - ".join(p.telefone))


def listar_professor(lista_professor):
    if len(lista_professor)==0:
        print("a lista esta vazia")
    else:
        i=0
        while i<len(lista_professor):
            imprime_professor(lista_professor[i])
            i+=1

def excluir_item_professor(lista_professor):
    if len(lista_professor)==0:
        print("a lista esta vazia")
    else:
            num_registro= (input("qual o registro deseja excluir?"))
            i=-1
            while i== -1:
                i=buscar_professor(lista_professor, num_registro)
                if i != -1:
                    break
                print("registro não existe")
                num_registro= (input("qual o registro deseja excluir?"))
            del lista_professor[i]
    
def alterar_item_professor(lista_professor):
        if len(lista_professor)==0:
            print("a lista esta vazia")
        else:
            num_registro= (input("qual o registro deseja alterar?"))
            i=-1
            while i== -1:
                i=buscar_professor(lista_professor, num_registro)
                if i != -1:
                    break
                print("registro não existe")
                num_registro= (input("qual o registro deseja alterar?"))

            lista_professor[i].nome = input("Digite o nome do professor: ")
            lista_professor[i].dataDeNascimento = input("Digite a data de nascimento do professor: ")
            lista_professor[i].sexo =input("Digite o sexo do professor")
            lista_professor[i].areaDePesquisa= input("Digite a area de pesquisa: ")
            lista_professor[i].titulação =input("Digite a titulação do professor: ")
            lista_professor[i].graduação=input("Digite a graduação do professor: ")
            lista_professor[i].email=[]
            lista_professor[i].email.append(input("Informe o email: "))
            

            mail = input("deseja informar outro email? (S ou aperte qualquer tecla para continuar)").upper()
            while mail=='S': 
                lista_professor[i].email.append(input("digite o email: "))
                mail = input("deseja informar outro email? (S ou aperte qualquer tecla para continuar)").upper()
            lista_professor[i].telefone=[]
            lista_professor[i].telefone.append(input("Informe o telefone: "))
            tel= input("deseja informar outro telefone? (S ou aperte qualquer tecla para continuar)").upper()
            while tel=='S': 
                lista_professor[i].telefone.append(input("digite o telefone: "))
                tel= input("deseja informar outro telefone? (S ou aperte qualquer tecla para continuar)").upper()


########################################## disciplina #################################################

class disciplina:
    sigla=""
    nome=""
    ementa=""
    bibliografia=""
    numeroDeCreditos=""
    cargaHoraria=""

def inserir_disciplina(lista_disciplina):
    d= disciplina()
    d.sigla=input("Informe a sigla: ")#nao pode estar duplicado
    existe=False
    i=0
    while i<len(lista_disciplina) and existe == False:
        while lista_disciplina[i].sigla == d.sigla:
            print("a sigla ja existe")
            i=0
            d.sigla=input("Informe a sigla: ") 
        existe == True  
        i+=1    
  
    d.nome=input("Informe o nome: ")
    d.ementa=input("Informe a ementa: ")
    d.bibliografia=input("Informe a bibliografia: ")
    d.numeroDeCreditos=input("Informe o numero de creditos: ")
    d.cargaHoraria=input("Informe a carga horaria: ")
    lista_disciplina.append(d)
    
def imprime_disciplina(d):
    print(d.sigla + " | " + d.nome + " | "+ d.ementa+" | "+d.bibliografia+" | "+d.numeroDeCreditos+" | "+d.cargaHoraria )

def listar_disciplina(lista_disciplina):
    if len(lista_disciplina)==0:
        print("a lista esta vazia")
    else:
       i=0
       while i<len(lista_disciplina):
        imprime_disciplina(lista_disciplina[i])
        i+=1

def buscar_d (lista_disciplina, num_sigla):
    existe = False
    saida = - 1
    i=0
    while i<len(lista_disciplina) and existe == False:
        if lista_disciplina[i].sigla == num_sigla:
            saida = i
            existe=True
        i=i+1
    return saida

def excluir_item_disciplina(lista_disciplina):
    if len(lista_disciplina)==0:
        print("a lista esta vazia")
    else:
        num_sigla= input("qual sigla deseja excluir?")
        i=buscar_d(lista_disciplina, num_sigla)
        del lista_disciplina[i]


def alterar_item_disciplina(lista_disciplina):
        if len(lista_disciplina)==0:
            print("a lista esta vazia")
        else:
            num_sigla= (input("qual sigla deseja alterar?"))
            i=-1
            while i==-1:
                i=buscar_d(lista_disciplina, num_sigla)
                if i!= -1:
                    break
                print("a sigla nao existe")
                num_sigla= (input("qual sigla deseja alterar?"))
            lista_disciplina[i].nome = input("Digite o nome do professor: ")
            lista_disciplina[i].ementa = input("Digite a ementa: ")
            lista_disciplina[i].bibliografia =input("Digite a bibliografia: ")
            lista_disciplina[i].numeroDeCreditos= input("Digite o número de créditos: ")
            lista_disciplina[i].cargaHoraria =input("Digite a carga horaria: ")
                
def listar_elemento_disciplina(lista_disciplina):
    if len(lista_disciplina)==0:
        print("lista vazia")
    else:
        num_sigla= (input("qual sigla deseja alterar?"))
        i=-1
        while i==-1:
                i=buscar_d(lista_disciplina, num_sigla)
                if i!= -1:
                    break
                print("a sigla nao existe")
                num_sigla= (input("qual sigla deseja listar?"))
        imprime_disciplina(lista_disciplina[i])
        
################################################# main ##################################################
def main():
    
        professores=[]
        disciplinas=[]
        opcao='voltarMenu'
        while opcao != '0':
            if opcao == "voltarMenu":
             opcao=menu()
             
             #menu dos professores
            if opcao == '1':
                op=''
                while op != '9':
                   op=submenu()
                   if op=="1":
                        listar_professor(professores)
                   elif op=="2":
                        listar_elemento_professor(professores)
                   elif op=="3":
                        inserir_professor(professores)
                   elif op=="4":
                        alterar_item_professor(professores)

                   elif op=="5":
                        excluir_item_professor(professores)
                else:
                    opcao="voltarMenu"

            #menu das disciplinas
            elif opcao == '2':
                op=''
                while op !='9':
                    op=submenu()
                    if op=="1":
                        listar_disciplina(disciplinas)
                    elif op=="2":
                        listar_elemento_disciplina(disciplinas)
                    elif op=="3":
                        inserir_disciplina(disciplinas)
                    elif op=="4":
                        alterar_item_disciplina(disciplinas)
                    elif op=="5":
                        excluir_item_disciplina(disciplinas)
                   
                else:
                    opcao="voltarMenu"
                    
            elif opcao == '0':
                print("obrigado por usar nosso programa!")
            else:
                print("opção invalida")    

                
def menu():
    print("**********************")
    print("professores..........1")
    print("disciplinas..........2")
    print("Sair.................0")
    opcao = input("-> ")
    return opcao

def submenu():
    print("_________________")
    print("Listar todos.........1") 
    print("listar um elemento...2") 
    print("incluir..............3") 
    print("alterar..............4") 
    print("excluir..............5") 
    print("voltar para o menu...9") 
    op= input("-> ")
    return op

main()
from pprintpp import pprint as pp
from db.database import Graph

class PersonDAO(object):
    def __init__(self):
        self.db = Graph(uri='bolt://44.201.27.203:7687',
                        user='neo4j', password='blankets-rag-symbols')

    def read_by_age(self):
        return self.db.execute_query("MATCH (n:Pessoa) WHERE toInteger(n.idade) > 30 RETURN n.nome")   
    
    def read_by_career(self):
        return self.db.execute_query("MATCH (n:Estudante) RETURN n.idade")
    
    def read_by_race(self):
        return self.db.execute_query("MATCH (p:Pet) RETURN p.nome, p.raça")

    def read_by_relation(self):
        return self.db.execute_query("MATCH (p:Pessoa:Estudante)-[r]->(m:Pessoa:Estudante) WHERE r.desde = 2018 RETURN r")

def divider():
    print('\n' + '-' * 80 + '\n')

dao = PersonDAO()

while True:  
    print('\nO que você deseja saber?\n')  
    option = input('0. Para sair do programa\n1. Quais os nomes das pessoas da família tem mais de 30 anos?\n2. Quais as idades dos estudantes da família? \n3. Qual a raça e nomes dos pets família?\n4. Qual o relacionamento entre Caroliny e Tiago?\n')

    if option == '1':
        aux = dao.read_by_age()
        pp(aux)
        divider()

    elif option == '2':
        aux = dao.read_by_career()
        pp(aux)
        divider()

    elif option == '3':
        aux = dao.read_by_race()
        pp(aux)
        divider()
    
    elif option == '4':
        aux = dao.read_by_relation()
        pp(aux)
        divider()

    elif option == '0':
        break

dao.db.close()

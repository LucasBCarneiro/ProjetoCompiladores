class LexTable:
    def __init__(self, token, lexeme, filepath):
        self.token = token
        self.lexeme = lexeme
        self.filepath = filepath

        self.create_report()
       
    # Retorna o idx do lexeme da tablea de simbolos
    def get_idx_tab(self, lexeme):
        arq_read = open("txts/"+self.filepath.split('/')[-1].replace('.DKS', '.TAB'), 'r')
        
        for line in arq_read:
            if lexeme in line and '@' not in line and 'CODIGO' not in line:
                return line.split(',')[0]
        return " - "

    # Cria o documento do .LEX
    def create_report(self):
        try:
            arq = open(self.filepath.replace('.DKS', '.LEX'), 'w')
        except Exception as e:
            print('Erro ao criar o arquivo .LEX')
            return

        filename = self.filepath.split('/')[-1].split('\\')[-1].replace('.DKS', '')
        arq.write('\n @ CODIGO DA EQUIPE: (EQ10) @\n')
        arq.write('@ LUCAS BRAGA CARNEIRO - lucas.carneiro@ucsal.edu.br - (71) 99350-6564 @\n')
        arq.write('@ JEAN ALVES SILVA - jeanalves.silva@ucsal.edu.br - (71) 99130-6053 @\n')
        arq.write('@ SAMIR DANTAS BARRETO - Samir.barreto@ucsal.edu.br - (71) 98650-0010 @\n')
        arq.write('@ GUSTAVO PEIXOTO DE OLIVEIRA DIAS - gustavo.dias@ucsal.edu.br - (71) 99652-1215 @\n')
        arq.write('\n\n')
        arq.write('\n @ RELATÓRIO DA ANÁLISE LÉXICA. TEXTO FONTE ANALISADO: {} @\n'.format(filename))


        arq.write('Lexeme, Codigo atomo, Indice tabela simbolos\n')

        for idx, item in enumerate(self.token):
            idx_tab = ""

            if 'ID' in self.token[idx]:
                idx_tab = self.get_idx_tab(self.lexeme[idx][:32])
            else:
                idx_tab = " - "
        
            print(self.lexeme[idx], self.token[idx], idx_tab)
            arq.write('{}, {}, {}\n'.format(self.lexeme[idx][:32], self.token[idx], idx_tab))

        print('\n\n\n')
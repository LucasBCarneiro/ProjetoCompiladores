class SymbolTable:
    def __init__(self, token, lexeme, row, filename):
        self.token = token
        self.lexeme = lexeme
        self.row = row
        self.filename = filename

        self.create_report()

    # Cria o documento do .TAB
    def create_report(self):
        obj = {}
        ordered_list = []
        try:
            arq = open(self.filename.replace('.DKS', '.TAB'), 'w')
        except Exception as e:
            print('Erro ao criar o arquivo .TAB')
            return

        count = 0

        for idx, item in enumerate(self.token):
            if 'ID' not in self.token[idx]:
                continue
            
            if self.lexeme[idx] not in obj.keys():
                obj[self.lexeme[idx]] = {
                        'id': count,
                        'lexeme': self.lexeme[idx][:35],
                        'size_before':len(self.lexeme[idx]),
                        'token': self.token[idx],
                        'linhas': [self.row[idx]]

                        }
                count += 1
                ordered_list.append(obj[self.lexeme[idx]])
            else:
                for item in ordered_list:
                    if self.lexeme[idx] == item['lexeme']:
                        item['linhas'].append(self.row[idx])



        arq.write('\n -- CODIGO DA EQUIPE: (EQ10) --\n')
        arq.write('-- LUCAS BRAGA CARNEIRO - lucas.carneiro@ucsal.edu.br - (71) 99350-6564 --\n')
        arq.write('-- JEAN ALVES SILVA - jeanalves.silva@ucsal.edu.br - (71) 99130-6053 --\n')
        arq.write('-- SAMIR DANTAS BARRETO - Samir.barreto@ucsal.edu.br - (71) 98650-0010 --\n')
        arq.write('-- GUSTAVO PEIXOTO DE OLIVEIRA DIAS - gustavo.dias@ucsal.edu.br - (71) 99652-1215 --\n')
        arq.write('\n\n')

        arq.write('id, lexeme, token, qnt_antes, qnt_dps, tipo, linhas\n')
        for item in ordered_list:
            print("{:<8} {:<15} {:<10}".format(item['lexeme'], item['token'], ''.join(str(item['linhas']))))
            aux = ''
            if item['token'] == 'ID03':
                aux = 'INT'
            elif item['token'] == 'ID06':
                aux = 'FLOAT'
            else:
                aux = 'VOID'
            arq.write('{}, {}, {}, {}, {}, {}, {}\n'.format(item['id'], item['lexeme'], item['token'], item['size_before'], len(item['lexeme']), aux, item['linhas']))

        print('\n\n\n')


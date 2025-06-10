from utils import remove_comments
import os

class Buffer:
    def __init__(self, filename):
        self.filename = filename

    def load_buffer(self):
        try:
            arq = open(self.filename, 'r')
            text = remove_comments(arq.read())
            arq.close()

            arq2 = open(os.path.abspath(os.getcwd())+'/txts/aux.DKS', 'w')
            arq2.write(text)
            arq2.close()

            arq3 = open(os.path.abspath(os.getcwd())+'/txts/aux.DKS', 'r')
        except Exception as e:
            print("Erro ao abrir arquivo: {}".format(str(e)))
            return

        text = arq3.readline()

        buffer = []
        cont = 1

        # O tamanho do buffer pode ser mudado ao mudar o "cont"
        while text != "":
            buffer.append(text)
            text = arq3.readline()
            cont += 1

            if cont == 10 or text == '':
                # Retorna um buffer completo
                buf = ''.join(buffer)
                cont = 1
                yield buf

                # Reseta o buffer
                buffer = []

        arq3.close()

import pandas as pd


class Word2VecUtilPortuguese:

    def __init__(self, path):
        self.dataclas = pd.read_csv(path);
        self.dataclas.set_index('nome', inplace=True)
        print(self.dataclas.shape[0])
        print(self.dataclas.shape[1])
        self.vecSize = self.dataclas.shape[1]

    def wordtodense(self, word):
        try:
            v = self.dataclas.loc[word]
            vect = v.values
            return vect
        except:
            return []

        # \xc3\xa1

        # receve a texte and rreturn a list of words

    def tokenization(self, texto):
        texto = texto.lower()

        texto = texto.replace('\t', ' ')
        texto = texto.replace(',', ' , ')
        texto = texto.replace('"', ' ')
        texto = texto.replace("'", ' ')
        texto = texto.replace(';', ' ; ')
        texto = texto.replace(':', ' ; ')
        texto = texto.replace('!', ' ! ')
        texto = texto.replace('?', ' ? ')
        texto = texto.replace('/', ' ')
        texto = texto.replace('(', ' ')
        texto = texto.replace('-', ' ')

        texto = texto.replace(')', ' ')
        texto = texto.replace('.', ' . ')
        texto = texto.replace('  ', ' ')

        palavras_tokenize = texto.split(' ')
        return palavras_tokenize;

    def wordsToDense(self, nomes):
        import numpy as np
        result = np.array([])
        for nm in nomes:
            # nm = nm + ' '
            valor = self.wordtodense(nm)

            if len(valor) == 50:
                result = np.concatenate((result, valor), axis=0)

        return result;

    def textToDense(self, texto):
        npalavreas = self.tokenization(texto)
        valoresv = self.wordsToDense(npalavreas)
        return valoresv

    def textToDenseFixesize(self, texto, fixedsize):
        import numpy as np
        vector = self.textToDense(texto)
        size = vector.shape[0]
        if size < fixedsize:
            zeros = np.zeros(fixedsize - size)
            vector = np.concatenate((vector, zeros), axis=0)
        elif size > fixedsize:
            vector = vector[0:fixedsize]
        return vector


def teste():
    path = '/home/desenvolvimento/python/NLP/dicionario_vec50.csv'
    wordVecDicionario = Word2VecUtilPortuguese(path)

    vec = wordVecDicionario.textToDenseFixesize("oi maria", 100 )


    print(vec)



#teste()




















import pandas as pd


class CsvProcessor:
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo
        self.df = None
        self.df_filtrado = None


    def carregar_csv(self):
        self.df = pd.read_csv(self.caminho_arquivo)
        return self.df 
    

    def filtrar_csv(self, coluna, atributo):
        self.df_filtrado = self.df[self.df[coluna] == atributo]
        return self.df_filtrado
    

    def sub_filtro_csv(self, coluna, atributo):
        return self.df_filtrado[self.df[coluna] == atributo]




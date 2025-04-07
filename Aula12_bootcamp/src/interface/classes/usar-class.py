from csv_class import CsvProcessor

arquivo_csv = './exemplo.csv'
coluna = 'estado'
atributo  = 'SP'

novo_filtro = 'preço'
atributo_2 = "99,99"

processar_csv = CsvProcessor(arquivo_csv)
processar_csv.carregar_csv()
print(processar_csv.filtrar_csv(coluna, atributo))
print('-'*35)
print(processar_csv.sub_filtro_csv(novo_filtro, atributo_2))


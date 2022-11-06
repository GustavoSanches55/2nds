import numpy as np
import pandas as pd
import networkx as nx
import sqlite3
from pyvis.network import Network

import random

palavras = ['prova', 'seminario', 'dificuldade', 'facilidade', "none", "none", "none"]
palavras_mais_usadas = []
for i in range(192):
    palavras_mais_usadas.append(random.choice(palavras))


class Graph:
    def __init__(self, bgcolor="#FFFFFF"):
        self.net = Network(height="100%", width="100%", bgcolor=bgcolor)
        self.darkcolor = "#222725"

        self.subject_nodes = []
        self.teatcher_nodes = []
        self.avaliation_nodes = []
        self.group_nodes = []

    def add_subject_nodes(self, dataframe, index_column, titlecolumn,subject_color="#222725", subject_size=10):
        # create a vector of colors and other for sizes
        sizes = [subject_size for i in range(dataframe.shape[0])]
        colors = [subject_color for i in range(dataframe.shape[0])]
        self.subject_nodes = dataframe[index_column].to_list()
        self.net.add_nodes(dataframe[index_column].to_list(), color=colors, size=sizes, title=dataframe[titlecolumn].to_list())

    def add_teatcher_nodes(self, dataframe, index_column, teatcher_color="#222725", teatcher_size=10):
        dataframe['size_teatcher'] = teatcher_size
        dataframe['color_teatcher'] = teatcher_color
        self.teatcher_nodes = dataframe[index_column].to_list()
        self.net.add_nodes(dataframe[index_column].to_list(), color=dataframe['color_teatcher'].to_list(), size=dataframe['size_teatcher'].to_list())
    
    def add_avaliation_nodes(self, dataframe, index_column, color_column, value_column, label_column, title_column):
        self.avaliation_nodes = dataframe[index_column].to_list()
        labels = [" " for i in range(len(self.avaliation_nodes))]
        self.net.add_nodes(dataframe[index_column].to_list(),
                            color=dataframe[color_column].to_list(), 
                            value=dataframe[value_column].to_list(), 
                            label=labels, 
                            title=dataframe[label_column].to_list())

    def add_word_nodes(self, vocabulary):
        for i in vocabulary:
            if i != 'none':
                self.net.add_node(i, color='#FFFFFF', size=20)

    def add_group_nodes(self, iterable1, iterable2):
        for i in list(iterable1):
            for j in list(iterable2):
                self.net.add_node(str(i) + '-' + str(j), size=0, label=' ')
                self.group_nodes.append([str(i), str(j)])

    def add_group_edges(self, dataframe):
        for i in range(dataframe.shape[0]):
            carater =  dataframe['carater'].iloc[i]
            self.net.add_edge(int(dataframe['id'].iloc[i]), carater+'-'+dataframe['nome_assunto'].iloc[i], length=5, color='#FFFFFF')

    def add_avaliation_subject_edges(self, dataframe):
        vertices = list(zip(dataframe["id"], dataframe["nome_assunto"]))
        # dataframe['vertices_avaliacao_assunto'] = list(zip(dataframe["id"], dataframe["nome_assunto"]))
        for vertice in vertices:
            self.net.add_edge(vertice[0], vertice[1])

    def add_subject_teatcher_edges(self, dataframe):
        # dataframe['vertices_assunto_professor'] = list(zip(dataframe["nome_assunto"], dataframe["nome_professor"]))
        vertices = list(zip(dataframe["nome_assunto"], dataframe["nome_professor"]))
        for vertice in vertices:
            self.net.add_edge(vertice[0], vertice[1])

    def add_avaliation_word_edges(self, dataframe):
        # dataframe['vertices_avaliacao_palavra'] = list(zip(dataframe["id"], dataframe["palavras_mais_usadas"]))
        vertices = list(zip(dataframe["id"], dataframe["palavras_mais_usadas"]))
        for vertice in vertices:
            if vertice[1] != 'none':
                self.net.add_edge(vertice[0], vertice[1], lenght=1000)

    def show_graph(self, name):
        self.net.show(name)

    def save_graph(self, name):
        self.net.save_graph(name)

colors = {"disposto-bom": '#F7E967', 'disposto-ruim': '#F1433F', 'indisposto-bom': '#A9CF54', 'indisposto-ruim': '#70B7BA'}

conn = sqlite3.connect('D:\\1 - FGV\\2nds_versao_att\\silvia\\db.sqlite3')
cursor = conn.cursor()

disciplina = pd.read_sql_query('select * from base_disciplina', conn)
assunto = pd.read_sql_query('select * from base_assunto', conn)
avaliacao = pd.read_sql_query('select * from base_avaliacao', conn)
sentimento = pd.read_sql_query('select * from base_sentimentos', conn)
professor = pd.read_sql_query('select * from base_professor', conn)

df_disciplina_assunto = pd.merge(disciplina, assunto, how="left", left_on='id_assunto_id', right_on='id', suffixes=('_disciplina', '_assunto'))
df_disciplina_assunto = pd.merge(df_disciplina_assunto, professor, how="left", left_on='id_professor_id', right_on='id', suffixes=('_disciplina_assunto', '_professor'))

df_final = pd.merge(avaliacao, sentimento, left_on='id_sentimento_id', right_on='id', how='left', suffixes=('', '_sentimento'))
df_final = pd.merge(df_final, disciplina, left_on='id_disciplina_id', right_on='id', how='left', suffixes=('', '_disciplina'))

df_final = pd.merge(df_final, professor, left_on='id_professor_id', right_on='id', how='left', suffixes=('', '_professor'))
df_final = pd.merge(df_final, assunto, left_on='id_assunto_id', right_on='id', how='left', suffixes=('', '_assunto'))
df_final['palavras_mais_usadas'] = palavras_mais_usadas
df_final['color'] = df_final['carater'].map(colors)


df_final['palavras_mais_usadas'] = palavras_mais_usadas
df_final['color'] = df_final['carater'].map(colors)


def create_teacher_graph(df_final, df_disciplina_assunto, teacher_id):
    grafo = Graph()

    df_final = df_final.loc[df_final['id_professor_id'] == teacher_id]
    df_disciplina_assunto = df_disciplina_assunto.loc[df_disciplina_assunto['id_professor_id'] == teacher_id]

    grafo.add_word_nodes(vocabulary=set(palavras_mais_usadas))
    grafo.add_subject_nodes(dataframe=df_disciplina_assunto, index_column='nome_assunto', titlecolumn='nome_professor')
    # grafo.add_teatcher_nodes(dataframe=professor, index_column='nome_professor')
    grafo.add_avaliation_nodes(dataframe=df_final, index_column='id', color_column='color', value_column='intensidade', label_column='nome_sentimentos', title_column='nome_professor')
    grafo.add_group_nodes(colors, df_disciplina_assunto['nome_assunto'])
    grafo.add_group_edges(dataframe=df_final)
    grafo.add_avaliation_subject_edges(dataframe=df_final)
    # grafo.add_subject_teatcher_edges(dataframe=df_final)
    grafo.add_avaliation_word_edges(dataframe=df_final)

    grafo.save_graph("generated_graphs/grafo_professor_" + str(teacher_id) + ".html")

def create_general_graph(df_final, df_disciplina_assunto):
    grafo = Graph()

    # df_final = df_final.loc[df_final['id_professor_id'] == teacher_id]
    # df_disciplina_assunto = df_disciplina_assunto.loc[df_disciplina_assunto['id_professor_id'] == teacher_id]

    # grafo.add_word_nodes(vocabulary=set(palavras_mais_usadas))
    grafo.add_subject_nodes(dataframe=df_disciplina_assunto, index_column='nome_assunto', titlecolumn='nome_professor')
    grafo.add_teatcher_nodes(dataframe=professor, index_column='nome_professor')
    grafo.add_avaliation_nodes(dataframe=df_final, index_column='id', color_column='color', value_column='intensidade', label_column='nome_sentimentos', title_column='nome_professor')
    grafo.add_group_nodes(colors, df_disciplina_assunto['nome_assunto'])
    grafo.add_group_edges(dataframe=df_final)
    grafo.add_avaliation_subject_edges(dataframe=df_final)
    grafo.add_subject_teatcher_edges(dataframe=df_final)
    # grafo.add_avaliation_word_edges(dataframe=df_final)

    grafo.save_graph("generated_graphs/general_graph.html")


for teacher_id in df_final.id_professor_id.unique():
    create_teacher_graph(df_final, df_disciplina_assunto, teacher_id)

create_general_graph(df_final, df_disciplina_assunto)

# close cursor
cursor.close()
# close connection
conn.close()
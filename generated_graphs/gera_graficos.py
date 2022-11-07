import altair as alt
import pandas as pd
import sqlite3


def query(id_disciplina, id_professor):
    q = f"""
    SELECT
        a.id AS id_avaliacao, 
        s.carater , 
        a.intensidade, 
        d.id AS id_disciplina,
        p.id AS id_professor,
        p.nome_professor,
        assunto.id AS id_assunto,
        assunto.nome_assunto,
        t.id AS id_turma,
        t.curso,
        t.periodo,
        t.tag,
        a.data,
        a.conhecimento

    FROM base_avaliacao AS a
    INNER JOIN base_sentimentos AS s
    ON a.id_sentimento_id = s.id

    INNER JOIN base_disciplina as d
    ON a.id_disciplina_id = d.id

    INNER JOIN base_professor as p
    ON d.id_professor_id = p.id

    INNER JOIN base_assunto AS assunto
    ON d.id_assunto_id = assunto.id

    INNER JOIN base_turma AS t
    ON d.id_turma_id = t.id

    WHERE d.id={id_disciplina} 
            AND p.id={id_professor}
    ;
    """
    return q


def grafico_barras(id_disciplina, id_professor):
    conn = sqlite3.connect('..\\silvia\\db.sqlite3')
    cur = conn.cursor()
    q = query(id_disciplina, id_professor)
    grafico_barras = pd.read_sql_query(q, conn)

    colors = {"disposto-bom": '#A9CF54', 'disposto-ruim': '#F1433F',
              'indisposto-bom': '#F7E967', 'indisposto-ruim': '#70B7BA'}
    grafico_barras['color'] = grafico_barras['carater'].map(colors)

    bar_graph = alt.Chart(grafico_barras.groupby(['color', 'carater']).sum().reset_index()).mark_bar().encode(
        alt.X('carater:N', sort='y'),
        alt.Y('intensidade:Q'),
        color=alt.Color('color:N', scale=None)
    ).properties(
        width=alt.Step(80)
    )

    bar_graph.save('grafico_barras.html', embed_options={'renderer': 'svg'})
    conn.close()


def avaliacao_tempo(id_disciplina, id_professor):
    conn = sqlite3.connect('../silvia/db.sqlite3')
    cur = conn.cursor()

    q = query(id_disciplina, id_professor)
    grafico_linhas = pd.read_sql_query(q, conn)

    for i in range(len(grafico_linhas)):
        if ('ruim' in grafico_linhas['carater'].loc[i]):
            grafico_linhas['intensidade'].loc[i] = (
                grafico_linhas['intensidade'].loc[i])*-1

    grafico_linhas['data'] = pd.to_datetime(
        grafico_linhas['data'], format='%d/%m/%Y')

    colors = {"disposto-bom": '#A9CF54', 'disposto-ruim': '#F1433F',
              'indisposto-bom': '#F7E967', 'indisposto-ruim': '#70B7BA'}
    grafico_barras['color'] = grafico_barras['carater'].map(colors)

    a_tempo = alt.Chart(grafico_linhas.groupby(['data']).mean().reset_index()).mark_bar().encode(
        alt.X('data:T', title='Data', axis=alt.Axis(format='%d/%m/%Y')),
        alt.Y('intensidade:Q'),
        color=alt.condition(
            alt.datum.intensidade > 0,
            alt.value('#A9CF54'),
            alt.value('#F1433F')
        )
    )

    a_tempo.save('avaliacao_tempo.html', embed_options={'renderer': 'svg'})
    conn.close()


def histograma(id_disciplina, id_professor):
    conn = sqlite3.connect('..\silvia\db.sqlite3')
    cur = conn.cursor()

    q = query(id_disciplina, id_professor)
    histograma = pd.read_sql_query(q, conn)

    histogram = alt.Chart(histograma, width=500, height=350).transform_joinaggregate(
        total='count(*)'
    ).transform_calculate(
        pct='1 / datum.total'
    ).mark_bar().encode(
        alt.X('conhecimento:Q', bin=True, title='Conhecimento categorizado'),
        alt.Y('sum(pct):Q', axis=alt.Axis(format='%'), title='porcentagem'),
    ).configure_bar(
        color='#70B7BA'
    )

    histogram.save('histograma.html', embed_options={'renderer': 'svg'})
    print('fim')
    conn.close()

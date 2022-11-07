# **SILVIA**

## **S**entiment **I**nsights in **L**earning **V**isualized through **I**ntuitive **A**nalysis

## Protótipo
https://lucastreuke.github.io/Silvia2ndPrototype


Quando se pensa em como melhorar o processo de ensino e aprendizagem, nesse caso com ciência de dados, a primeira coisa que vem a mente é desenvolver uma ferramenta que facilite ou a coleta de informações ou a sumarização das mesmas. Porém, essas soluções falham em tratar de problemas emocionais e de comunicação em sala de aula. 

A **SILVIA** é um mecanismo de feedback dos alunos, tanto para instituição de ensino quanto para o professor, de forma humanizada. A humanização do processo se dá ao afastar-se de perguntas que quantifiquem diretamente o descontentamento com a matéria.

Buscamos melhorar a comunicação professor-aluno no dia-a-dia. Para dessa forma evitar sobrecarga emocional e, consequentemente, déficits no aprendizado. Além de fornecer uma ferramenta de apoio à decisão no momento de escolher instrumentos avaliativos, provas etc.

Um exemplo claro da problemática, se dá no quarto período do curso de Matemática aplicada da FGV - EMAp. Esse período específicamente possuí duas matérias, Análise Real e Inferência Estatística, que exigem muito do alunos e são conhecidas pela dificuldade, gerando um stress exoberante nos alunos. Com o uso da **SILVIA**, os professores podem ter acesso a uma visualização dos sentimentos e pensamentos dos alunos e analisar o perfil da turma. Eventualmente, seria possível achar padrões e adptar o método de ensino.

Perguntas como: "De um a cinco, quanto você acha que esse professor busca ajudar os alunos?", podem, em algum nível, parecer uma crítica pessoal ao professor. Nosso objetivo não é criar uma avaliação para a matéria nem para o professor, muito menos classificá-la como boa ou ruim. Nesse campo de avaliação, não existem categorias claras para "encaixar" uma aula. Por esse motivos, o que é feito é coletar como os alunos se sentem ao longo de todo o período das aulas. Ao cruzar esses sentimentos com palavras chaves como "prova", "seminário" e "dificuldade" podemos efetivamente melhorar a comunicação em sala de aula de forma empática.

### Como resolver a problemática?

A idéia é de tempo em tempo possibilitar o feedback de certas matérias, aos poucos e continuamente. Em um dia, os alunos avaliam como se sentem em relação a quatro ou cinco matérias, e em outro mais algumas. Manter o número de feedbacks por período de tempo baixo ajuda a não cansar os usuários com formulários. Além disso, todo o processo deve ser rápido e consiso, durando no máximo 10 minutos para todos os feedbacks do dia.

Para tal, desenvolvemos uma tela inicial do usuário aluno simples.

![tela inicial aplicativo](imagens_relatorio\tela_inicial.png)

Os sentimentos possíveis são codificados em quatro categorias diferentes, identificados fortemente por sua cor.

>   ## Sentimentos:
>   
>   **Indisposto bom**
>   Calma, confiança, esperança, satisfacao
>   
>   **Indisposto ruim**
>   Medo,  tédio, tristeza, cansaço
>   
>   **Disposto bom**
>   Empolgação, otimismo, interesse, alegria 
>
>   **Disposto ruim**
>   Indignacão, raiva, estresse, ansiedade
>
>   *disclaimer:* o termo disposto e indisposto estão sendo empregados no sentido de estar agitado/ativo e tranquilo/passivo respectivamente.

Os dados coletados nessa etapa são:

-   Matéria
-   Sentimento (str)
-   Intensidade (int)
-   Conhecimento na matéria (int)
-   Comentário (text, podendo ser vazio)

Todas as respostas vão parar em um banco Sqlite3. Por meio do Django. Uma vez tendo os dados coletados, podemos gerar análilses diversas.

Vale resaltar nesse ponto que professores apenas poderão visualizar dados de suas matérias. Gráficos/Grafos mais amplos estarão disponíveis apenas para a instuição.

### Grafos

A escolha de visualização através de grafos visa explicitar a relação entre entidades e dar um feedback visual através das cores das avaliações.

Uma vez que o leitor do grafo associa a cor aos sentimentos, basta olhar para um nó de alguma matéria e averiguar se existem mais nós de um cor em volta dele ou não.

**Grafo geral da instituição**:



O grafo geral tem por objetivo dar um overview de como as matérias dadas pelos professores estão sendo recebidas pelos alunos. 

Observando apenas essa visualização conseguimos ter uma noção geral do decorrer das disciplinas. 


![Grafo geral](https://github.com/GustavoSanches55/2nds/blob/main/imagens_relatorio/grafo_geral.jpg)

Entretanto, o verdadeiro valor do Grafo Geral se dá ao combiná-lo com filtros e o grafo a seguir.

![Grafo professor](imagens_relatorio\grafo_professor.jpg)

O grafo acima é especializado para um professor em específico. Nesse exemplo, o professor de geografia. Através dele é possível notar a satisfação geral da turma e relacionar com palavras chaves.

*nota:* as palavras chaves são retiradas dos comentários, dessa maneira nem toda avaliação terá palavras chaves (trabalho em progresso)

para o caso da matéria de geografia, nota-se um número grande de avaliações do tipo "disposto-bom" e com alta intensidade (tamanho do vértice). Também, percebe-se a relação desses sentimentos com a facilidade da matéria.

Apartir dessas análises, é possível tomar duas principais conclusões:

>   "A matéria está em um bom nível de dificuldade, os alunos estão aprendendo e curtindo o processo ao mesmo tempo" 

e

>   "A matéria está fácil de mais, existe margem para dificultá-la e ensinar mais conteúdo"

A escolha irá depender única e exclusivamete do professor. Caso decida mudar, poderá continuar acompanhando a satisfação da turma, voltar atrás da decisão ou não. Dando autonomia total e aumentando a quantidade de informação que o professor tem.

Acreditamos que a escolha do grafo para representar essas informações se tornou ideal, devido ao fato de (nesse caso) ser simplificada para leitura do público leigo. E outro ponto positivo é que segue o mantra de Ben Shneiderman.

>   "Overview first, zoom and filter, then details-on-demand
Overview first, zoom and filter, then details-on-demand
Overview first, zoom and filter, then details-on-demand
Overview first, zoom and filter, then details-on-demand " 

Criando um caminho claro: primeiro observa o grafo geral e nota disparidades (matérias com muitos sentimentos do mesmo tipo, por exemplo), em sequência, filtra e adiciona detalhes, a fim de auxiliar na tomada de decisão.

### Gráficos

Além de toda a informação dada pelos gráfos, também existirá uma auxílio por gráficos. Estes sendo o seguinte:

- Um gráfico de histograma que mostra a porcentagem de alunos em cada categoria de conhecimento. Permite cruzar o conhecimento com a satisfação.

![Histograma](imagens_relatorio\histograma.jpg)


-   Um gráfico de barras para mostrar a quantidade de avaliações em cada categoria de sentimento.

![gráfico de barras](imagens_relatorio\grafico_barras.jpg)

-   Uma análise temporal do sentimentos,  onde são caluladas as médias diáriass dos feedbacks boas e ruins.

![analise de tempo](imagens_relatorio\analise_tempo.jpg)


### Modelagem do banco de dados

Modelamos um banco de dados focado na avaliação, imagem a seguir:

![Banco](imagens_relatorio\banco.png)

*nota*: os nomes de algumas entidades como disciplina são um pouco abstratos. Não se apegue a eles para a compreensão geral do banco.

### Conclusão

Dento tudo isso dito, é de suma importância manter a saúde mental em dia com objetivo de render e aprender mais. E para tal, o professor tem um papel chave em não sobrecarregar físicamente e mentalmente os alunos.

Acreditamos fielmente que a **SILVIA** tem a capacidade de melhorar o intermédio de aluno-professor, tornando o professor mais consciente de suas decisões e de suas consequências, e tornar o ensino melhor através de visualização e coleta de dados continua.

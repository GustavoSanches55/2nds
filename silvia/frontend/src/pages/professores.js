import React from 'react'

const Professores = () => {
    const updateInsights = event => {
        console.log("update")
    }

    return (
<div>
    <div class="header">
        <div class="logo"></div>
        <div class="scroll-nav"></div>
    </div>
    <div class="content snap">
        <section data-page="1" class="insight">
            <h1>Professores</h1>
            
            <div class="greetings">
                <p>
                    Bem vindo ao seu dashboard personalizado.
                </p>
                <p>
                    Desça pelas telas para ver insights sobre como seus alunos estão se saindo na disciplina escolhida.
                </p>
                <label for="disciplina">Escolha a disciplina:</label>
                <select name="disciplina" id="input_disciplina">
                    <option value="matemática|1|B"><span class="assunto">Matemática</span> <span class="periodo">1</span> <span class="tag">B</span></option>
                    <option value="matemática|1|B"><span class="assunto">Matemática</span> <span class="periodo">3</span> <span class="tag">A</span></option>
                    <option value="matemática|1|B"><span class="assunto">Ciências</span> <span class="periodo">1</span> <span class="tag">A</span></option>
                </select>
            </div>
            <div class="insight-status">
                <p id="up-to-date-feedback">
                    Seus insights estão atualizados.
                </p>
                <button id="update_insights" onClick={updateInsights}>
                    <span class="material-symbols-outlined">update</span>
                    Atualizar Insights
                </button>
            </div>

            <div class="scroll-down-tip">Arrasta pra cima!</div>
        </section>
        <section data-page="2" class="insight">

        </section>
        <section data-page="3" class="insight">

        </section>
        <section data-page="4" class="insight">

        </section>
    </div>
    <div class="footer">
        <a href="home" class="home">
            <span class="material-symbols-outlined">
            home
            </span></a>
        <a href="graph" class="graph">
            <span class="material-symbols-outlined">
            hub
            </span></a>
        <a href="menu" class="menu">
            <span class="material-symbols-outlined">
            density_medium
            </span></a>
    </div>
</div>
    )
}

export default Professores

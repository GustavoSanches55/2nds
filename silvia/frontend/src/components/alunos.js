import React from 'react'

const Alunos = () => {
  return (
<body>
    <div class="content">
        <h1>Avaliações</h1>
        <form action="">
            <label for="materia">escolha a disciplina:</label>
            <select name="materia" id="input_materia">
                <option value="none">Toque para opções</option>
            </select>
            <label for="conhecimento">conhecimento na matéria:</label>
            <div class="slider-container">
                | | | | | |
                <span> </span>
                <div class="ends"></div>
                <input type="range" name="conhecimento" id="input_conhecimento" min="0" max="10" value="5" step="1" class="slider"></input>
            </div>
            <label for="sentimento">escolha a categoria de sentimento:</label>
            <h2>sentimentos</h2>
            <input type="hidden" name="sentimento" id="input_sentimento"></input>
            <div class="sentimentBox">
                <div class="box1">
                    <h3 class="sentimentKind">Indisposto+Bom</h3>
                    <div class="box1">
                        <p class="sentiment">Sentimento 1</p>
                    </div>
                    <div class="box2">
                        <p class="sentiment">Sentimento 2</p>
                    </div>
                    <div class="box3">
                        <p class="sentiment">Sentimento 3</p>
                    </div>
                    <div class="box4">
                        <p class="sentiment">Sentimento 4</p>
                    </div>
                </div>
                <div class="box2">
                    <h3 class="sentimentKind">Disposto+Bom</h3>
                    <div class="box1">
                        <p class="sentiment">Sentimento 1</p>
                    </div>
                    <div class="box2">
                        <p class="sentiment">Sentimento 2</p>
                    </div>
                    <div class="box3">
                        <p class="sentiment">Sentimento 3</p>
                    </div>
                    <div class="box4">
                        <p class="sentiment">Sentimento 4</p>
                    </div>
                </div>
                <div class="box3">
                    <h3 class="sentimentKind">Indisposto+Ruim</h3>
                    <div class="box1">
                        <p class="sentiment">Sentimento 1</p>
                    </div>
                    <div class="box2">
                        <p class="sentiment">Sentimento 2</p>
                    </div>
                    <div class="box3">
                        <p class="sentiment">Sentimento 3</p>
                    </div>
                    <div class="box4">
                        <p class="sentiment">Sentimento 4</p>
                    </div>
                </div>
                <div class="box4">
                    <h3 class="sentimentKind">Disposto+Ruim</h3>
                    <div class="box1">
                        <p class="sentiment">Sentimento 1</p>
                    </div>
                    <div class="box2">
                        <p class="sentiment">Sentimento 2</p>
                    </div>
                    <div class="box3">
                        <p class="sentiment">Sentimento 3</p>
                    </div>
                    <div class="box4">
                        <p class="sentiment">Sentimento 4</p>
                    </div>
                </div>
            </div>
            <label for="comentario">por que você se sente dessa forma sobre a matéria?</label>
            <textarea name="comentario" id="input_comentario" cols="40" rows="8"></textarea>
            <button type="submit">enviar</button>
        </form>
    </div>
    <div class="footer">
        <button class="home">🏠</button>
        <button class="mySentiments">❤</button>
        <button class="menu">📝</button>
    </div>

</body>
  )
}

export default Alunos
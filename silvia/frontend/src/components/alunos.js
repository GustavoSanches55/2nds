import React from 'react'




















const Alunos = () => {
    const handleCategoryClick = event => {
        document.getElementsByClassName("sentimentBox")[0].classList.add("category-selected");
        event.currentTarget.classList.add("selected");
        setTimeout(function(e){
            e.classList.add("avaliable");
        }, 140, event.currentTarget);
    }

    const handleSentimentClick = event => {
        if (event.currentTarget.parentElement.classList.contains("avaliable")){
            event.currentTarget.classList.add("selected");
            document.getElementsByClassName("sentimentBox")[0].classList.add("sentiment-selected");
            document.getElementById("input_sentimento").value = event.currentTarget.getElementsByClassName("sentiment")[0].innerHTML;
            let color = getComputedStyle(event.currentTarget).getPropertyValue("--background-color")
            document.getElementById("submit").style.setProperty("--background-color", color);
            document.getElementById("submit").classList.add("sentiment-selected");
            setTimeout(function(e){
                document.getElementById("input_intensidade").parentElement.classList.add("shadow-filter");
            }, 140, event.currentTarget);
        }
    }

  return (
<div>
<div class="content">
        <h1>Avaliações</h1>
        <form action="">
            <label for="materia">escolha a disciplina:</label>
            <select name="materia" id="input_materia">
                <option value="matematica">Matemática</option>
                <option value="portugues">Português</option>
                <option value="historia">História</option>
                <option value="geografia">Geografia</option>
            </select>
            <label for="conhecimento">conhecimento na matéria:</label>
            <div class="slider-container">
                | | | | | |
                <span> </span>
                <div class="ends"></div>
                <input type="range" name="conhecimento" id="input_conhecimento" min="0" max="10" default="5" step="1" class="slider"></input>
            </div>
            <label for="sentimento">escolha a categoria de sentimento:</label>
            <h2>sentimentos</h2>
            <input type="hidden" name="sentimento" id="input_sentimento"></input>
            <div class="sentimentBox">
                <div onClick={handleCategoryClick} class="category box1">
                    <h3 class="sentimentKind">Indisposto Bom</h3>
                    <div onClick={handleSentimentClick} class="box1">
                        <p class="sentiment">Sentimento 1</p>
                    </div>
                    <div onClick={handleSentimentClick} class="box2">
                        <p class="sentiment">Sentimento 2</p>
                    </div>
                    <div onClick={handleSentimentClick} class="box3">
                        <p class="sentiment">Sentimento 3</p>
                    </div>
                    <div onClick={handleSentimentClick} class="box4">
                        <p class="sentiment">Sentimento 4</p>
                    </div>
                </div>
                <div onClick={handleCategoryClick} class="category box2">
                    <h3 class="sentimentKind">Disposto Bom</h3>
                    <div onClick={handleSentimentClick} class="box1">
                        <p class="sentiment">Sentimento 1</p>
                    </div>
                    <div onClick={handleSentimentClick} class="box2">
                        <p class="sentiment">Sentimento 2</p>
                    </div>
                    <div onClick={handleSentimentClick} class="box3">
                        <p class="sentiment">Sentimento 3</p>
                    </div>
                    <div onClick={handleSentimentClick} class="box4">
                        <p class="sentiment">Sentimento 4</p>
                    </div>
                </div>
                <div onClick={handleCategoryClick} class="category box3">
                    <h3 class="sentimentKind">Indisposto Ruim</h3>
                    <div onClick={handleSentimentClick} class="box1">
                        <p class="sentiment">Sentimento 1</p>
                    </div>
                    <div onClick={handleSentimentClick} class="box2">
                        <p class="sentiment">Sentimento 2</p>
                    </div>
                    <div onClick={handleSentimentClick} class="box3">
                        <p class="sentiment">Sentimento 3</p>
                    </div>
                    <div onClick={handleSentimentClick} class="box4">
                        <p class="sentiment">Sentimento 4</p>
                    </div>
                </div>
                <div onClick={handleCategoryClick} class="category box4">
                    <h3 class="sentimentKind">Disposto Ruim</h3>
                    <div onClick={handleSentimentClick} class="box1">
                        <p class="sentiment">Sentimento 1</p>
                    </div>
                    <div onClick={handleSentimentClick} class="box2">
                        <p class="sentiment">Sentimento 2</p>
                    </div>
                    <div onClick={handleSentimentClick} class="box3">
                        <p class="sentiment">Sentimento 3</p>
                    </div>
                    <div onClick={handleSentimentClick} class="box4">
                        <p class="sentiment">Sentimento 4</p>
                    </div>
                </div>
                <label for="intensidade">Qual é a intensidade do seu sentimento?</label>
                <div class="slider-container">
                    | | | | |
                    <span> </span>
                    <div class="ends"></div>
                    <input type="range" name="intensidade" id="input_intensidade" min="1" max="5" default="3" step="1" class="slider"></input>
                </div>
            </div>
            
            <label for="comentario">por que você se sente dessa forma sobre a matéria?</label>
            <textarea name="comentario" id="input_comentario" cols="40" rows="8"></textarea>
            <button id="submit" type="submit">enviar</button>
        </form>
    </div>
    <div class="footer">
        <a href="home" class="home"><span class="material-symbols-outlined">
            home
            </span></a>
        <a href="sentimentos" class="mySentiments"><span class="material-symbols-outlined">
            favorite
            </span></a>
        <a href="menu" class="menu"><span class="material-symbols-outlined">
            density_medium
            </span></a>
    </div>
</div>
  )
}

export default Alunos
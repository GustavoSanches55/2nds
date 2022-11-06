import React from "react";
import axios from "axios";


const Base = () => {
    let API_URL = "http://localhost:8000/listarAlunos";

    const getStudents = () => {
        axios.get(API_URL).then(res => document.getElementById('vasco').innerHTML = res.data);
    }
    return (
        <div>
            <h1>Index</h1>
            <button onClick={getStudents}>Listar Alunos</button>
            <h2 id="vasco">Parada</h2>
        </div>
    )
}

export default Base;

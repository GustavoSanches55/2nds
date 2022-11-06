import './App.css';
import Alunos from './components/alunos';
import React, { useState, useEffect } from 'react';

function App() {

  const [alunos, setAlunos] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/listarAlunos/' , {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
    }
  })
      .then(res => res.json())
      .then(data => setAlunos(data))

  }, []);


  return (
    <div className="App">
      {alunos.map(aluno => {
        return <h2>{aluno}</h2>
      })}
    </div>
  );
}

export default App;

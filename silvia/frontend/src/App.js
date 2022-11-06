import './App.css';
import Alunos from './components/alunos';
import React, { useState, useEffect } from 'react';

function App() {

  const [alunos, setAlunos] = useState(['Aluno 1']);



  return (
    <div className="App">
    {alunos.map(aluno => {
      return <Alunos nome={aluno} />
    }
    )}

    </div>
  );
}

export default App;

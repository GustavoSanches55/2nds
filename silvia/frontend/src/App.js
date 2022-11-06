import './App.css';
import Alunos from './components/alunos';
import React, { useState, useEffect } from 'react';
import Head from './components/head';

function App() {

  const [alunos, setAlunos] = useState([]);

  


  return (
    <div className="App">
      <Head />
      <Alunos />

    </div>
  );
}

export default App;

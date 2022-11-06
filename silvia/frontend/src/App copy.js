import './App.css';
import Alunos from './pages/alunos';
import Professores from './pages/professores';
import React, { useState, useEffect } from 'react';
import Head from './components/head';
import ReactDOM from "react-dom";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";



function App() {

  return (
  <Router>
    <div className="App">
      <Head />

      <Switch>
        <Route path="/alunos">
          <Alunos />
        </Route>
    
        <Route path="/professores">
          <Professores />
        </Route>
    
      </Switch>
    </div>
  </Router>
  

  );
}

export default App;

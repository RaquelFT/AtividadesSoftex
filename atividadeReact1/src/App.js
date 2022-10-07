import React, {useState} from 'react';
import './App.css';
import MyPage from './MyPage.js';

function App() {

  const [str, setStr] = useState('Olá mundo!');

  function handleClick(){
    setStr('Seja Bem-vindo!');
  }


  return (
    <div className="App">
      <h2>{str}</h2>
      <MyPage></MyPage>
    </div>
  );
}

export default App;

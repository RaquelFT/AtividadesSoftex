import logo from './logo.svg';
import './App.css';
import HelloWorld from './componentes/HelloWorld';
import Nome from './componentes/Nome';
import Soma from './componentes/Soma';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <HelloWorld/>
        <Nome nome="Raquel"/>
        <Soma/>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
        
        </a>
      </header>
    </div>
  );
}

export default App;
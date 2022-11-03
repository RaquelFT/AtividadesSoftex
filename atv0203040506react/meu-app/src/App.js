import logo from './logo.svg';
import './App.css';
import {Routes,Route,Link} from 'react-router-dom';
import HelloWorld from './componentes/HelloWorld';
import Nome from './componentes/Nome';
import Soma from './componentes/Soma';
import Pg1 from './componentes/Pagina1';
import Pg2 from './componentes/Pagina2';
import Pg3 from './componentes/Pagina3';



function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Link to='/'>Home</Link>
        <Link to='/pag1'>Página 1</Link>
        <Link to='/pag2'>Página 2</Link>
        <Link to='/pag3'>Página 3</Link>
        <img src={logo} className="App-logo" alt="logo" />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
        </a>
      </header> 
      <main>
        <HelloWorld/>
        <Nome nome="Raquel"/>
        <Soma/>
        <Routes>
          <Route path='/pag1' element={<Pg1/>}/>
          <Route path='/pag2' element={<Pg2/>}/>
          <Route path='/pag3' element={<Pg3/>}/>
        </Routes>  
      </main> 
    </div>
    
  );
}

export default App;
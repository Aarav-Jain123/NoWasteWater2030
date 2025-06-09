import { Routes, Route } from 'react-router-dom';
import Home from '../src/Home';
import Quiz from '../src/Quiz';
import Shop from './Shop';
import YourProfile from './YourProfile';
function App() {

  return (
    <Routes>
      <Route path='/' element={<Home/>}/>
      <Route path='/quiz/' element={<Quiz/>}/>
      <Route path='/shop' element={<Shop/>}/>
      <Route path='/your-profile' element={<YourProfile/>}/>
    </Routes>
  )
};

export default App;

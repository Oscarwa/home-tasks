import React, { useEffect } from 'react';
import './App.css';

function App() {
  useEffect(() => {
    fetch('http://127.0.0.1:8000/tasks/').then(res => res.json()).then(console.log)
  }, [])
  return (
    <div className="App">
     
    </div>
  );
}

export default App;

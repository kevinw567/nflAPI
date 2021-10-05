import React from 'react';
import './App.css';
import { Results } from "./results";
import { Sidebar } from "./sidebar";

function App() {
  return (
    <React.Fragment>
      <div className="header"> NFL Stats </div>
      <div>
        <Sidebar/>
      </div>
      <div>
        <Results/>
      </div>
    </React.Fragment>
  );
}

export default App;

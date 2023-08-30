import React from 'react';
import { Route, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import ProposalList from './components/ProposalList';

function App() {
  return (
    <div>
      <nav className="navbar navbar-expand navbar-dark bg-dark">
        <a href="/" className="navbar-brand">
          Personal Loan Proposal
        </a>
      </nav>

      <div className="container mt-3">
        <Routes>
          <Route path="/" element={<ProposalList />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;

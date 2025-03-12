import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import UsersPage from './UsersPage';

function HomePage() {
  return (
    <div>
      <nav style={{ padding: '10px', borderBottom: '1px solid #ccc' }}>
        <Link to="/user">Users</Link>
      </nav>
      <Routes>
        <Route path="/user" element={<UsersPage />} />
      </Routes>
    </div>
  );
}

export default HomePage;
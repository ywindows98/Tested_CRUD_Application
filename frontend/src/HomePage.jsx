import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import UsersPage from './UsersPage';
import UserDetails from './UserDetails';
import UserEdit from './UserEdit';
import UserCreate from './UserCreate';

function HomePage() {
  return (
    <div>
      <nav style={{ padding: '10px', borderBottom: '1px solid #ccc' }}>
        <Link to="/user">Users</Link>
      </nav>
      <Routes>
        <Route path="/user" element={<UsersPage />} />
        <Route path="/user/:userId" element={<UserDetails />} />
        <Route path="/user/:userId/edit" element={<UserEdit />} />
        <Route path="/user/create" element={<UserCreate />} />
      </Routes>
    </div>
  );
}

export default HomePage;
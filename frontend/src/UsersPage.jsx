import React, { useEffect, useState } from 'react';

function UsersPage() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // Assumes the Flask backend exposes the users data at /api/users
    fetch('http://127.0.0.1:5000/user')
      .then((res) => res.json())
      .then((data) => setUsers(data))
      .catch((err) => console.error('Error fetching users:', err));
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Users List</h1>
      {users.length === 0 ? (
        <p>No users found.</p>
      ) : (
        <ul>
          {users.map((user) => (
            <li key={user.id}>
              {user.username} - {user.email}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default UsersPage;
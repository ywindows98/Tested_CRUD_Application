import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { BACKEND_URL } from './config';

function UsersPage() {
  const [users, setUsers] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch(`${BACKEND_URL}/user`)
      .then((res) => res.json())
      .then((data) => setUsers(data))
      .catch((err) => console.error('Error fetching users:', err));
  }, []);

  console.log(users)

  return (
    <div style={{ padding: '20px' }}>
      <h1>Users List</h1>
      <button onClick={() => navigate(`/user/create`)}>
        Create User
      </button>
      {users.length === 0 ? (
        <p>No users found.</p>
      ) : (
          <>
            <ul>
              {users.map((user) => (
                <li key={user.id}>
                  {user.username} | {user.email} | {user.status}
                  <button onClick={() => navigate(`/user/${user.id}`)}>
                    View Details
                  </button>

                </li>
              ))}
            </ul>
          </>
      )}
    </div>
  );
}

export default UsersPage;
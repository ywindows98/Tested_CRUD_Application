import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { BACKEND_URL } from './config';

function UserDetail() {
  const { userId } = useParams();
  const navigate = useNavigate();
  const [userDetail, setUserDetail] = useState(null);

  useEffect(() => {
    fetch(`${BACKEND_URL}/user/${userId}`)
      .then((res) => res.json())
      .then((data) => setUserDetail(data))
      .catch((err) => console.error('Error fetching user detail:', err));
  }, [userId]);

  const handleDelete = () => {
    fetch(`${BACKEND_URL}/user/${userId}`, {
      method: 'DELETE'
    })
      .then((res) => {
        if (res.ok) {
          navigate('/user');
        } else {
          console.error('Failed to delete user');
        }
      })
      .catch((err) => console.error('Error deleting user:', err));
  };

  if (!userDetail) {
    return <p>Loading user details...</p>;
  }

  return (
    <div style={{ padding: '20px' }}>
      <h1>User Detail</h1>
      <p><strong>ID:</strong> {userDetail.id}</p>
      <p><strong>Username:</strong> {userDetail.username}</p>
      <p><strong>Email:</strong> {userDetail.email}</p>
      <p><strong>Subscription ID:</strong> {userDetail.subscription_id}</p>
      <p><strong>Location:</strong> {userDetail.location}</p>
      <p><strong>Registration Date:</strong> {userDetail.date_registered}</p>
      <p><strong>Status:</strong> {userDetail.status}</p>
      <button onClick={() => navigate('/user')} style={{ marginTop: '20px' }}>
        Back to Users List
      </button>
      <button onClick={() => navigate(`/user/${userId}/edit`)} style={{ marginTop: '20px' }}>
        Edit User
      </button>
      <button
        onClick={handleDelete}
        style={{ marginTop: '20px' }}
        >
        Delete User
      </button>
    </div>
  );
}

export default UserDetail;
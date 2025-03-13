import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

function UserDetail() {
  const { userId } = useParams();
  const navigate = useNavigate();
  const [userDetail, setUserDetail] = useState(null);

  useEffect(() => {
    // Assumes the Flask backend exposes individual user data at /user/<userId>
    fetch(`http://127.0.0.1:5000/user/${userId}`)
      .then((res) => res.json())
      .then((data) => setUserDetail(data))
      .catch((err) => console.error('Error fetching user detail:', err));
  }, [userId]);

  if (!userDetail) {
    return <p>Loading user details...</p>;
  }

  return (
    <div style={{ padding: '20px' }}>
      <h1>User Detail</h1>
      <p><strong>ID:</strong> {userDetail.id}</p>
      <p><strong>Username:</strong> {userDetail.username}</p>
      <p><strong>Email:</strong> {userDetail.email}</p>
      <p><strong>Status:</strong> {userDetail.subscription_id}</p>
      <p><strong>Status:</strong> {userDetail.location}</p>
      <p><strong>Status:</strong> {userDetail.date_registered}</p>
      <p><strong>Status:</strong> {userDetail.status}</p>
      <button onClick={() => navigate('/user')} style={{ marginTop: '20px' }}>
        Back to Users List
      </button>
    </div>
  );
}

export default UserDetail;
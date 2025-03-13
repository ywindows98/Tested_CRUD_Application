import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

function UserEdit() {
  const { userId } = useParams();
  const navigate = useNavigate();
  const [userData, setUserData] = useState({
    username: '',
    email: '',
    subscription_id: '',
    location: '',
    date_registered: '',
    status: ''
  });

  useEffect(() => {
    // Fetch the current data for the user
    fetch(`http://127.0.0.1:5000/user/${userId}`)
      .then((res) => res.json())
      .then((data) =>
        setUserData({
          username: data.username,
          email: data.email,
          subscription_id: data.subscription_id,
          location: data.location,
          date_registered: data.date_registered,
          status: data.status
        })
      )
      .catch((err) => console.error('Error fetching user data:', err));
  }, [userId]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUserData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Send a PUT request to update the user's data
    fetch(`http://127.0.0.1:5000/user/${userId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(userData)
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error('Error updating user');
        }
        return res.json();
      })
      .then((data) => {
        console.log('User updated:', data);
        navigate(`/user/${userId}`);
      })
      .catch((err) => console.error('Error updating user:', err));
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Edit User</h1>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '10px' }}>
          <label>
            Username:
            <input
              type="text"
              name="username"
              value={userData.username}
              onChange={handleChange}
            />
          </label>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>
            Email:
            <input
              type="email"
              name="email"
              value={userData.email}
              onChange={handleChange}
            />
          </label>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>
            Subscription ID:
            <input
              type="text"
              name="subscription_id"
              value={userData.subscription_id}
              onChange={handleChange}
            />
          </label>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>
            Location:
            <input
              type="text"
              name="location"
              value={userData.location}
              onChange={handleChange}
            />
          </label>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>
            Date Registered:
            <input
              type="text"
              name="date_registered"
              value={userData.date_registered}
              onChange={handleChange}
            />
          </label>
        </div>
        <div style={{ marginBottom: '10px' }}>
          <label>
            Status:
            <input
              type="text"
              name="status"
              value={userData.status}
              onChange={handleChange}
            />
          </label>
        </div>
        <button type="submit">Save Changes</button>
      </form>
      <button onClick={() => navigate(`/user/${userId}`)} style={{ marginTop: '20px' }}>
        Cancel
      </button>
    </div>
  );
}

export default UserEdit;

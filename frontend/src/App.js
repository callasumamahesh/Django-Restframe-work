import React, { useEffect, useState } from 'react'
import './App.css'
function App() {

  const [usersData, setUsersData] = useState([])

  useEffect(() => {
    fetchUsersData() 
  },[])

  const fetchUsersData = async () => {
    const data = await fetch('http://localhost:8000/api/users/');
    const res = await data.json()
    console.log(res, 'This is data')
    setUsersData(res)
  }

  return (
    <div>
      <h1>Users Data Testing</h1>
      <p>Total users data : {usersData && usersData.length}</p>
    </div>
  )
}

export default App

import React, { useState, useEffect } from "react";
import './App.css';
import Sidebar from "./Components/Sidebar";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({
      name: "",
      age: 0,
      date: "",
      programming: "",
  });

  // Using useEffect for single rendering
  useEffect(() => {
      // Using fetch to fetch the api from 
      // flask server it will be redirected to proxy
      fetch("/data").then((res) =>
          res.json().then((data) => {
              // Setting a data from api
              setdata({
                  name: data.Name,
                  age: data.Age,
                  date: data.Date,
                  programming: data.programming,
              });
          })
      );
  }, []);
  
  return (
    <>
      <Router>
        <Sidebar />
        <Routes>
          <Route path='/' />
        </Routes>
      </Router>
    </>
  );
}

export default App;

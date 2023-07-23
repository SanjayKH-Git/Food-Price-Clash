import React, { useState } from "react";
import "./App.css";

function App() {
  const [location, setLocation] = useState("");
  const [responseData, setResponseData] = useState("");

  const handleInputChange = (event) => {
    setLocation(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      alert("submit");

      const response = await fetch(`http://127.0.0.1:8000/${location}`);
      console.log(response); // Add this line to inspect the response
      const data = await response.json();
      console.debug(data);
      alert(data);

      setResponseData(data.message);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };


  return (
    <div className="App">
      <header className="App-header">
        <form onSubmit={handleSubmit}>
          <label>
            Enter Location:
            <input
              type="text"
              value={location}
              onChange={handleInputChange}
            />
          </label>
          <button type="submit">Submit</button>
        </form>
        <p>{responseData}</p>
      </header>
    </div>
  );
}

export default App;

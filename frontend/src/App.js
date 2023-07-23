import React, { useState } from "react";
import "./App.css";

function App() {
  const [location, setLocation] = useState("");
  const [resturant, setResturant] = useState("");
  const [responseData, setResponseData] = useState("");

  const handleInputChange = (event) => {
    setLocation(event.target.value);
  };

  const handleRestaurantChange = (event) => {
    setResturant(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // alert("submit");

      const response = await fetch(`http://127.0.0.1:8000/${location}/${resturant}`);
      console.log(response); // Add this line to inspect the response
      const data = await response.json();
      console.debug(data);
      // alert(data);

      setResponseData(data.message);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };


  return (
    <div className="App">
      <div className="App-base">
        <header className="App-header">
          <h3 className="header-text">Welcome to Food Price Clash!</h3>
        </header>

        <div className="App-search">
          <form onSubmit={handleSubmit}>
            <div>
              <label>
                Enter Location:
                <input
                  type="text"
                  value={location}
                  onChange={handleInputChange}
                  required/>
              </label>
            </div>

            <div>
              <label>
                Search Food/Restaurant:
                <input
                  type="text"
                  value={resturant}
                  onChange={handleRestaurantChange}
                  required/>
              </label>
            </div>

            <div>
              <button type="submit">Search Clash</button>
            </div>
          </form>
          <p>{responseData}</p>
        </div>
      </div>
    </div>
  );
}

export default App;

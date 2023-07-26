import React, { useState } from "react";
import "./App.css";

function App() {
  const [location, setLocation] = useState("");
  const [restaurant, setRestaurant] = useState("");
  const [responseData, setResponseData] = useState({});

  const handleInputChange = (event) => {
    setLocation(event.target.value);
  };

  const handleRestaurantChange = (event) => {
    setRestaurant(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch(`http://127.0.0.1:8000/${location}/${restaurant}`);
      const data = await response.json();
      setResponseData(data.message);
      console.debug(data.message);
      if (data && data.message) {
        console.debug("Data Message (Swiggy):", data.message.swiggy);
        console.debug("Data Message (Zomato):", data.message.zomato);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
      setResponseData({}); // Reset to an empty object on error
    }
  };

  const renderTable = (data, platform) => {
    if (!data || Object.keys(data).length === 0) {
      return (
        <div className="table-container">
          <h2>{platform}</h2>
          <p>None</p>
        </div>
      );
    }

    return (
      <div className="table-container">
        <h2>{platform}</h2>
        <table>
          <thead>
            <tr>
              <th>Food Name</th>
              <th>Price</th>
            </tr>
          </thead>
          <tbody>
            {Object.keys(data).map((foodName) => (
              <tr key={foodName}>
                <td>{foodName}</td>
                <td>{data[foodName]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
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
                  required
                />
              </label>
            </div>

            <div>
              <label>
                Search Food/Restaurant:
                <input
                  type="text"
                  value={restaurant}
                  onChange={handleRestaurantChange}
                  required
                />
              </label>
            </div>

            <div>
              <button type="submit">Search Clash</button>
            </div>
          </form>
        </div>

        <div className="table-wrapper">
          <p>{responseData.swiggy} </p>

          {renderTable(responseData.swiggy, "Swiggy")}
          {renderTable(responseData.zomato, "Zomato")}
        </div>
      </div>
    </div>
  );
}

export default App;

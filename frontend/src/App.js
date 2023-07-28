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
      console.debug(data);
      if (data && data.message) {
        console.debug("Data Message (Swiggy):", data.message.swiggy);
        console.debug("Data Message (Zomato):", data.message.zomato);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
      setResponseData({}); // Reset to an empty object on error
    }
  };

  const renderSuggestion = (swiggy_common_Total, zomato_common_Total) => {
    // alert(swiggy_common_Total);
    if (swiggy_common_Total === undefined) {
      return (
        <div>
          <p className="initial">Please Enter Correct Details and Check Outstanding Real-Time Statistics.</p>
        </div>
      );
    } else if (swiggy_common_Total === zomato_common_Total) {
      return (
        <div>
          <h4 className="live">Live</h4>
          <p className="equal">Based on our analysis, both Swiggy and Zomato have similar prices.
            However, we recommend checking the Real-Time Price Table displayed below for more details.</p>
        </div>
      );
    } else if (swiggy_common_Total < zomato_common_Total) {
      return (
        <div>
          <h4 className="live">Live</h4>
          <p className="swiggyCheap">Based on our Real-time analysis, <i className="s">Swiggy</i> is cheaper than <i className="z">Zomato</i> Today.</p>
        </div>
      );
    } else {
      return (
        <div>
          <h4 className="live">Live</h4>
          <p className="zomatoCheap">Based on our Real-time analysis, <i className="z">Zomato</i> is cheaper than <i className="s">Swiggy</i> Today.</p>
        </div>
      );
    }
  };

  const renderTable = (data, platform) => {
    if (!data || Object.keys(data).length === 0) {
      return (
        <div className={`table-container ${platform === 'Swiggy' ? 'swiggyTable' : 'zomatoTable'}`}>
          <h2>{platform}</h2>
          <p>None</p>
        </div>
      );
    }

    const zomatoData = responseData.zomato || {};

    return (
      <div className={`table-container ${platform === 'Swiggy' ? 'swiggyTable' : 'zomatoTable'}`}>
        <h2>{platform}</h2>
        <table>
          <thead>
            <tr>
              <th>Food Name</th>
              <th>Price</th>
            </tr>
          </thead>
          <tbody>
            {Object.keys(data).map((foodName) => {
              const swiggyPrice = data[foodName];
              const zomatoPrice = zomatoData[foodName];
              const isSwiggyCheaper = swiggyPrice && zomatoPrice && swiggyPrice < zomatoPrice;
              const isZomatoCheaper = zomatoPrice && swiggyPrice && zomatoPrice < swiggyPrice;

              return (
                <tr
                  key={foodName}
                  className={isSwiggyCheaper ? (platform === 'Swiggy' ? 'swiggyCheap' : '') : isZomatoCheaper ? (platform === 'Zomato' ? 'zomatoCheap' : '') : ''}
                >
                  <td>{foodName}</td>
                  <td>{swiggyPrice}₹</td>
                </tr>
              );
            })}
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

        <h3>Our Suggestion:</h3>
        <div className="suggestion">
          <p>{renderSuggestion(responseData.swiggy_common_Total, responseData.zomato_common_Total)} </p>
        </div>

        <div className="table-wrapper">
          {renderTable(responseData.swiggy, "Swiggy")}
          {renderTable(responseData.zomato, "Zomato")}
        </div>
      </div>
    </div>
  );
}

export default App;

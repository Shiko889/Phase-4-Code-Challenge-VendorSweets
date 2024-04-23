import React, { useState, useEffect } from 'react';
import { Switch, Route } from 'react-router-dom';
import Header from './Header';
import Vendor from './Vendor';
import Home from './Home';

function App() {
  const [vendors, setVendors] = useState([]);

  useEffect(() => {
    fetch('/vendors')
      .then(response => response.json())
      .then(data => setVendors(data));
  }, []);

  return (
    <div>
      <Header />
      <main>
        <Switch>
          <Route exact path="/vendors/:id">
            <Vendor />
          </Route>
          <Route exact path="/">
            <Home vendors={vendors} />
          </Route>
        </Switch>
      </main>
    </div>
  );
}

export default App;

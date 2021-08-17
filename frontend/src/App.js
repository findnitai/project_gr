
import React, { useState } from "react";
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';
import Details from './components/Details';
import Cookies from "js-cookie";

import Dashboard from './components/Dashboard';
// import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

const AuthApi = React.createContext();
const TokenApi = React.createContext(); 


function App() {

  const [auth, setAuth] = useState(false);
  const [token, setToken] = useState("");
  const readCookie = () => {
    let token = Cookies.get("token");
    if (token) {
      setAuth(true);
      setToken(token);
    }
  };
  React.useEffect(() => {
    readCookie();
  }, []);

  return (
  <>
    <AuthApi.Provider value = {{ auth, setAuth }}>
    <TokenApi.Provider value = {{ token, setToken }}>
    <Router>
      <Switch>
        {!auth ? (
        <Route path="/login" exact component={SignIn} /> ) : (<></>)
        }
        {!auth ? (
          <Route path="/signup" exact component={SignUp} /> ) : (<></>)
        }
        
        <Route path="/details" exact component={Details} />
        <Route path="/dash" exact component={Dashboard} />
      </Switch>
    </Router>
    </TokenApi.Provider>
    </AuthApi.Provider>
  </>
  );
}

export default App;

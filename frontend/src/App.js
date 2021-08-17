
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';
import Details from './components/Details';

import Dashboard from './components/Dashboard';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/login" exact component={SignIn} />
        <Route path="/signup" exact component={SignUp} />
        <Route path="/details" exact component={Details} />
        <Route path="/dash" exact component={Dashboard} />
      </Switch>
    </Router>
  );
}

export default App;

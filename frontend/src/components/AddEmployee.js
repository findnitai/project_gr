import React, {useState} from 'react';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import axios from 'axios'

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '150%', // Fix IE 11 issue.
    marginTop: theme.spacing(3),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export default function SignUp() {
  const classes = useStyles();

  const [name, setName] = useState('');
  const [phone_number, setNumber] = useState('');
  const [email, setEmail] = useState('');
  const [address, setAddress] = useState('');
  const [cin, setCIN] = useState('');
  const [tax_registration_number, setTRN] = useState('');

  const handleSubmitEmployee = async (e) => {
        e.preventDefault();
        console.log(name, email, phone_number, address, cin, tax_registration_number)
        const employee = {
            name : name,
            email : email,
            phone_number : phone_number,
            address : address,
            cin : cin,
            tax_registration_number : tax_registration_number
        }
         const resp = await axios.post('http://localhost:8000/api/client/', employee);
         console.log(resp);
    }

  

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Typography component="h1" variant="h5">
          Add a new Employee
        </Typography>
        <form className={classes.form} noValidate>
          <Grid container spacing={2}>
          <Grid item xs={6} >
              <TextField
                autoComplete="fname"
                name="firstName"
                variant="outlined"
                fullWidth
                label="Employee Name"
                autoFocus
                onChange={e => setName(e.target.value)}
              />
              
            </Grid>
            <Grid item xs={6} >
              <TextField
                variant="outlined"
                required
                fullWidth
                id="address"
                label="Email ID"
                onChange={e => setNumber(e.target.value)}
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                variant="outlined"
                required
                fullWidth
                label="Salary Currency"
                onChange={e => setEmail(e.target.value)}
              />
            </Grid>
            <Grid item xs={6}>
                          <TextField
                            variant="outlined"
                            required
                            fullWidth
                            label="Offer Value"
                            onChange={e => setAddress(e.target.value)}
                          />
                        </Grid>
            {/* <Grid item xs={6}>
                          <TextField
                            variant="outlined"
                            fullWidth
                            id="address"
                            label="Company CIN"
                            onChange={e => setCIN(e.target.value)}
                          />
                        </Grid>
            <Grid item xs={6}>
                          <TextField
                            variant="outlined"
                            fullWidth
                            id="address"
                            label="Tax Registration Number"
                            onChange={e => setTRN(e.target.value)}
                          />
                        </Grid> */}

          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
            onClick={handleSubmitEmployee}
          >
            Add Employee
          </Button>
        </form>
      </div>
    </Container>
  );
}
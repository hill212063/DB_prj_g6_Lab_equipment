import UserFooter from '@/components/UserFooter'
import Link from "next/link"
import styles from "@/styles/Home.module.css"
import { useState } from 'react';
import axios from 'axios';
import { useRouter } from 'next/router';


export default function Home() {
  const [u_email, setu_email] = useState('');
  const [u_password, setu_password] = useState('');
  const router = useRouter()
  const handleICITChange = (e) => {
    setu_email(e.target.value);
  };

  const handleu_passwordChange = (e) => {
    setu_password(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post(`${process.env.NEXT_PUBLIC_BASE_URL_BACKEND}/api/login/`, 
    { u_email:u_email, u_password:u_password })
    .then((response) => {
      window.localStorage.setItem('role', `${response.data.role}`);
      window.localStorage.setItem('token', `${response.data.token}`);
      window.localStorage.setItem('u_id', `${response.data.u_id}`);
      if(response.data.role === 'Admin'){
        router.push("/Admin")
      }else if(response.data.role === 'User'){
        router.push('/Items')
      }
    })
    .catch((error) => {
      console.error(error);
    });
};


  return (
    <>
    <div className={styles.container}>
      <h1>Login</h1>
      <form onSubmit={handleSubmit} className={styles.form}>
        <label htmlFor="u_email" className={styles.label}>Email:</label>
        <input
          type="text"
          id="u_email"
          value={u_email}
          onChange={handleICITChange}
          className={styles.input}
          required
        />
        <label htmlFor="u_password" className={styles.label}>password:</label>
        <input
          type="password"
          id="u_password"
          value={u_password}
          onChange={handleu_passwordChange}
          className={styles.input}
          required
        />
        <button type="submit" className={styles.button}>Login</button>
      </form>
    </div>
    <UserFooter/>
    </>
  );
}


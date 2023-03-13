import UserFooter from '@/components/UserFooter'
import Link from "next/link"
import styles from "@/styles/Home.module.css"
import react from 'react'
import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [ICITID, setICITID] = useState('');
  const [password, setPassword] = useState('');

  const handleICITChange = (e) => {
    setICITID(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/login', { ICITID, password })
    .then((response) => {
      console.log(response.data);
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
        <label htmlFor="ICIT" className={styles.label}>Email:</label>
        <input
          type="text"
          id="ICITID"
          value={ICITID}
          onChange={handleICITChange}
          className={styles.input}
          required
        />
        <label htmlFor="password" className={styles.label}>Password:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={handlePasswordChange}
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


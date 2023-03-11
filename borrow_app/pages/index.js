import UserFooter from '@/components/UserFooter'
import Link from "next/link"
import styles from "@/styles/Home.module.css"
import react from 'react'
import { useState } from 'react';

export default function Home() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // TODO: Implement login logic here
  };

  return (
    <>
    <div className={styles.container}>
      <h1 className={styles.title}>Login</h1>
      <form onSubmit={handleSubmit} className={styles.form}>
        <label htmlFor="email" className={styles.label}>Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={handleEmailChange}
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


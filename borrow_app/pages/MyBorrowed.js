import UserNavbar from "@/components/UserNavbar"
import Head from "next/head"
import styles from "@/styles/MyBorrowed.module.css"
import Image from 'next/image';
import { useState } from "react";

export default function MyBorrowed() {
    const [search, setSearch] = useState('');

  const handleSearchChange = (e) => {
    setEmail(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // TODO: Implement login logic here
  };
    return (
    <>
        <Head>
                <title>การยืมของฉัน | My borrowed</title>
        </Head>
        <UserNavbar/>
        <h1> 
            <div className={styles.label}>
                This is My borrowed Items page
            </div>
            </h1>
        <div className={styles.center}> 
            <label htmlFor="search" className={styles.labelsearch}>Search:</label>
                <input
                    type="text"
                    id="search"
                    value={search}
                    onChange={handleSearchChange}
                    className={styles.input}
                    required
                    />
            <button type="submit" className={styles.button}>search</button>
        </div>  
        <div className={styles.center}>
            <div className={styles.box}>
                <h2 className={styles.label2}>Label
                </h2>
        
                <div className={styles.image}>
                    <Image
                        src="/image.png"
                        alt="Example Image"
                        width={200}
                        height={200}
                />
                </div>
            <button className={styles.button}>see more</button>
            </div>
        </div>
        <div className={styles.center}>
            <div className={styles.box}>
                <h2 className={styles.label2}>Label
                </h2>
        
                <div className={styles.image}>
                    <Image
                        src="/image.png"
                        alt="Example Image"
                        width={200}
                        height={200}
                />
                </div>
            <button className={styles.button}>see more</button>
            </div>
        </div>
        <div className={styles.center}>
            <div className={styles.box}>
                <h2 className={styles.label2}>Label
                </h2>
        
                <div className={styles.image}>
                    <Image
                        src="/image.png"
                        alt="Example Image"
                        width={200}
                        height={200}
                />
                </div>
            <button className={styles.button}>see more</button>
            </div>
        </div>
    </>
    )
};

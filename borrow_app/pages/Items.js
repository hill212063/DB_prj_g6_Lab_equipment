import UserFooter from '@/components/UserFooter'
import UserNavbar from '@/components/UserNavbar'
import styles from "@/styles/Items.module.css";
import { useState, useEffect } from "react";
import axios from "axios"; // or import your MongoDB library here

import Image from 'next/image';

export default function Items() {
  const [searchTerm, setSearchTerm] = useState("");
  const [items, setItems] = useState([]);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('/api/items');
        setItems(response.data);
      } catch (error) {
        console.log(error);
      }
    };
    fetchData();
  }, []);
  

  const handleSearch = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.get(`/api/items?search=${searchTerm}`);
      setItems(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <>
      <UserNavbar />
      <main className={styles.blogMain}>
        <h2 className={styles.blogTitle}>ITEMS</h2>
        <p className={styles.blogDescription}>
          What item do you want to borrow? Let's find it!
        </p>
        <form className={styles.searchBar} onSubmit={handleSearch}>
          <input
            type="text"
            placeholder="Search for items..."
            value={searchTerm}
            onChange={(event) => setSearchTerm(event.target.value)}
          />
          <button className={styles.searchBtn} type="submit">
            Search
          </button>
        </form>

        {/* Section for post */}
        <section id="posts">
          {items.map((item) => (
            <div className={styles.post} key={item._id}>
              <div className={styles.imgBlogOne}>
                <Image alt="" src={item.imageUrl} width={200} height={200} />
              </div>
              <div className={styles.textBlogPost}>
                <h3>{item.name}</h3>
                <p className={styles.postAuthor}>Status: {item.status}</p>
                <p className={styles.postDate}>Category: {item.category}</p>
                <p className={styles.postExcerpt}>Description: {item.description}</p>
                <a href="">
                  <button className={styles.readMoreBtn}>More Detail</button>
                </a>
              </div>
            </div>
          ))}
        </section>
        

        {/* For example in section ^^ : examplay /#posts*/}
        <div className={styles.post}>
            <div className={styles.imgBlogTwo}>
                <Image alt="" src="/items/Oscil.png" width={200} height={200}/>
            </div>
            <div className={styles.textBlogPost}>
              <h3>ITEMS 2</h3>
              <p className={styles.postAuthor}>Status : </p>
              <p className={styles.postDate}>Category : </p>
              <p className={styles.postExcerpt}>Description : </p>
              <a href="">
                <button className={styles.readMoreBtn}>More Detail</button>
              </a>
            </div>
          </div>
      </main>
      <UserFooter />
    </>
  );
}

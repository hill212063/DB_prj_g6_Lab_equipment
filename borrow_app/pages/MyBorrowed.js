import UserFooter from '@/components/UserFooter'
import UserNavbar from '@/components/UserNavbar'
import styles from "@/styles/MyBorrowed.module.css";
import { useState, useEffect } from "react";
import axios from "axios"; // or import your MongoDB library here
import { useRouter } from 'next/router';
import DataTable from 'react-data-table-component';
import Link from 'next/link';
export default function MyBorrowed() {
    const router = useRouter()
    const [search, setSearch] = useState("");
    const [filteredItems, setFilteredItems] = useState([]);

    const [items, setItems] = useState([]);
    const fetchData = async (uid,token) => {
      try {
      axios.get(`${process.env.NEXT_PUBLIC_BASE_URL_BACKEND}/api/update-expire/`)
      .then(res =>{
        axios.get(`${process.env.NEXT_PUBLIC_BASE_URL_BACKEND}/api/borrowed/${uid}/`)
        .then(response => {
          //  console.log(response);
          setItems(response.data);
          setFilteredItems(response.data);
        })
        .catch(error => {
          console.log(error);
        });
      }
      ).catch(error => {
        console.log(error);
      });

      } catch (error) {
        console.log(error);
      }
    }
 
    useEffect(() => {
      let role = window.localStorage.getItem('role');
      let u_id = window.localStorage.getItem('u_id');
      let token = window.localStorage.getItem('token');
      if(!role || !token){
        router.push('/')
      }
      fetchData(u_id,token);
    }, []);

    useEffect(() => {
      const result = items.filter(items=> {
        return items.item_name.toLowerCase().match(search.toLowerCase());
      })
  
      setFilteredItems(result);
    }, [search])

    const columns = [
      {
        name: "BORROWED TABLE",
        cell: row => (
          <section id="posts">
          
            <div className={styles.post}>
              <div className={styles.imgBlogOne}>
                <img alt="" src={row.item_img_url} width={200} height={200} />
              </div>
              <div className={styles.textBlogPost}>
                <h3>{row.item_name}</h3>
                <p className={styles.postAuthor}>Status: {row.item_status}</p>
                <p className={styles.postDate}>Category: {row.item_category}</p>
                <p className={styles.postExcerpt}>Description: {row.item_description}</p>
                <Link href="/Contact">
                    <button className={styles.readMoreBtn}>Contact</button>
                  </Link>
              </div>
            </div>
          
        </section>
        )
      }
    ];
    

    return (
      <>
        <UserNavbar />
        <main className={styles.blogMain}>
          <h2 className={styles.blogTitle}>MY BORROWED</h2>
          
          
  
          {/* Section for post */}
          <DataTable
          columns={columns}
          data={filteredItems}
          pagination
          fixedHeader
          noTableHead
          fixedHeaderScrollHeight="1500px"
          subHeader
          subHeaderComponent={
            <input 
              type="text" 
              placeholder="Search by Items name" 
              className="w-50 form-control searchcenter"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              ></input>
          }
          subHeaderAlign="center">
          
          </DataTable>
          {/* For example in section ^^ : examplay /#posts
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
            </div> */}
        </main>
        <UserFooter />
      </>
    );
  }
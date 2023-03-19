import UserNavbar from "@/components/UserNavbar";
import Head from "next/head";
import Link from "next/link";
import styles from "@/styles/Contact.module.css"
import Image from "next/image";
import { useEffect } from "react";
import { useRouter } from 'next/router';
import UserFooter from "@/components/UserFooter";
export default function Contact() {
  const router = useRouter()
  useEffect(() => {
    let role = window.localStorage.getItem('role');
    let token = window.localStorage.getItem('token');
    if (!role || !token) {
      router.push('/')
    }
  }, []);
  return (
    <>
      <Head>
        <title>ติดต่อ | Contact</title>
      </Head>

      <UserNavbar />
      <section className={styles.sectiontitle}>
        <div className={styles.container}>
          
          <div className={styles.address}>
          <div className={styles.logo}>
            <a href="https://ece.eng.kmutnb.ac.th/home/index.php">
              <img
                src="https://ece.eng.kmutnb.ac.th/home/wp-content/uploads/ECELogo2020_400x400-150x150.png"
                alt="ECE Logo"
                width="200"
                height="200"
              />
            </a>
          </div>
            <address>
              ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์
              <br />
              คณะวิศวกรรมศาสตร์
              <br />
              มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ
              <br />
              1518 ถ.ประชาราษฏร์ 1 แขวงวงศ์สว่าง
              <br />
              บางซื่อ กทม. 10800
            </address>
            <address>โทรศัพท์ 02-555-2000 ต่อ 8519, 8520</address>
            <address>
              <a
                href="https://www.facebook.com/ECE-kmutnb-120163421404222/?ref=br_rs"
                target="_blank"
                rel="noopener noreferrer"
              >
                <img
                  src="http://www.ece.eng.kmutnb.ac.th/home/wp-content/uploads/2018/02/124010-150x150.png"
                  alt="Facebook Logo"
                  width="50"
                  height="50"
                />
              </a>
            </address>
            <address>
              
              สำหรับการติดต่อบุคลากรของภาควิชาฯ 
              <br />
              ท่านสามารถติดต่อผ่านทางอีเมล์
              <br />
              Firstname.L@eng.kmutnb.ac.th
              <br />
              โดย L เป็นอักษรอังกฤษตัวแรกของนามสกุล
              <br />
              หรือสืบค้นได้จากเว็บไซต์
              <br />
              <Link href="https://www.eng.kmutnb.ac.th/web/staff.php?dept=0101">https://www.eng.kmutnb.ac.th/web/staff.php?dept=0101</Link>
            </address>
            
          </div>
          
          
        </div>
        
        
      </section>
     
      
      
      <UserFooter/>


    </>

  )
};

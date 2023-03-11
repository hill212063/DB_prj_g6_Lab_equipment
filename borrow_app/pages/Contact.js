import UserNavbar from "@/components/UserNavbar";
import Head from "next/head";
import Link from "next/link";
import styles from "@/styles/Contact.module.css"
import Image from "next/image";
export default function Contact() {
    return (
        <>
            <Head>
                <title>ติดต่อ | Contact</title>
            </Head>
            
            <UserNavbar/>
            <h1>
                <div className={styles.mes}>
                    <label className = {styles.label} > Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eu scelerisque elit. 
                    <br/>Quisque interdum pellentesque rhoncus. Mauris tempor sollicitudin tincidunt. 
                    <br/>Phasellus sodales ornare sagittis. Sed viverra neque dolor, quis tristique urna dignissim eu. 
                    <br/>Phasellus euismod ex a odio dignissim hendrerit. Praesent sollicitudin ligula quis fermentum viverra. 
                    <br/>Nam eget tristique leo, in gravida sem.Aenean tristique massa mauris, luctus 
                    <br/>porta eros blandit at. Suspendisse quam orci, rhoncus eu purus a, 
                    </label>
                </div>
                <div>
                    <Image src="/contact.jpg" alt = "logo"  width= {100} height= {100}  className={styles.image} />
                </div>

            </h1>
        
        </>
            
    )
};

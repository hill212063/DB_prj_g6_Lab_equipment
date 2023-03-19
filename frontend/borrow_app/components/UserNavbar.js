import Link from "next/link"
import Head from "next/head";
// Import the FontAwesomeIcon component
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import the icons you need
import {
  faBars
} from "@fortawesome/free-solid-svg-icons";

import { useState,useEffect } from "react";
import { useRouter } from "next/router";


export default function UserNavbar() {
    const router = useRouter();
    const [role,setRole] = useState("");
    useEffect(() => {
        if(router.isReady){
            setRole(window.localStorage.getItem('role'))
         }
      }, [router.isReady]);
    return (
        <>
        <Head>
            <script src="../scripts/side_controll.js" />
            
        </Head>

        <div id="page-top">
        <nav className="navbar navbar-expand-lg bg-navcolor text-uppercase fixed-top" id="mainUserNav">
            <div className="container">
                <a className="navbar-brand" href="/Items">BORROW APP</a>
                <button className="navbar-toggler text-uppercase font-weight-bold bg-menu text-white rounded" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                <FontAwesomeIcon icon={faBars} width="20" height="20"/>
                </button>
                <div className="collapse navbar-collapse" id="navbarResponsive" role="tablist">
                    <ul className="navbar-nav ms-auto nav-pills">
                        { (role==='Admin')
                        ? <li className="nav-item mx-0 mx-lg-1"><Link className="nav-link py-3 px-0 px-lg-3 rounded"  href="/Admin">Dashboard</Link></li>
                        : <></>
                        }

                        <li className="nav-item mx-0 mx-lg-1"><Link className="nav-link py-3 px-0 px-lg-3 rounded"  href="/Items">Items</Link></li>
                        <li className="nav-item mx-0 mx-lg-1"><Link className="nav-link py-3 px-0 px-lg-3 rounded" href="/MyBorrowed">My Borrowed</Link></li>
                        <li className="nav-item mx-0 mx-lg-1"><Link className="nav-link py-3 px-0 px-lg-3 rounded" href="/Contact">Contact</Link></li>
                        <li className="nav-item mx-0 mx-lg-1"><Link type="button" className="btn btn-primary py-3 px-0 px-lg-3 rounded" onClick={(e)=>{
                             window.localStorage.clear();
                        }} href="/">Logout</Link></li>
                        
                    </ul>
                </div>
            </div>
        </nav>
        </div>
        {/* <nav className="userNav">
            <div className="Logo">
                <Link href="/">BORROW APP</Link>

            </div>
            <div className="NavBTN">
            <Link href="/Admin">Dashboard</Link>
            <Link href="/Items">Items</Link>
            <Link href="/MyBorrowed">My borrowed</Link>
            <Link href="/Contact">Contact</Link>
            <Link href="/">Logout</Link>
            </div>
        </nav> */}
        </>
    )
    
};

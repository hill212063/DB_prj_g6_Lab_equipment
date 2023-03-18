// Import the FontAwesomeIcon component
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import the icons you need
import {
  faBars
} from "@fortawesome/free-solid-svg-icons";
import Head from "next/head";
import Link from "next/link";
import { useState, useEffect } from 'react';

export default function AdminNavbar() {
  const ReloadWhenToggle = () => {
    setTimeout(() => {
    location.reload()
  }, 200);
    
  };
  
  
    return (
        
        <>
        <Head>
            <script src="../scripts/side_controll.js" />
        </Head>
        
        
        <nav className="sb-topnav navbar navbar-expand navbar-dark bg-dark">
            {/* Navbar Brand */}
            <Link href="/Admin/UsersManage" className="navbar-brand ps-3">
            <div>BORROW APP</div>
            </Link>
            {/* Sidebar Toggle */}
            <button className="btn btn-link btn-sm order-1 order-lg-0 me-4 me-lg-0" id="sidebarToggle" >
              <FontAwesomeIcon icon={faBars} />
            </button>
            {/* Navbar Search */}
            <form className="d-none d-md-inline-block form-inline ms-auto me-0 me-md-3 my-2 my-md-0">
            </form>
            {/* Navbar */}
            <ul className="navbar-nav ms-auto ms-md-0 me-3 me-lg-4">
                <li className="nav-item dropdown">
                    <a className="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Options
                    </a>
                    <ul className="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                      <li>
                        <Link className="dropdown-item" href="/Items">
                        <div >User view</div>
                        </Link>
                      </li>
                      <li><hr className="dropdown-divider" /></li>
                      <li>
                        <Link className="dropdown-item" onClick={(e)=>{
                             window.localStorage.clear();
                        }} href="/">
                        <div >Logout</div>
                        </Link>
                        </li>
                    </ul>
                </li>
            </ul>
        </nav>
        
        </>
    )
};

import Link from "next/link"
import Head from "next/head";
// Import the FontAwesomeIcon component
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import the icons you need
import {
  faBars
} from "@fortawesome/free-solid-svg-icons";

export default function UserNavbar() {
    return (
        <>
        <Head>
            <script src="../scripts/side_controll.js" />
            
        </Head>

        <div id="page-top">
        <nav class="navbar navbar-expand-lg bg-navcolor text-uppercase fixed-top" id="mainUserNav">
            <div class="container">
                <a class="navbar-brand" href="/Items">BORROW APP</a>
                <button class="navbar-toggler text-uppercase font-weight-bold bg-menu text-white rounded" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                <FontAwesomeIcon icon={faBars} width="20" height="20"/>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive" role="tablist">
                    <ul class="navbar-nav ms-auto nav-pills">
                    <li class="nav-item mx-0 mx-lg-1"><Link class="nav-link py-3 px-0 px-lg-3 rounded"  href="/Admin">Dashboard</Link></li>
                        <li class="nav-item mx-0 mx-lg-1"><Link class="nav-link py-3 px-0 px-lg-3 rounded"  href="/Items">Items</Link></li>
                        <li class="nav-item mx-0 mx-lg-1"><Link class="nav-link py-3 px-0 px-lg-3 rounded" href="/MyBorrowed">My Borrowed</Link></li>
                        <li class="nav-item mx-0 mx-lg-1"><Link class="nav-link py-3 px-0 px-lg-3 rounded" href="/Contact">Contact</Link></li>
                        <li class="nav-item mx-0 mx-lg-1"><Link type="button" class="btn btn-primary py-3 px-0 px-lg-3 rounded" href="/">Logout</Link></li>
                        
                    </ul>
                </div>
            </div>
        </nav>
        </div>
        {/* <nav class="userNav">
            <div class="Logo">
                <Link href="/">BORROW APP</Link>

            </div>
            <div class="NavBTN">
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

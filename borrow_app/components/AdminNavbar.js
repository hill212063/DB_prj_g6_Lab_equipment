// Import the FontAwesomeIcon component
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import the icons you need
import {
  faBars
} from "@fortawesome/free-solid-svg-icons";
import Head from "next/head";
import Link from "next/link";

export default function AdminNavbar() {
    return (
        
        <>
        <Head>
            <script src="../scripts/side_controll.js" />
        </Head>
        
        
        <nav class="sb-topnav navbar navbar-expand navbar-dark bg-dark">
            {/* Navbar Brand */}
            <Link href="/Admin/UsersManage" class="navbar-brand ps-3">
            <div>BORROW APP</div>
            </Link>
            {/* Sidebar Toggle */}
            <button class="btn btn-link btn-sm order-1 order-lg-0 me-4 me-lg-0" id="sidebarToggle" href="#!">
              <FontAwesomeIcon icon={faBars} />
            </button>
            {/* Navbar Search */}
            <form class="d-none d-md-inline-block form-inline ms-auto me-0 me-md-3 my-2 my-md-0">
            </form>
            {/* Navbar */}
            <ul class="navbar-nav ms-auto ms-md-0 me-3 me-lg-4">
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Options
                    </a>
                    <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                      <li>
                        <Link class="dropdown-item" href="/Contact">
                        <div >User view</div>
                        </Link>
                      </li>
                      <li><hr class="dropdown-divider" /></li>
                      <li>
                        <Link class="dropdown-item" href="/">
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

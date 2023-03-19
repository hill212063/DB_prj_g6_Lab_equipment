// Import the FontAwesomeIcon component
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useEffect, useState, useRouter } from "react";
// import the icons you need
import {
  faUser,
  faInfo,
  faTools,
  faBars

} from "@fortawesome/free-solid-svg-icons";
import Link from "next/link";
import Head from "next/head";
import styles from "@/styles/AdminNav.module.css"

export default function AdminSidebar() {


  return (
    <>
    <div id="layoutSidenav_nav">
      
        <nav className="bg-dark sb-sidenav accordion sb-sidenav-dark" id="sidenavAccordion">
          <div className="sb-sidenav-menu">
            <div className="nav">
              <div className="sb-sidenav-menu-heading">Management</div>
              <Link  className="nav-link" href="/Admin/UsersManage">
                <div className="sb-nav-link-icon">
                  <FontAwesomeIcon
                    icon={faUser}
                    width="15px"
                  />
                </div>
                Users Management
              </Link>
              <Link  className="nav-link" href="/Admin/BorrowedInfo">
                <div className="sb-nav-link-icon">
                  <FontAwesomeIcon
                    icon={faInfo}
                    width="18px"
                  />
                </div>
                Borrowing Information
              </Link>
              <Link className="nav-link" href="/Admin/ItemsManage">
                <div className="sb-nav-link-icon">
                  <FontAwesomeIcon
                    icon={faTools}
                    width="20px"
                  />
                </div>
                Item Management
              </Link>
              {/* <Link className="nav-link" href="/Admin/test">
              <div className="sb-nav-link-icon">
              <FontAwesomeIcon 
              icon={faTools}
              width ="20px"
              />
              </div>
              Test BUG
            </Link> */}
            </div>
          </div>
          <div className="sb-sidenav-footer">
            <div className="small">Logged in as:</div>
            Admin
          </div>
        </nav>
      </div>

    </>
  );
}

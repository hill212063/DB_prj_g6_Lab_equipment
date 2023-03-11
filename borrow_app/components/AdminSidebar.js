// Import the FontAwesomeIcon component
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

// import the icons you need
import {
  faUser,
  faInfo,
  faTools
  
} from "@fortawesome/free-solid-svg-icons";
import Script from "next/script";
import Link from "next/link";

export default function AdminSidebar() {
  return (
    <>
    <div id="layoutSidenav_nav">
      <nav class="sb-sidenav accordion sb-sidenav-dark" id="sidenavAccordion">
        <div class="sb-sidenav-menu">
          <div class="nav">
            <div class="sb-sidenav-menu-heading">Management</div>
            <Link class="nav-link" href="/Admin/UsersManage">
              <div class="sb-nav-link-icon"> 
              <FontAwesomeIcon 
              icon={faUser}
              width ="15px"
              />
              </div> 
              Users Management
            </Link>
            <Link class="nav-link" href="/Admin/BorrowedInfo">
              <div class="sb-nav-link-icon">
              <FontAwesomeIcon 
              icon={faInfo}
              width ="18px"
              />
              </div>
              Borrowing Information
            </Link>
            <Link class="nav-link" href="/Admin/ItemsManage">
              <div class="sb-nav-link-icon">
              <FontAwesomeIcon 
              icon={faTools}
              width ="20px"
              />
              </div>
              Item Management
            </Link>
          </div>
        </div>
        <div class="sb-sidenav-footer">
          <div class="small">Logged in as:</div>
          Admin
        </div>
      </nav>
    </div>
    </>
  );
}

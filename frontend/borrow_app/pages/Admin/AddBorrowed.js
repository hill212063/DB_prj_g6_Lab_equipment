import AdminFooter from "@/components/AdminFooter";
import AdminNavbar from "@/components/AdminNavbar";
import AdminSidebar from "@/components/AdminSidebar";
import Head from "next/head";
// Import the FontAwesomeIcon component
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import the icons you need
import {
  faClock,
  faBars
} from "@fortawesome/free-solid-svg-icons";
import { useState,useEffect } from "react";
import axios from "axios";
import Link from "next/link";
import { useRouter } from 'next/router';
export default function AddBorrowed(params) {
  const router = useRouter()

  useEffect(() => {
    let role = window.localStorage.getItem('role');
    let token = window.localStorage.getItem('token');
    if((role !== 'Admin') || !token){
      router.push('/')
    }
  }, []);

  const [b_item,setb_item] = useState("") 
  const [b_user,setb_user] = useState("")
  const [b_borrow_time,setb_borrow_time] = useState("")
  const [b_return_time,setb_return_time] = useState("")
  const [b_location,setb_location] = useState("")
  const [b_note,setb_note] = useState("")
  const handleOnSubmit = (e) =>{
    e.preventDefault();
    // console.log(new Date(b_borrow_time).toISOString().slice(0, 19).replace('T', ' '))
    axios.post(`${process.env.NEXT_PUBLIC_BASE_URL_BACKEND}/api/dashboard/borrowing-info/add/`,
    {b_item,b_user,
      b_borrow_time:new Date(b_borrow_time).toISOString().slice(0, 19).replace('T', ' '),
      b_return_time:new Date(b_return_time).toISOString().slice(0, 19).replace('T', ' '),
      b_location,b_note })
    .then((Response)=>{
      // console.log(Response)
      router.push('/Admin/BorrowedInfo')
    })
    .catch((error)=>{
      console.log(error)
    })
  }

  const handleb_itemChange = (e) =>{
    setb_item(e.target.value)
  }
  const handleb_userChange = (e) =>{
    setb_user(e.target.value)
  }
  const handleb_borrow_timeChange = (e) =>{
    setb_borrow_time(e.target.value)
  }
  const handleb_return_timeChange = (e) =>{
    setb_return_time(e.target.value)
  }
  const handleb_locationChange = (e) =>{
    setb_location(e.target.value)
  }
  const handleb_noteChange = (e) =>{
    setb_note(e.target.value)
  }
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

const handleSidebarToggle = () => {
  setIsSidebarOpen(!isSidebarOpen);
  
};
const ReloadWhenToggle = () => {
  setTimeout(() => {
  location.reload()
}, 200);
};

  return (
    <div className="sb-nav-fixed">
      <Head>
        <title>Add Borrow-Item</title>
      </Head>
      {/* Top navbar */}
      <nav className="sb-topnav navbar navbar-expand navbar-dark bg-dark">
            {/* Navbar Brand */}
            <Link href="/Admin/UsersManage" className="navbar-brand ps-3">
            <div>BORROW APP</div>
            </Link>
            {/* Sidebar Toggle */}
            <button onClick={handleSidebarToggle} className="btn btn-link btn-sm order-1 order-lg-0 me-4 me-lg-0" id="sidebarToggle" >
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

      <div id="layoutSidenav">
        {/* Sidenav */}
        <AdminSidebar isOpen={isSidebarOpen} />
        <div id="layoutSidenav_content">
          <main>
            {/* Dashboard Content */}
            <div className="container-fluid px-4">
              <h1 className="mt-4">Borrowing Infomation</h1>
              <ol className="breadcrumb mb-4">
                <li className="breadcrumb-item active">Borrowing Infomation / Add</li>
              </ol>
              <div className="row">
                <div className="col-md-12">
                  <div className="card">
                    <div className="card-header">
                      <h4> Add Borrow-Item </h4>
                    </div>
                    <div className="card-body">
                      <form onSubmit={handleOnSubmit} method="post">
                        <div className="row">
                          <div className="col-md-6 mb-3">
                            <label htmlFor="">Item ID</label>
                            <input
                              type="text"
                              name="itemname"
                              className="form-control"      
                              value={b_item}
                              onChange = {handleb_itemChange}  
                              maxLength={50}                  
                            />
                          </div>
                          <div className="col-md-6 mb-3">
                            <label htmlFor="">Email</label>
                            <input
                              type="email"
                              name="idtype"
                              className="form-control"
                              value={b_user}
                              onChange = {handleb_userChange}
                              maxLength={100}  
                            />
                          </div>
                          <div className="col-md-6 mb-3">
                            <label htmlFor="">Borrow Time</label>
                            <div className="input-group">
                                <input value={b_borrow_time} onChange = {handleb_borrow_timeChange} type="datetime-local" name="btime" className="form-control" />
                                <span className="input-group-text" >
                                    <FontAwesomeIcon icon={faClock} />
                                </span>
                            </div>
                          </div>
                          <div className="col-md-6 mb-3">
                            <label htmlFor="">Return Time</label>
                            <div className="input-group">
                                <input value = {b_return_time} onChange = {handleb_return_timeChange}  type="datetime-local" name="btime" className="form-control" />
                                <span className="input-group-text" >
                                    <FontAwesomeIcon icon={faClock} />
                                </span>
                            </div>
                          </div>
                          <div className="col-md-12 mb-3">
                            <label  htmlFor="">Location</label>
                            <textarea value = {b_location} onChange = {handleb_locationChange} name="location" required className="form-control" rows="4"></textarea>
                          </div>
                          <div className="col-md-12 mb-3">
                            <label   htmlFor="">Note</label>
                            <textarea value={b_note} onChange = {handleb_noteChange} name="note" required className="form-control" rows="4"></textarea>
                          </div>
                          
                          <div className="col-md-12 mb-3">
                            <button
                              type="submit"
                              name="add_user"
                              className="btn btn-primary"
                            >
                              Add Borrow-Item
                            </button>
                            <Link onClick={ReloadWhenToggle} href={"/Admin/BorrowedInfo"}
                              className="btn btn-danger"
                            >
                              Cancel
                            </Link>
                          </div>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </main>
          {/* Footer */}
          <AdminFooter />
        </div>
      </div>
    </div>
  );
}

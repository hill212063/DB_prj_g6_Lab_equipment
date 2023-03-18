// Import the FontAwesomeIcon component
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import the icons you need
import {
  faBars
} from "@fortawesome/free-solid-svg-icons";
import AdminFooter from "@/components/AdminFooter";
import AdminNavbar from "@/components/AdminNavbar";
import AdminSidebar from "@/components/AdminSidebar";
import Head from "next/head";
import { useState,useEffect } from "react";
import axios from "axios";
import Link from "next/link";
import FormData from 'form-data'
import { useRouter } from 'next/router';

export default function AddItems(params) {

  const router = useRouter()

  useEffect(() => {
    let role = window.localStorage.getItem('role');
    let token = window.localStorage.getItem('token');
    if((role !== 'Admin') || !token){
      router.push('/')
    }
  }, []);
  const [images, setImages] = useState([]);
  const [item_id,setitem_id] = useState("")
  const [item_id_type,setitem_id_type] = useState("")
  const [item_name,setitem_name] = useState("")
  const [item_category,setitem_category] = useState("")
  const [item_department,setitem_department] = useState("")
  const [item_major,setitem_major] = useState("")
  const [item_status,setitem_status] = useState("")
  const [item_borrow_status,setitem_borrow_status] = useState("")
  const [item_description,setitem_description] = useState("")
  const [item_note,setitem_note] = useState("")

  const [item_img_url, setImagesURLs] = useState([]);

  useEffect(() => {
    if (images.length < 1) return;
    const newImageUrls = [];
    images.forEach(image => newImageUrls.push(URL.createObjectURL(image)))
    setImagesURLs(newImageUrls)
  }, [images]); 
  
  const handleitem_ImageChange = (e) =>{
    setImages([e.target.files[0]])
    // console.log([e.target.files[0]])
  }
  const handleitem_idChange = (e) =>{
    setitem_id(e.target.value)
  }
  const handleitem_id_typeChange = (e) =>{
    setitem_id_type(e.target.value)
  }
  const handleitem_nameChange = (e) =>{
    setitem_name(e.target.value)
  }
  const handleitem_categoryeChange = (e) =>{
    setitem_category(e.target.value)
  }
  const handleitem_departmentChange = (e) =>{
    setitem_department(e.target.value)
  }
  const handleitem_majorChange = (e) =>{
    setitem_major(e.target.value)
  }
  const handleitem_statusChange = (e) =>{
    setitem_status(e.target.value)
  }
  const handleitem_borrow_statusChange = (e) =>{
    setitem_borrow_status(e.target.value)
  }
  const handleitem_descriptionChange = (e) =>{
    setitem_description(e.target.value)
  }
  const handleitem_noteChange = (e) =>{
    setitem_note(e.target.value)
  }
  const handleOnSubmit = (e) =>{
    e.preventDefault();
    let data = new FormData();
    if(images[0] && images[0].name){
      data.append('file',images[0],images[0].name)
    }
    data.append('item_id',item_id)
    data.append('item_id_type',item_id_type)
    data.append('item_name',item_name)
    data.append('item_category',item_category)
    data.append('item_department',item_department)
    data.append('item_major',item_major)
    data.append('item_status',item_status)
    data.append('item_borrow_status',item_borrow_status)
    data.append('item_description',item_description)
    data.append('item_note',item_note )
    axios.post(`${process.env.NEXT_PUBLIC_BASE_URL_BACKEND}/api/dashboard/item-info/add/`,
    data
    )
    .then((Response)=>{
      // console.log(Response)
      router.push('/Admin/ItemsManage')
    })
    .catch((error)=>{
      console.log(error)
    })
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
        <title>Add Items</title>
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
              <h1 className="mt-4">Items Management</h1>
              <ol className="breadcrumb mb-4">
                <li className="breadcrumb-item active">Items Management / Add</li>
              </ol>
              <div className="row">
                <div className="col-md-12">
                  <div className="card">
                    <div className="card-header">
                      <h4> Add Item</h4>
                    </div>
                    <div className="card-body">
                      <form onSubmit ={handleOnSubmit} method="post">
                        <div className="row">
                          <div className="col-md-6 mb-3">
                            <label htmlFor="">Item ID</label>
                            <input
                              type="text"
                              name="itemid"
                              className="form-control"
                              value={item_id}
                              maxLength={50}
                              onChange={handleitem_idChange}
                            />
                          </div>
                          {/* <div className="col-md-6 mb-3">
                            <label htmlFor="">Item ID Type</label>
                            <input
                              type="text"
                              name="idtype"
                              className="form-control"
                              value={item_id_type}
                              onChange = {handleitem_id_typeChange}
                            />
                          </div> */}
                          <div className="col-md-6 mb-3">
                            <label htmlFor="">Item ID Type</label>
                            <select value={item_id_type} onChange={handleitem_id_typeChange} name="physStatus" require={toString()} className="form-control">
                              <option value="">--Select ID Type--</option>
                              <option value="1">Commodity</option>
                              <option value="2">Custom</option>
                              
                            </select>
                          </div>
                          <div className="col-md-6 mb-3">
                            <label htmlFor="">Item Name</label>
                            <input
                              type="text"
                              name="Itemname"
                              className="form-control"
                              value={item_name}
                              maxLength={100}
                              onChange = {handleitem_nameChange}
                            />
                          </div>
                          <div className="col-md-6 mb-3">
                            <label htmlFor="">Item Type(Category)</label>
                            <select value={item_category} onChange = {handleitem_categoryeChange} name="department" require={toString()} className="form-control">
                              <option value="">--Select Category--</option>
                              <option value="1">Multimeter</option>
                              <option value="2">Oscilloscope</option>
                              <option value="3">Function Generator</option>
                              <option value="4">Lab Table</option>
                              <option value="5">Experiment Set</option>
                              <option value="6">PLC</option>
                            </select>
                          </div>
                          <div className="col-md-6 mb-3">
                            <label htmlFor="">Department</label>
                            <select value={item_department} onChange = {handleitem_departmentChange} name="department" require={toString()} className="form-control">
                              <option value="">--Select Department--</option>
                              <option value="1">ECE</option>
                            </select>
                          </div>
                          <div className="col-md-6 mb-3">
                            <label htmlFor="">Major</label>
                            <select value={item_major} onChange = {handleitem_majorChange} name="major" require={toString()} className="form-control">
                              <option value="">--Select Major--</option>
                              <option value="1">EE</option>
                              <option value="2">MEE</option>
                              <option value="3">DEE</option>
                              <option value="4">Cpr.E</option>
                            </select>
                          </div>
                          <div className="col-md-6 mb-3">
                            <label htmlFor="">Physical Status</label>
                            <select value={item_status} onChange={handleitem_statusChange} name="physStatus" require={toString()} className="form-control">
                              <option value="">--Select Physical Status--</option>
                              <option value="1">Normal (can be used)</option>
                              <option value="2">Unusable(cannot be used)</option>
                              <option value="3">Damaged (still usable)</option>
                            </select>
                          </div>
                          <div className="col-md-6 mb-3">
                            <label htmlFor="">Borrow Status</label>
                            <select value={item_borrow_status} onChange = {handleitem_borrow_statusChange} name="borrowStatus" require={toString()} className="form-control">
                              <option value="">--Select Borrow Status--</option>
                              <option value="1">Borrowed</option>
                              <option value="2">Available</option>
                              <option value="3">Expired</option>
                            </select>
                          </div>

                          <div className="col-md-12 mb-3">
                            <label htmlFor="">Description</label>
                            <textarea value={item_description} onChange={handleitem_descriptionChange} name="description" require={toString()} className="form-control" rows="4"></textarea>
                          </div>
                          <div className="col-md-12 mb-3">
                            <label htmlFor="">Note</label>
                            <textarea value={item_note} onChange={handleitem_noteChange} name="note" require={toString()} className="form-control" rows="4"></textarea>
                          </div>

                           {/* Select picture Btn here */}
                           <div className="col-md-12 mb-3">
                            <label htmlFor="">Picture</label>
                            <div className="input-group">
                              <div className="custom-file">
                                <input type="file" multiple className="custom-file-input" id="inputGroupFile04" accept="image/*" onChange={handleitem_ImageChange} />
                                <label className="custom-file-label" htmlFor="inputGroupFile04">Choose picture</label>

                              </div>
                              
                              {/* Show image url when select image in directory */}
                              <div id="url-display"></div>
                            </div>
                            {/* Show Picture when select and save picture file in public/items/ */}
                            <div>
                            <img src={item_img_url} alt="" width={300} height={300}></img> 
                            </div>
                          </div>

                          
                          <div className="col-md-12 mb-3">
                            <button
                              type="submit"
                              name="add_user"
                              className="btn btn-primary"
                            >
                              Add Item
                            </button>
                            <Link onClick={ReloadWhenToggle} href={"/Admin/ItemsManage"}
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

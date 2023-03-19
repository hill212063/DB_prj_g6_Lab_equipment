
import AdminFooter from "@/components/AdminFooter";
import AdminNavbar from "@/components/AdminNavbar";
import AdminSidebar from "@/components/AdminSidebar";
import Head from "next/head";
import Link from "next/link";
import axios from "axios";
import {  useEffect,useState } from "react";
import { useRouter } from "next/router";
import DataTable from 'react-data-table-component';
// Import the FontAwesomeIcon component
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import the icons you need
import {
  faUser,
  faInfo,
  faTools,
  faBars

} from "@fortawesome/free-solid-svg-icons";

export default function BorrowedInfo() {
  const [BorrowedItem,setBorrowedItem] = useState([])
  const [search,setSearch] = useState("");
  const [filteredItems, setFilteredItems] = useState([]);

  const fetchData = async () => {
    try {
      axios.get(`${process.env.NEXT_PUBLIC_BASE_URL_BACKEND}/api/update-expire/`)
      .then(res =>{
        axios.get(`${process.env.NEXT_PUBLIC_BASE_URL_BACKEND}/api/dashboard/borrowing-info/`)
        .then(response => {
          // console.log(response);
          setBorrowedItem(response.data);
          setFilteredItems(response.data);
        })
        .catch(error => {
          console.log(error);
        });  
      }
      ).catch(error => {
        console.log(error);
      });

    } catch (error) {
      console.log(error);
    }
  }

  const router = useRouter()

  useEffect(() => {
    let role = window.localStorage.getItem('role');
    let token = window.localStorage.getItem('token');
    if((role !== 'Admin') || !token){
      router.push('/')
    }
    fetchData();
  }, []);

  useEffect(() => {
    const result = BorrowedItem.filter(BorrowedItem => {
      return BorrowedItem.b_item.toLowerCase().match(search.toLowerCase());
    })

    setFilteredItems(result);
  }, [search])
  
  const handleDelelte = (b_id) => {
    axios.delete(`${process.env.NEXT_PUBLIC_BASE_URL_BACKEND}/api/dashboard/borrowing-info/delete/${parseInt(b_id)}/`)
    .then((response) => {
      // console.log(response.data);
      fetchData()
    })
    .catch((error) => {
      console.error(error);
    });
};

const columns = [
  {
    name : "BORROW INFO ID",
    selector: row => row.b_id,
      sortable: true,
      sortField: "b_id",
      style: {
        fontSize: "15px", fontWeight: "bold"

      }
  },
  {
    name : "EMAIL",
    selector: row => row.b_user,
      sortable: true,
      sortField: "b_user",
      style: {
        fontSize: "16px",

      }
  },
  // {
  //   name : "BORROW TIME",
  //   selector: row => row.b_borrow_time,
  //     sortable: true,
  //     sortField: "b_borrow_time",
  //     style: {
  //       fontSize: "16px",

  //     }
  // },
  {
    name : "BORROW TIME",
    selector: row => (new Date(row.b_borrow_time)).toLocaleString('en-US', {
      dateStyle: 'medium',
        timeStyle: 'medium',
        hour12: false,
    }),
      sortable: true,
      sortField: "b_borrow_time",
      style: {
        fontSize: "17px",

      }
  },
  {
    name: "RETURN TIME",
    selector: row => (new Date(row.b_return_time)).toLocaleString('en-US', {
      dateStyle: 'medium',
        timeStyle: 'medium',
        hour12: false,
    }),
      sortable: true,
      sortField: "b_return_time",
      style: {
        fontSize: "17px",

      }
  },
  {
    name : "LOCATION",
    selector: row => row.b_location,
      sortable: true,
      sortField: "b_location",
      style: {
        fontSize: "16px",

      }
  },
  {
    name : "NOTE",
    selector: row => row.b_note,
      sortable: true,
      sortField: "b_note",
      style: {
        fontSize: "16px",

      }
  },
  {
    name : "EDIT / MORE",
    cell: row => <Link href={`/Admin/EditBorrowed?id=${row.b_id}`} className="btn btn-success">Edit</Link>
  },
  {
    name: "DELETE",
    cell: (row) => (
      <button
        onClick={() => handleDelelte(row.b_id)}
        name="item_delete"
        className="btn btn-danger"
      >
        Delete
      </button>
    ),
  },
  
]

const [isSidebarOpen, setIsSidebarOpen] = useState(false);

const handleSidebarToggle = () => {
  setIsSidebarOpen(!isSidebarOpen);
  
};


    return(
      <div className="sb-nav-fixed">
      <Head>
        <title>Borrowing Infomation</title>
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
        {" "}
        {/* Sidenav */}
        <AdminSidebar isOpen={isSidebarOpen} />
        <div id="layoutSidenav_content">
          <main>
            {/* Dashboard Content */}
            <div className="container-fluid px-4">
              {/* header */}
              <h1 className="mt-4">Borrowing Infomation</h1>
              {/* header */}

              {/* sub-header */}
              <ol className="breadcrumb mb-4">
                            <li className="breadcrumb-item"><Link href="/Admin"> Dashboard</Link></li>
                            <li className="breadcrumb-item active">Borrowing Infomation</li>
                        </ol>
              {/* sub-header */}

              {/* card */}
              <div className="row">
                <div className="col-md-12">
                  <div className="card">
                    {/* card header */}
                    <div className="card-header">
                      <h4>
                        {" "}
                        Borrowing Infomation
                        <Link href="/Admin/AddBorrowed">
                        <div className="btn btn-primary float-end">
                          Add
                        </div>
                        </Link>
                      </h4>
                    </div>
                    {/* card header */}

                    {/* card body */}
                    <div className="card-body">
                      {/* card body */}

                      {/* registered users table */}
                      <DataTable 
                                columns={columns} 
                                data={filteredItems} 
                                pagination
                                fixedHeader
                                fixedHeaderScrollHeight="500px"
                                highlightOnHover
                                actions={
                                  <input 
                                    type="text" 
                                    placeholder="Search by Items name" 
                                    className="w-50 form-control"
                                    value={search}
                                    onChange={(e) => setSearch(e.target.value)}
                                    >
                                    </input>}
                                
                                
                                >

                                </DataTable>
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
    )
};

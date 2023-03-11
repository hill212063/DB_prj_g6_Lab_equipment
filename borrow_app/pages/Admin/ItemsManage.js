import AdminFooter from "@/components/AdminFooter";
import AdminNavbar from "@/components/AdminNavbar";
import AdminSidebar from "@/components/AdminSidebar";
import Head from "next/head";
import Link from "next/link";

export default function ItemsManage() {
  return (
    <div class="sb-nav-fixed">
      <Head>
        <title>Items Management</title>
      </Head>
      {/* Top navbar */}
      <AdminNavbar />

      <div id="layoutSidenav">
        {/* Sidenav */}
        <AdminSidebar />
        <div id="layoutSidenav_content">
          <main>
            {/* Dashboard Content */}
            <div class="container-fluid px-4">
              {/* header */}
              <h1 class="mt-4">Items Management</h1>
              {/* header */}

              {/* sub-header */}
              <ol class="breadcrumb mb-4">
                <li class="breadcrumb-item active">
                  Dashboard / Items Management
                </li>
              </ol>
              {/* sub-header */}

              {/* card */}
              <div class="row">
                <div class="col-md-12">
                  <div class="card">
                    {/* card header */}
                    <div class="card-header">
                      <h4>
                        {" "}
                        Items Management
                        <Link href="/Admin/AddItems" class="btn btn-primary float-end">
                          Add
                        </Link>
                      </h4>
                    </div>
                    {/* card header */}

                    {/* card body */}
                    <div class="card-body">
                      {/* card body */}

                      {/* registered users table */}
                      <table class="table table-bordered">
                        {/* table header */}
                        <thead>
                          <tr>
                            <th>ITEM ID</th>
                            <th>ITEM TYPE</th>
                            <th>ITEM NAME</th>
                            <th>FACULTY</th>
                            <th>DEPARTMENT</th>
                            <th>BORROW STATUS</th>
                            <th>Edit</th>
                            <th>Delete</th>
                          </tr>
                        </thead>

                        <tbody>
                            <tr>
                                <td>ad</td>
                                <td>ad</td>
                                <td>ad</td>
                                <td>asd</td>
                                <td>asd</td>
                                <td>asd</td>
                                <td>
                                    <Link href="/Admin/EditItems" class="btn btn-success">Edit</Link>
                                </td>
                                <td>
                                <form method="post">
                                <button type="sumbit" name="user_delete"  class="btn btn-danger">Delete</button>
                                </form>
                                </td>
                            </tr>
                            
                            {/* table header */}
                            {/* Put Data here */}
                            <tr>
                                <td>ad</td>
                                <td>ad</td>
                                <td>ad</td>
                                <td>asd</td>
                                <td>asd</td>
                                <td>asd</td>
                                <td>
                                    <Link href="/Admin/EditItems" class="btn btn-success">Edit</Link>
                                </td>
                                <td>
                                <form method="post">
                                <button type="sumbit" name="user_delete"  class="btn btn-danger">Delete</button>
                                </form>
                                </td>
                            </tr>
 
                        </tbody>     
                        
                      </table>
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

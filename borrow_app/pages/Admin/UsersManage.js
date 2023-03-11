import AdminFooter from "@/components/AdminFooter";
import AdminNavbar from "@/components/AdminNavbar";
import AdminSidebar from "@/components/AdminSidebar";
import Head from "next/head";
import Link from "next/link";

export default function UsersManage() {
  return (
    <div class="sb-nav-fixed">
      <Head>
        <title>Users Management</title>
      </Head>
      {/* Top navbar */}
      <AdminNavbar />

      <div id="layoutSidenav">
        {" "}
        {/* Sidenav */}
        <AdminSidebar />
        <div id="layoutSidenav_content">
          <main>
            {/* Dashboard Content */}
            <div class="container-fluid px-4">
              {/* header */}
              <h1 class="mt-4">User Management</h1>
              {/* header */}

              {/* sub-header */}
              <ol class="breadcrumb mb-4">
                <li class="breadcrumb-item active">
                  Dashboard / User Management
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
                        Registered User
                        <Link href="/Admin/AddUser" class="btn btn-primary float-end">
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
                            <th>ID</th>
                            <th>NAME</th>
                            <th>TELEPHONE</th>
                            <th>FACULTY</th>
                            <th>DEPARTMENT</th>
                            <th>ROLE</th>
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
                                    <Link href="/Admin/EditUser" class="btn btn-success">Edit</Link>
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
                                  <Link href="/Admin/EditUser" class="btn btn-success">Edit</Link>
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

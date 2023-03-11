import AdminFooter from "@/components/AdminFooter";
import AdminNavbar from "@/components/AdminNavbar";
import AdminSidebar from "@/components/AdminSidebar";
import Head from "next/head";
import Link from "next/link";

export default function BorrowedInfo() {
    return(
      <div class="sb-nav-fixed">
      <Head>
        <title>Borrowing Infomation</title>
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
              <h1 class="mt-4">Borrowing Infomation</h1>
              {/* header */}

              {/* sub-header */}
              <ol class="breadcrumb mb-4">
                <li class="breadcrumb-item active">
                  Dashboard / Borrowing Infomation
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
                        Borrowing Infomation
                        <Link href="/Admin/AddBorrowed">
                        <div class="btn btn-primary float-end">
                          Add
                        </div>
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
                            <th>ITEM NAME</th>
                            <th>USER</th>
                            <th>BORROW TIME</th>
                            <th>RETURN TIME</th>
                            <th>LOCATION</th>
                            <th>NOTE</th>
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
                                <Link href="/Admin/EditBorrowed">
                                <div className="btn btn-success">Edit</div>
                                </Link>
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
                                  <Link href="/Admin/EditBorrowed">
                                  <div className="btn btn-success">Edit</div>
                                  </Link>
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
    )
};

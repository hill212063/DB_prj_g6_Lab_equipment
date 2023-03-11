import AdminFooter from "@/components/AdminFooter";
import AdminNavbar from "@/components/AdminNavbar";
import AdminSidebar from "@/components/AdminSidebar";
import Head from "next/head";

export default function AddUser(params) {
  return (
    <div class="sb-nav-fixed">
      <Head>
        <title>Add User</title>
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
              <h1 class="mt-4">Users Management</h1>
              <ol class="breadcrumb mb-4">
                <li class="breadcrumb-item active">User Management / Add</li>
              </ol>
              <div class="row">
                <div class="col-md-12">
                  <div class="card">
                    <div class="card-header">
                      <h4> Add User/Admin</h4>
                    </div>
                    <div class="card-body">
                      <form method="post">
                        <div class="row">
                          <div class="col-md-6 mb-3">
                            <label for="">Name</label>
                            <input
                              type="text"
                              name="username"
                              class="form-control"
                            />
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">Email Address</label>
                            <input
                              type="text"
                              name="email"
                              class="form-control"
                            />
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">Password</label>
                            <input
                              type="text"
                              name="password"
                              class="form-control"
                            />
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">Telephone</label>
                            <input
                              type="text"
                              name="telephone"
                              class="form-control"
                            />
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">Faculty</label>
                            <select name="faculty" require class="form-control">
                              <option value="">--Select Faculty--</option>
                              <option value="1">ECE</option>
                            </select>
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">Department</label>
                            <select name="department" require class="form-control">
                              <option value="">--Select Department--</option>
                              <option value="3">EE</option>
                              <option value="2">MEE</option>
                              <option value="1">DEE</option>
                              <option value="0">Cpr.E</option>
                            </select>
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">Role as</label>
                            <select name="role_as" require class="form-control">
                              <option value="">--Select Role--</option>
                              <option value="1">Admin</option>
                              <option value="0">User</option>
                            </select>
                          </div>
                          
                          <div class="col-md-12 mb-3">
                            <button
                              type="submit"
                              name="add_user"
                              class="btn btn-primary"
                            >
                              Add User/Admin
                            </button>
                            <button
                              type="submit"
                              name="cancel"
                              class="btn btn-danger"
                            >
                              Cancel
                            </button>
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

import AdminFooter from "@/components/AdminFooter";
import AdminNavbar from "@/components/AdminNavbar";
import AdminSidebar from "@/components/AdminSidebar";
import Head from "next/head";
// Import the FontAwesomeIcon component
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import the icons you need
import {
  faClock
} from "@fortawesome/free-solid-svg-icons";


export default function EditBorrowed(params) {
    return(
        <div class="sb-nav-fixed">
      <Head>
        <title>Edit Borrow-Item</title>
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
              <h1 class="mt-4">Borrowing Infomation</h1>
              <ol class="breadcrumb mb-4">
                <li class="breadcrumb-item active">Borrowing Infomation / Edit</li>
              </ol>
              <div class="row">
                <div class="col-md-12">
                  <div class="card">
                    <div class="card-header">
                      <h4> Edit Borrow-Item </h4>
                    </div>
                    <div class="card-body">
                      <form method="post">
                        <div class="row">
                          <div class="col-md-6 mb-3">
                            <label for="">Item Name</label>
                            <input
                              type="text"
                              name="itemname"
                              class="form-control"
                            />
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">User</label>
                            <input
                              type="text"
                              name="idtype"
                              class="form-control"
                            />
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">Borrow Time</label>
                            <div className="input-group">
                                <input type="datetime-local" name="btime" className="form-control" />
                                <span className="input-group-text" >
                                    <FontAwesomeIcon icon={faClock} />
                                </span>
                            </div>
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">Return Time</label>
                            <div className="input-group">
                                <input type="datetime-local" name="btime" className="form-control" />
                                <span className="input-group-text" >
                                    <FontAwesomeIcon icon={faClock} />
                                </span>
                            </div>
                          </div>
                          <div class="col-md-12 mb-3">
                            <label for="">Location</label>
                            <textarea name="location" required class="form-control" rows="4"></textarea>
                          </div>
                          <div class="col-md-12 mb-3">
                            <label for="">Note</label>
                            <textarea name="note" required class="form-control" rows="4"></textarea>
                          </div>
                          
                          <div class="col-md-12 mb-3">
                            <button
                              type="submit"
                              name="add_user"
                              class="btn btn-success"
                            >
                              Update
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
    )
};

import AdminFooter from "@/components/AdminFooter";
import AdminNavbar from "@/components/AdminNavbar";
import AdminSidebar from "@/components/AdminSidebar";
import Head from "next/head";
import Image from 'next/image';

export default function EditItems(params) {
    return(
        <div class="sb-nav-fixed">
      <Head>
        <title>Edit Items</title>
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
              <h1 class="mt-4">Items Management</h1>
              <ol class="breadcrumb mb-4">
                <li class="breadcrumb-item active">Items Management / Edit</li>
              </ol>
              <div class="row">
                <div class="col-md-12">
                  <div class="card">
                    <div class="card-header">
                      <h4> Edit Item</h4>
                    </div>
                    <div class="card-body">
                      <form method="post">
                        <div class="row">
                          <div class="col-md-6 mb-3">
                            <label for="">Item ID</label>
                            <input
                              type="text"
                              name="itemid"
                              class="form-control"
                            />
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">Item ID Type</label>
                            <input
                              type="text"
                              name="idtype"
                              class="form-control"
                            />
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">Item Name</label>
                            <input
                              type="text"
                              name="Itemname"
                              class="form-control"
                            />
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">Item Type(Category)</label>
                            <select name="faculty" require class="form-control">
                              <option value="">--Select Faculty--</option>
                              <option value="3">Resistor</option>
                              <option value="2">IC Module</option>
                              <option value="1">Osciiloscope</option>
                              <option value="0">Powersupply</option>
                            </select>
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
                            <label for="">Physical Status</label>
                            <select name="physStatus" require class="form-control">
                              <option value="">--Select Role--</option>
                              <option value="3">Defective (cannot be used)</option>
                              <option value="1">Normal (can be used)</option>
                              <option value="0">Slightly damaged (still usable)</option>
                            </select>
                          </div>
                          <div class="col-md-6 mb-3">
                            <label for="">Borrow Status</label>
                            <select name="borrowStatus" require class="form-control">
                              <option value="">--Select Role--</option>
                              <option value="3">Borrowed</option>
                              <option value="1">Available</option>
                              <option value="0">Past due</option>
                            </select>
                          </div>

                          <div class="col-md-12 mb-3">
                            <label for="">Description</label>
                            <textarea name="description" required class="form-control" rows="4"></textarea>
                          </div>
                          <div class="col-md-12 mb-3">
                            <label for="">Note</label>
                            <textarea name="note" required class="form-control" rows="4"></textarea>
                          </div>

                          {/* Select picture Btn here */}
                          <div class="col-md-12 mb-3">
                            <label for="">Picture</label>
                            <div class="input-group">
                              <div class="custom-file">
                                <input type="file" class="custom-file-input" id="inputGroupFile04" aria-describedby="inputGroupFileAddon04"/>
                                <label class="custom-file-label" for="inputGroupFile04">Choose Picture</label>
                              </div>
                              
                              {/* Show image url when select image in directory */}
                              <div id="url-display"></div>
                            </div>
                            {/* Show Picture when select and save picture file in public/items/ */}
                            <div>
                              <Image id="picture-preview" width={300} height={300}/>
                            </div>
                          </div>
                          
                          <div class="col-md-12 mb-3">
                            <button
                              type="submit"
                              name="add_user"
                              class="btn btn-success"
                            >
                              Update Item
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

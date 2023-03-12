import '@/styles/globals.css'
import Script from 'next/script';

// import Font Awesome CSS
import "@fortawesome/fontawesome-svg-core/styles.css"; 

import { config } from "@fortawesome/fontawesome-svg-core";
// Tell Font Awesome to skip adding the CSS automatically 
// since it's already imported above
config.autoAddCss = false; 

export default function App({ Component, pageProps }) {
  return (
    <>
    <Script>
      
    </Script>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/simple-datatables@latest" crossorigin="anonymous"></script>
  <Component {...pageProps} /> 
    </>
  )
}

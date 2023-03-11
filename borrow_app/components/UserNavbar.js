import Link from "next/link"

export default function UserNavbar() {
    return (
        <>
        <nav class="userNav">
            <div class="Logo">
                <Link href="/">BORROW APP</Link>

            </div>
            <div class="NavBTN">
            <Link href="/Admin">Dashboard</Link>
            <Link href="/Items">Items</Link>
            <Link href="/MyBorrowed">My borrowed</Link>
            <Link href="/Contact">Contact</Link>
            </div>
        </nav>
        </>
    )
    
};

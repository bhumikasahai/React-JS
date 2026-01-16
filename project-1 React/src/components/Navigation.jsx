const Navigation = () => {

return(
    <nav className="container">
        <div className="logo">
            <img src="/Nike_Logo_Png.png" alt="logo" style={{ width: "120px", height: "120px" }}></img>
        </div>
        <ul>
            <li href="#">Menu</li>
            <li href="#">Location</li>
            <li href="#">About</li>
            <li href="#">Contact</li>
        </ul>
        <button>login</button>
    </nav>
    );
};

export default Navigation;
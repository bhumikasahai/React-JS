import styles from './Navigation.module.css';

const Navigation = () => {
    console.log(styles);

    return (
        <nav>
            <div className={`${styles.navigation} conatiner`}>
                <img src="/frame-img.png" alt="do some coding" style={{ width: "60px", height: "60px" }}></img>
            </div>
            <ul>
                <li>Home</li>
                <li>About</li>
                <li>Contact</li>
            </ul>
        </nav>
    );
};
export default Navigation;
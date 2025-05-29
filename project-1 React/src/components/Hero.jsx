const HeroSection = () => {
    return (
        <main className="hero container">
            <div className="hero-wrapper">
                {/* Left side content */}
                <div className="hero-content">
                    <h1>YOUR FEET DESERVE <br></br>THE BEST</h1>
                    <p>YOUR FEET DESERVE THE BEST AND WE'RE HERE TO HELP YOU WITH OUR SHOES.</p>
                    <p>YOUR FEET DESERVE THE BEST AND WE'RE HERE TO HELP YOU WITH OUR SHOES.</p>
                    <div className="hero-button">
                        <button>SHOPNOW</button>
                        <button className="secondary-btn">CATEGORY</button>
                    </div>
                    <div className="shopping">
                        <p>Also available on</p>
                        <div className="brand-icons">
                            <img src="/amazon-logo.png" alt="amazon-logo" style={{ width: "40px", height: "40px" }} />
                            <img src="/flipkart-logo.png" alt="flipkart-logo" style={{ width: "40px", height: "40px" }} />
                        </div>
                    </div>
                </div>

                {/* Right side image */}
                <div className="hero-image">
                    <img src="/nike-shoes-img.png" alt="shoe-image" style={{ width: "400px", height: "auto" }} />
                </div>
            </div>
        </main>
    );
};

export default HeroSection;

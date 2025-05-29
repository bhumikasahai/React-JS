import styles from './ContactForm.module.css';
import Button from '../Button/Button';
import { TbMessageFilled } from "react-icons/tb";
import { FaPhoneAlt } from "react-icons/fa"; 
import { HiMail } from "react-icons/hi";
import { useState } from 'react';

const ContactForm = () => {
    const[name,setName] = useState("Ojasvi");
    const[email,setEmail] = useState("suport@gmail.com");
    const[text,setText] = useState("how may I help you");

    const onviaCallSubmit = () => {
        console.log("I am free for call");
    }
    const onSubmit = (event) => {
        event.preventDefault();
        setName(event.target[0].value);
        setEmail(event.target[1].value);
        setText(event.target[2].value);
    };

    return (
        <section className={styles.container}>
            <div className={styles.contact_form}>
                <div className={styles.top_btn}>
                    <Button text="VIA SUPPORT CHAT" icon={<TbMessageFilled fontSize="24px" />}/>
                    <Button 
                        onClick={onviaCallSubmit}
                        text="VIA CALL" icon={<FaPhoneAlt fontSize="24px"/>} />
                </div>
                <Button 
                isOutline = {true}
                text="VIA EMAIL FORM" icon={<HiMail fontSize="24px"/>} />
                <form onSubmit={onSubmit}>
                    <div className={styles.form_control}>
                        <label htmlFor='name'>Name</label> 
                        <input type='text' name='name' />
                    </div>
                    <div className={styles.form_control}>
                        <label htmlFor='email'>EMail</label> 
                        <input type='email' name='email' />
                    </div>
                    <div className={styles.form_control}>
                        <label htmlFor='text'>Text</label> 
                        <textarea name='text' rows={6}/>
                    </div>
                    <div style={{  
                            display:"flex", 
                            justifyContent:"end",
                        }}>
                        <Button text = "SUBMIT" />
                            <div>{d name + " " + email + " " + text}</div>
                    </div>
                </form>
            </div>
            <div className={styles.contact_page}>
                <img src="/contact_img.png" alt="contact image" style={{ width: "500px", height: "400px" }}/>
            </div>
        </section>
    );
};

export default ContactForm;

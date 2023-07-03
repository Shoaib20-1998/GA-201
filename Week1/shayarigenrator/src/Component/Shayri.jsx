import React, { useState } from 'react';
import axios from 'axios'
import './Shayri.css'
function ShayriGenerator() {
    const [inputValue, setInputValue] = useState('');
    const [generatedShayri, setGeneratedShayri] = useState('');
    const handleSubmit = async () => {

        try {
            if (inputValue) {
                const response = await axios.post('https://chatgpt-intergration.onrender.com/shayari', { message: `world's best Shayri about ${inputValue} in hindi and keep it in 4 lines` });
                setGeneratedShayri(response.data.reply)
                setInputValue("")
            }else{
                alert("please write a keyword of shayri")
            }

        } catch (error) {
            console.log('Error:', error);
        }
    };

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    };

    return (
        <div className="container">
            <h1 className="title">Shayri Generator</h1>
            <div className="input-container">
                <input
                    type="text"
                    className="input"
                    placeholder="Enter a keyword here"
                    value={inputValue}
                    onChange={handleInputChange}
                />
                <button className="generate-btn" onClick={handleSubmit}>
                    Generate
                </button>
            </div>
            {generatedShayri && (
                <div className="shayri-container">
                    <h2 className="shayri-title">Generated Shayri:</h2>
                    <p className="shayri-text">{generatedShayri}</p>
                </div>
            )}
        </div>
    );
}

// Define the styles as objects
const containerStyle = {
    maxWidth: '600px',
    margin: '0 auto',
    padding: '20px',
};

const titleStyle = {
    fontSize: '24px',
    textAlign: 'center',
};

const inputContainerStyle = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    marginTop: '20px',
};

const inputStyle = {
    width: '100%',
    maxWidth: '400px',
    padding: '10px',
    borderRadius: '4px',
    border: '1px solid #ccc',
};

const buttonStyle = {
    marginTop: '10px',
    padding: '10px 20px',
    borderRadius: '4px',
    border: 'none',
    backgroundColor: '#007bff',
    color: '#fff',
    cursor: 'pointer',
};

const shayriContainerStyle = {
    marginTop: '40px',
    padding: '20px',
    borderRadius: '8px',
    backgroundColor: '#fff',
    boxShadow: '0 2px 6px rgba(0, 0, 0, 0.15)',
    animation: 'fade-in 0.5s ease-in-out',
};

const shayriTitleStyle = {
    fontSize: '20px',
    marginBottom: '10px',
};

const shayriTextStyle = {
    fontSize: '18px',
};

export default ShayriGenerator;

import React, { useState } from 'react';
import './Code.css'
import axios from 'axios'
const Converter = () => {
    const [input, setInput] = useState('');
    const [output, setOutput] = useState('');
    const [targetLanguage, setTargetLanguage] = useState('');
    const [loading, setloading] = useState(false)
    const [loading1, setloading1] = useState(false)
    const [loading2, setloading2] = useState(false)


    const handleInputChange = (e) => {
        setInput(e.target.value);
    };
    console.log(input)
    const handleConvert = () => {
        if (targetLanguage && input) {
            setloading(true)
            axios
                .post('https://chatgpt-intergration.onrender.com/convertor', { message: `${input} convert the following code into ${targetLanguage} and give me output only in code.` })
                .then((response) => {
                    setOutput(response.data.reply);
                    setloading(false)

                })
                .catch((error) => {
                    console.error('Error:', error);
                });

        } else if (!targetLanguage) {
            alert("Please Select Target Language")
        } else {
            alert("please give an input code")
        }

    };

    const handleTargetLanguageChange = (e) => {
        setTargetLanguage(e.target.value);
    };
    const handleDebugger = () => {
        if (input) {
            setloading1(true)
            axios
                .post('https://chatgpt-intergration.onrender.com/debuger', { message: `${input} debug the following code` })
                .then((response) => {
                    setOutput(response.data.reply)
                    setloading1(false)
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        } else {
            alert("please give an input code")
        }
    };

    const handleQualityCheck = () => {
        if (input) {
            setloading2(true)
            axios
                .post('https://chatgpt-intergration.onrender.com/check', { message: `${input} please check the quality of this following code in terms of : 1.time complexity,2. space complexity, 3.clean code, 4.proper comments, 5.No extra code. list all the the things following these paramenter. note: if it can be solve in better way than you can provide it as well in new result section` })
                .then((response) => {
                    // Handle the quality check response as needed
                    setOutput(response.data.reply)
                    setloading2(false)
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        } else {
            alert("please give an input code")
        }
    };

    return (
        <div>

            <h1>Code Converter</h1>
            <textarea className="code-input" value={input} onChange={handleInputChange} placeholder="Enter your code" />
            <div className="select-container">
                <label htmlFor="target-language">Target Language:</label>
                <select id="target-language" value={targetLanguage} onChange={handleTargetLanguageChange}>
                    <option value="">Select Language</option>
                    <option value="python">Python</option>
                    <option value="javascript">JavaScript</option>
                    <option value="C++">C++</option>
                    <option value="Java">Java</option>
                    <option value="PHP">PHP</option>
                    <option value="GO">GO</option>
                    <option value="Typescript">Typescript</option>
                    <option value="Kotlin">Kotlin</option>
                    <option value="C">C</option>
                    {/* Add more options for other languages */}
                </select>
            </div>

           {loading?<button onClick={handleConvert}>Converting....</button>:<button onClick={handleConvert}>Convert</button>} 
           {loading1?<button onClick={handleDebugger}>Debugging...</button>:<button onClick={handleDebugger}>Debugger</button>} 
            {loading2?<button onClick={handleQualityCheck}>Quality Checking...</button>:<button onClick={handleQualityCheck}>Quality Check</button>}
            <pre className="code-output">{output}</pre>
        </div>
    );
};

export default Converter;


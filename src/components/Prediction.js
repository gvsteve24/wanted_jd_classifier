import React, { useState } from "react";
import styled from 'styled-components/macro';
import axios from 'axios';

const Wrapper = styled.div`
    width: 1000px;
    height: 100%;
    margin: 0 auto;

    h2 {
        height: 4rem;
        text-align: center;
        line-height: 4rem;
    }
`;

const TextInput = styled.input.attrs({type: 'text'})`
    font-size: 1em;
    padding: 0 20px;
    color: white;
    font-weight: 600;
    box-sizing: border-box;
    width: 70%;
    height: 5rem;
    line-height: 5rem;
    border: 2px solid black;
    border-radius: 8px;
    background-color: #666;

    ::placeholder {
        font-size: 1em;
        color: white;
        font-weight: 600;
    }
`;

const TextArea = styled.input.attrs({type: 'textarea'})`
    font-size: 1em;
    margin: .3rem 0 0 0;
    padding: 0 20px;
    color: white;
    font-weight: 600;
    box-sizing: border-box;
    width: 70%;
    height: 5rem;
    line-height: 5rem;
    border: 2px solid black;
    border-radius: 8px;
    background-color: #666;

    ::placeholder {
        font-size: 1em;
        color: white;
        font-weight: 600;
    }
`;

const Submit = styled.input.attrs({type: 'submit'})`
    font-size: 18px;
    color: #443E52;
    font-weight: 600;
    line-height: 18px;
    width: 300px;
    height: 50px;
    box-sizing: border-box;
`;

export function Prediction(props){
    const [result, setResult] = useState(undefined);
    const [job, setJob] = useState({
        "position":"",
        "mainTask":"",
        "requirements":"",
        "preferred":"",
    });
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await axios.post('/predict', job);
        if (response && response.data){
            const classified = response.data.class_name;
            setResult(classified);
        }else {
            setResult(null)
        }
    }

    const handleInputChange = (event) => {
        const target = event.target;
        const value = target.value;
        const name = target.name;
    
        setJob({
          ...job,
          [name]: value
        });
    }

    return (
        <Wrapper>
            <h2>포지션, 주요업무, 자격요건, 우대사항을 입력하면 직군을 분류합니다.</h2>
            <form onSubmit={handleSubmit}>
                <TextInput type="text" onChange={handleInputChange} name="position" placeholder="포지션을 입력하세요"/>
                <br/>
                <TextArea type="textarea" onChange={handleInputChange} name="mainTask" placeholder="주요업무를 입력하세요"/>
                <br/>
                <TextArea type="textarea" onChange={handleInputChange} name="requirements" placeholder="자격요건을 입력하세요"/>
                <br/>
                <TextArea type="textarea" onChange={handleInputChange} name="preferred" placeholder="우대사항을 입력하세요"/>
                <br/>
                <Submit button type="submit" value={result ? `${result} 직군입니다` : "직군 예측"}/>
            </form>
        </Wrapper>
    );
}

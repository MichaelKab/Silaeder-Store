import './App.css';
import React, {useState, useEffect} from "react"
import axios from "axios"
/*
function Get_data() {
        const[people, setPeople] = useState([])
        useEffect(() => {
            axios({
                metod: "GET",
                url: "http://127.0.0.1:8000/api/products"
            }).then(response => {
                setPeople(response.data)
            })
        }, [])
        return {people}
}*/

function App(){
    const[text, setText] = useState([])
    useEffect(() => {
                axios({
                    metod: "GET",
                    url: "http://127.0.0.1:8000/api/products/"
                }).then(response => {
                    setText(response.data)
                })
            }, [])
        function Getdata(element) {
            useEffect(() => {
                axios({
                    metod: "GET",
                    url: "http://127.0.0.1:8000/api/" + element + "/"
                }).then(response => {
                    setText(response.data)
                })
            }, [])
        }
        return (
            <div className="App">
                <h1>Hello world</h1>
                <ul>
                    {text.map(p => (
                        <ul>
                            <li>{p.id}</li>
                        </ul>
                    ))}
                </ul>
                <h2>{text}</h2>
            </div>
        );
}

export default App;
